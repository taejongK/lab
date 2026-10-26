# /// script
# requires-python = ">=3.10"
# dependencies = ["laya @ git+https://github.com/NandhaKishorM/laya@432312b36714d8889eba405507b37eda25257d9c"]
# ///
"""Can a System One model (local Laya) drive an NPC on an ASCII 2D map?

uv run probe_ascii_map.py [n_states] [n_episodes]

A  ascii      : map + position + object list, legal directions only, no hints
B  facts      : same, plus per-direction facts computed by code (BFS distance after the move)
B2 short      : same facts, decisive word first ("CLOSER: 3 steps left")
C  target     : pick which object to walk to for a stimulus (semantic judgment); code does the path
Random baselines are computed exactly from the same states.
"""
import json
import random
import statistics
import sys
import time
from collections import deque

import laya

SIZE = 9
DIRS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
OBJECTS = [  # symbol, name, description
    ("A", "apple", "Fresh food. Eating it removes hunger."),
    ("K", "key", "Opens the locked gate."),
    ("F", "campfire", "Warm. Standing next to it removes cold, touching it burns."),
    ("B", "bed", "Sleeping here removes tiredness."),
    ("W", "well", "Drinking water here removes thirst."),
]
STIMULI = {  # stimulus -> correct object name
    "The NPC is very hungry.": "apple",
    "The NPC is shivering from the cold night air.": "campfire",
    "The NPC can barely keep its eyes open.": "bed",
    "The NPC's throat is dry after a long walk.": "well",
    "The NPC wants to get through the locked gate.": "key",
}


def make_world(rng):
    while True:
        walls = {(r, c) for r in range(SIZE) for c in range(SIZE)
                 if r in (0, SIZE - 1) or c in (0, SIZE - 1) or rng.random() < 0.18}
        free = [(r, c) for r in range(SIZE) for c in range(SIZE) if (r, c) not in walls]
        cells = rng.sample(free, 1 + len(OBJECTS))
        agent, objs = cells[0], dict(zip([o[1] for o in OBJECTS], cells[1:]))
        if all(bfs(walls, agent, p) is not None for p in objs.values()):
            return walls, agent, objs


def bfs(walls, start, goal):
    """Shortest path length from start to goal (goal cell is walkable), None if unreachable."""
    dist, q = {start: 0}, deque([start])
    while q:
        p = q.popleft()
        if p == goal:
            return dist[p]
        for dr, dc in DIRS.values():
            n = (p[0] + dr, p[1] + dc)
            if n not in walls and n not in dist:
                dist[n] = dist[p] + 1
                q.append(n)
    return None


def render(walls, agent, objs):
    sym = {p: s for (s, name, _), p in ((o, objs[o[1]]) for o in OBJECTS)}
    rows = []
    for r in range(SIZE):
        rows.append("".join("@" if (r, c) == agent else sym.get((r, c), "#" if (r, c) in walls else ".")
                            for c in range(SIZE)))
    return rows


def state_of(walls, agent, objs, task):
    return {
        "task": task,
        "map": render(walls, agent, objs),
        "legend": "@ = you (the NPC), # = wall, . = floor. Row 0 is the top row, column 0 is the left column. "
                  "up = row - 1, down = row + 1, left = column - 1, right = column + 1.",
        "you": {"row": agent[0], "col": agent[1]},
        "objects": [{"symbol": s, "name": n, "description": d, "row": objs[n][0], "col": objs[n][1]}
                    for s, n, d in OBJECTS],
    }


def legal(walls, agent):
    return [d for d, (dr, dc) in DIRS.items() if (agent[0] + dr, agent[1] + dc) not in walls]


def step(agent, d):
    return agent[0] + DIRS[d][0], agent[1] + DIRS[d][1]


def criteria(walls, agent, target, with_facts):
    now = bfs(walls, agent, target)
    out = {}
    for d in legal(walls, agent):
        nxt = step(agent, d)
        if not with_facts:
            out[d] = f"Move one cell {d}."
            continue
        after = bfs(walls, nxt, target)
        if with_facts == "short":  # decisive fact first, nothing else
            out[d] = f"{'CLOSER' if after < now else 'FARTHER' if after > now else 'SAME'}: {after} steps left"
            continue
        trend = "closer to" if after < now else "farther from" if after > now else "same distance to"
        out[d] = (f"Move {d} to row {nxt[0]} col {nxt[1]}. Afterwards the target is {after} steps away by walking "
                  f"(now {now}), so this moves {trend} the target.")
    return out


def good_moves(walls, agent, target):
    now = bfs(walls, agent, target)
    return {d for d in legal(walls, agent) if bfs(walls, step(agent, d), target) < now}


def ask_move(agent_model, walls, agent, objs, target_name, with_facts):
    target = objs[target_name]
    q = {"move": {"type": "choice",
                  "instructions": f"Which direction should the NPC move next to reach the {target_name} "
                                  f"by the shortest walkable path? Walls (#) block movement.",
                  "criteria": criteria(walls, agent, target, with_facts)}}
    t = time.perf_counter()
    res = agent_model.system_one(state_of(walls, agent, objs, f"Walk to the {target_name}."), q)
    return res, (time.perf_counter() - t) * 1000


TRUNCATED = []


def answer_of(res, qid):
    TRUNCATED.append(res["usage"]["truncated"])
    return res["answers"][qid]["choice"]


def main():
    n_states = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    n_eps = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    model = laya.load()
    rng = random.Random(7)
    worlds = []
    for _ in range(n_states):
        walls, agent, objs = make_world(rng)
        target = rng.choice([o[1] for o in OBJECTS])
        if objs[target] == agent or not good_moves(walls, agent, objs[target]):
            continue
        worlds.append((walls, agent, objs, target))

    report, lat = {}, []
    # one-step accuracy: is the chosen direction on some shortest path?
    for name, facts in (("A_ascii", False), ("B_facts", True), ("B2_short", "short")):
        hit = 0
        for walls, agent, objs, target in worlds:
            res, ms = ask_move(model, walls, agent, objs, target, facts)
            lat.append(ms)
            hit += answer_of(res, "move") in good_moves(walls, agent, objs[target])
        report[f"{name}_step_acc"] = round(hit / len(worlds), 3)
    report["random_step_acc"] = round(statistics.mean(
        len(good_moves(w, a, objs[t])) / len(legal(w, a)) for w, a, objs, t in worlds), 3)

    # closed loop: walk until on the target, budget = 2 x shortest distance
    for name, facts in (("A_ascii", False), ("B_facts", True), ("B2_short", "short"), ("random", None)):
        ok, eff = 0, []
        erng = random.Random(11)
        for walls, agent, objs, target in worlds[:n_eps]:
            pos, best = agent, bfs(walls, agent, objs[target])
            for t in range(2 * best):
                if facts is None:
                    d = erng.choice(legal(walls, pos))
                else:
                    d = answer_of(ask_move(model, walls, pos, objs, target, facts)[0], "move")
                pos = step(pos, d)
                if pos == objs[target]:
                    ok += 1
                    eff.append(best / (t + 1))
                    break
        report[f"{name}_loop_success"] = f"{ok}/{len(worlds[:n_eps])}"
        report[f"{name}_loop_path_eff"] = round(statistics.mean(eff), 3) if eff else 0.0

    # C: semantic target choice from a stimulus, each stimulus on 6 different maps
    hit, n, probs = 0, 0, []
    for stim, gold in STIMULI.items():
        for walls, agent, objs, _ in worlds[:6]:
            q = {"target": {"type": "choice", "instructions": "Which object should the NPC walk to?",
                            "criteria": {n_: d for _, n_, d in OBJECTS}}}
            res = model.system_one(state_of(walls, agent, objs, stim), q)
            pick = answer_of(res, "target")
            hit, n = hit + (pick == gold), n + 1
            probs.append(res["answers"]["target"]["probabilities"][gold])
            if pick != gold:
                report.setdefault("C_misses", []).append({"stimulus": stim, "pick": pick})
    report["C_target_acc"] = f"{hit}/{n}"
    report["C_gold_prob_mean"] = round(statistics.mean(probs), 3)
    report["n_states"] = len(worlds)
    report["truncated_calls"] = f"{sum(TRUNCATED)}/{len(TRUNCATED)}"
    report["latency_ms_p50"] = round(statistics.median(lat), 1)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
