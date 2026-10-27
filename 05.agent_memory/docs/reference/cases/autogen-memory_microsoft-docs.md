# Memory and RAG (AutoGen AgentChat)

- 제목: Memory and RAG (AutoGen AgentChat)
- 발행: Microsoft AutoGen Docs
- 발행일: 상시 갱신 (stable)
- URL: https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html
- 수집일: 2026-10-27
- 그룹: 3. 오픈소스 메모리 프레임워크/서비스
- 유형: docs
- 수집 방식: HTML 본문 추출 (trafilatura, 내비게이션·푸터 제거). 요약하지 않은 원문. 이미지·일부 서식은 빠졌을 수 있음.

---

# Memory and RAG[#](#memory-and-rag)

There are several use cases where it is valuable to maintain a *store* of useful facts that can be intelligently added to the context of the agent just before a specific step. The typically use case here is a RAG pattern where a query is used to retrieve relevant information from a database that is then added to the agent’s context.

AgentChat provides a [`Memory`](../../reference/python/autogen_core.memory.html#autogen_core.memory.Memory) protocol that can be extended to provide this functionality.  The key methods are `query`, `update_context`,  `add`, `clear`, and `close`.

- `add`: add new entries to the memory store
- `query`: retrieve relevant information from the memory store
- `update_context`: mutate an agent’s internal `model_context` by adding the retrieved information (used in the [`AssistantAgent`](../../reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.AssistantAgent) class)
- `clear`: clear all entries from the memory store
- `close`: clean up any resources used by the memory store

# ListMemory Example[#](#listmemory-example)

[`ListMemory`](../../reference/python/autogen_core.memory.html#autogen_core.memory.ListMemory) is provided as an example implementation of the [`Memory`](../../reference/python/autogen_core.memory.html#autogen_core.memory.Memory) protocol. It is a simple list-based memory implementation that maintains memories in chronological order, appending the most recent memories to the model’s context. The implementation is designed to be straightforward and predictable, making it easy to understand and debug.
In the following example, we will use ListMemory to maintain a memory bank of user preferences and demonstrate how it can be used to provide consistent context for agent responses over time.

```
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.memory import ListMemory, MemoryContent, MemoryMimeType
from autogen_ext.models.openai import OpenAIChatCompletionClient
```
```
# Initialize user memory
user_memory = ListMemory()
# Add user preferences to memory
await user_memory.add(MemoryContent(content="The weather should be in metric units", mime_type=MemoryMimeType.TEXT))
await user_memory.add(MemoryContent(content="Meal recipe must be vegan", mime_type=MemoryMimeType.TEXT))
async def get_weather(city: str, units: str = "imperial") -> str:
    if units == "imperial":
        return f"The weather in {city} is 73 °F and Sunny."
    elif units == "metric":
        return f"The weather in {city} is 23 °C and Sunny."
    else:
        return f"Sorry, I don't know the weather in {city}."
assistant_agent = AssistantAgent(
    name="assistant_agent",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4o-2024-08-06",
    ),
    tools=[get_weather],
    memory=[user_memory],
)
```
```
# Run the agent with a task.
stream = assistant_agent.run_stream(task="What is the weather in New York?")
await Console(stream)
```
```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- MemoryQueryEvent (assistant_agent) ----------
[MemoryContent(content='The weather should be in metric units', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None), MemoryContent(content='Meal recipe must be vegan', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None)]
---------- ToolCallRequestEvent (assistant_agent) ----------
[FunctionCall(id='call_33uMqZO6hwOfEpJavP9GW9LI', arguments='{"city":"New York","units":"metric"}', name='get_weather')]
---------- ToolCallExecutionEvent (assistant_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 23 °C and Sunny.', name='get_weather', call_id='call_33uMqZO6hwOfEpJavP9GW9LI', is_error=False)]
---------- ToolCallSummaryMessage (assistant_agent) ----------
The weather in New York is 23 °C and Sunny.
```
```
TaskResult(messages=[TextMessage(source='user', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 8, 867845, tzinfo=datetime.timezone.utc), content='What is the weather in New York?', type='TextMessage'), MemoryQueryEvent(source='assistant_agent', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 8, 869589, tzinfo=datetime.timezone.utc), content=[MemoryContent(content='The weather should be in metric units', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None), MemoryContent(content='Meal recipe must be vegan', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None)], type='MemoryQueryEvent'), ToolCallRequestEvent(source='assistant_agent', models_usage=RequestUsage(prompt_tokens=123, completion_tokens=19), metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 10, 240626, tzinfo=datetime.timezone.utc), content=[FunctionCall(id='call_33uMqZO6hwOfEpJavP9GW9LI', arguments='{"city":"New York","units":"metric"}', name='get_weather')], type='ToolCallRequestEvent'), ToolCallExecutionEvent(source='assistant_agent', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 10, 242633, tzinfo=datetime.timezone.utc), content=[FunctionExecutionResult(content='The weather in New York is 23 °C and Sunny.', name='get_weather', call_id='call_33uMqZO6hwOfEpJavP9GW9LI', is_error=False)], type='ToolCallExecutionEvent'), ToolCallSummaryMessage(source='assistant_agent', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 10, 243722, tzinfo=datetime.timezone.utc), content='The weather in New York is 23 °C and Sunny.', type='ToolCallSummaryMessage')], stop_reason=None)
```
We can inspect that the `assistant_agent` model\_context is actually updated with the retrieved memory entries.  The `transform` method is used to format the retrieved memory entries into a string that can be used by the agent.  In this case, we simply concatenate the content of each memory entry into a single string.

```
await assistant_agent._model_context.get_messages()
```
```
[UserMessage(content='What is the weather in New York?', source='user', type='UserMessage'),
 SystemMessage(content='\nRelevant memory content (in chronological order):\n1. The weather should be in metric units\n2. Meal recipe must be vegan\n', type='SystemMessage'),
 AssistantMessage(content=[FunctionCall(id='call_33uMqZO6hwOfEpJavP9GW9LI', arguments='{"city":"New York","units":"metric"}', name='get_weather')], thought=None, source='assistant_agent', type='AssistantMessage'),
 FunctionExecutionResultMessage(content=[FunctionExecutionResult(content='The weather in New York is 23 °C and Sunny.', name='get_weather', call_id='call_33uMqZO6hwOfEpJavP9GW9LI', is_error=False)], type='FunctionExecutionResultMessage')]
```
We see above that the weather is returned in Centigrade as stated in the user preferences.

Similarly, assuming we ask a separate question about generating a meal plan, the agent is able to retrieve relevant information from the memory store and provide a personalized (vegan) response.

```
stream = assistant_agent.run_stream(task="Write brief meal recipe with broth")
await Console(stream)
```
```
---------- TextMessage (user) ----------
Write brief meal recipe with broth
---------- MemoryQueryEvent (assistant_agent) ----------
[MemoryContent(content='The weather should be in metric units', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None), MemoryContent(content='Meal recipe must be vegan', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None)]
---------- TextMessage (assistant_agent) ----------
Here's a brief vegan meal recipe using broth:
**Vegan Vegetable Broth Soup**
**Ingredients:**
- 1 tablespoon olive oil
- 1 onion, chopped
- 3 cloves garlic, minced
- 2 carrots, sliced
- 2 celery stalks, sliced
- 1 zucchini, chopped
- 1 cup mushrooms, sliced
- 1 cup kale or spinach, chopped
- 1 can (400g) diced tomatoes
- 4 cups vegetable broth
- 1 teaspoon dried thyme
- Salt and pepper to taste
- Fresh parsley, chopped (for garnish)
**Instructions:**
1. Heat olive oil in a large pot over medium heat. Add the onion and garlic, and sauté until soft.
2. Add the carrots, celery, zucchini, and mushrooms. Cook for about 5 minutes until the vegetables begin to soften.
3. Add the diced tomatoes, vegetable broth, and dried thyme. Bring to a boil.
4. Reduce heat and let it simmer for about 20 minutes, or until the vegetables are tender.
5. Stir in the chopped kale or spinach and cook for another 5 minutes.
6. Season with salt and pepper to taste.
7. Serve hot, garnished with fresh parsley.
Enjoy your comforting vegan vegetable broth soup!
```
```
TaskResult(messages=[TextMessage(source='user', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 10, 256897, tzinfo=datetime.timezone.utc), content='Write brief meal recipe with broth', type='TextMessage'), MemoryQueryEvent(source='assistant_agent', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 10, 258468, tzinfo=datetime.timezone.utc), content=[MemoryContent(content='The weather should be in metric units', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None), MemoryContent(content='Meal recipe must be vegan', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata=None)], type='MemoryQueryEvent'), TextMessage(source='assistant_agent', models_usage=RequestUsage(prompt_tokens=205, completion_tokens=266), metadata={}, created_at=datetime.datetime(2025, 7, 1, 23, 53, 14, 67151, tzinfo=datetime.timezone.utc), content="Here's a brief vegan meal recipe using broth:\n\n**Vegan Vegetable Broth Soup**\n\n**Ingredients:**\n- 1 tablespoon olive oil\n- 1 onion, chopped\n- 3 cloves garlic, minced\n- 2 carrots, sliced\n- 2 celery stalks, sliced\n- 1 zucchini, chopped\n- 1 cup mushrooms, sliced\n- 1 cup kale or spinach, chopped\n- 1 can (400g) diced tomatoes\n- 4 cups vegetable broth\n- 1 teaspoon dried thyme\n- Salt and pepper to taste\n- Fresh parsley, chopped (for garnish)\n\n**Instructions:**\n1. Heat olive oil in a large pot over medium heat. Add the onion and garlic, and sauté until soft.\n2. Add the carrots, celery, zucchini, and mushrooms. Cook for about 5 minutes until the vegetables begin to soften.\n3. Add the diced tomatoes, vegetable broth, and dried thyme. Bring to a boil.\n4. Reduce heat and let it simmer for about 20 minutes, or until the vegetables are tender.\n5. Stir in the chopped kale or spinach and cook for another 5 minutes.\n6. Season with salt and pepper to taste.\n7. Serve hot, garnished with fresh parsley.\n\nEnjoy your comforting vegan vegetable broth soup!", type='TextMessage')], stop_reason=None)
```
# Custom Memory Stores (Vector DBs, etc.)[#](#custom-memory-stores-vector-dbs-etc)

You can build on the `Memory` protocol to implement more complex memory stores. For example, you could implement a custom memory store that uses a vector database to store and retrieve information, or a memory store that uses a machine learning model to generate personalized responses based on the user’s preferences etc.

Specifically, you will need to overload the `add`, `query` and `update_context`  methods to implement the desired functionality and pass the memory store to your agent.

Currently the following example memory stores are available as part of the [`autogen_ext`](../../reference/python/autogen_ext.html#module-autogen_ext) extensions package.

- `autogen_ext.memory.chromadb.ChromaDBVectorMemory`: A memory store that uses a vector database to store and retrieve information.
- `autogen_ext.memory.chromadb.SentenceTransformerEmbeddingFunctionConfig`: A configuration class for the SentenceTransformer embedding function used by the `ChromaDBVectorMemory` store. Note that other embedding functions such as `autogen_ext.memory.openai.OpenAIEmbeddingFunctionConfig` can also be used with the `ChromaDBVectorMemory` store.
- `autogen_ext.memory.redis.RedisMemory`: A memory store that uses a Redis vector database to store and retrieve information.

```
import tempfile
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.memory import MemoryContent, MemoryMimeType
from autogen_ext.memory.chromadb import (
    ChromaDBVectorMemory,
    PersistentChromaDBVectorMemoryConfig,
    SentenceTransformerEmbeddingFunctionConfig,
)
from autogen_ext.models.openai import OpenAIChatCompletionClient
# Use a temporary directory for ChromaDB persistence
with tempfile.TemporaryDirectory() as tmpdir:
    chroma_user_memory = ChromaDBVectorMemory(
        config=PersistentChromaDBVectorMemoryConfig(
            collection_name="preferences",
            persistence_path=tmpdir,  # Use the temp directory here
            k=2,  # Return top k results
            score_threshold=0.4,  # Minimum similarity score
            embedding_function_config=SentenceTransformerEmbeddingFunctionConfig(
                model_name="all-MiniLM-L6-v2"  # Use default model for testing
            ),
        )
    )
    # Add user preferences to memory
    await chroma_user_memory.add(
        MemoryContent(
            content="The weather should be in metric units",
            mime_type=MemoryMimeType.TEXT,
            metadata={"category": "preferences", "type": "units"},
        )
    )
    await chroma_user_memory.add(
        MemoryContent(
            content="Meal recipe must be vegan",
            mime_type=MemoryMimeType.TEXT,
            metadata={"category": "preferences", "type": "dietary"},
        )
    )
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
    )
    # Create assistant agent with ChromaDB memory
    assistant_agent = AssistantAgent(
        name="assistant_agent",
        model_client=model_client,
        tools=[get_weather],
        memory=[chroma_user_memory],
    )
    stream = assistant_agent.run_stream(task="What is the weather in New York?")
    await Console(stream)
    await model_client.close()
    await chroma_user_memory.close()
```
```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- MemoryQueryEvent (assistant_agent) ----------
[MemoryContent(content='The weather should be in metric units', mime_type='MemoryMimeType.TEXT', metadata={'category': 'preferences', 'mime_type': 'MemoryMimeType.TEXT', 'type': 'units', 'score': 0.4342913031578064, 'id': 'b8a70e90-a39f-47ed-ab7b-5a274009d9f0'}), MemoryContent(content='The weather should be in metric units', mime_type='MemoryMimeType.TEXT', metadata={'mime_type': 'MemoryMimeType.TEXT', 'type': 'units', 'category': 'preferences', 'score': 0.4342913031578064, 'id': 'b240f12a-1440-42d1-8f5e-3d8a388363f2'})]
---------- ToolCallRequestEvent (assistant_agent) ----------
[FunctionCall(id='call_YmKqq1nWXgAkAAyXWWk9YpFW', arguments='{"city":"New York","units":"metric"}', name='get_weather')]
---------- ToolCallExecutionEvent (assistant_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 23 °C and Sunny.', name='get_weather', call_id='call_YmKqq1nWXgAkAAyXWWk9YpFW', is_error=False)]
---------- ToolCallSummaryMessage (assistant_agent) ----------
The weather in New York is 23 °C and Sunny.
```
Note that you can also serialize the ChromaDBVectorMemory and save it to disk.

```
chroma_user_memory.dump_component().model_dump_json()
```
```
'{"provider":"autogen_ext.memory.chromadb.ChromaDBVectorMemory","component_type":"memory","version":1,"component_version":1,"description":"Store and retrieve memory using vector similarity search powered by ChromaDB.","label":"ChromaDBVectorMemory","config":{"client_type":"persistent","collection_name":"preferences","distance_metric":"cosine","k":2,"score_threshold":0.4,"allow_reset":false,"tenant":"default_tenant","database":"default_database","persistence_path":"/Users/justin.cechmanek/.chromadb_autogen"}}'
```
## Redis Memory[#](#redis-memory)

You can perform the same persistent memory storage using Redis. Note, you will need to have a running Redis instance to connect to.

See `RedisMemory` for instructions to run Redis locally or via Docker.

```
from logging import WARNING, getLogger
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.memory import MemoryContent, MemoryMimeType
from autogen_ext.memory.redis import RedisMemory, RedisMemoryConfig
from autogen_ext.models.openai import OpenAIChatCompletionClient
logger = getLogger()
logger.setLevel(WARNING)
# Initailize Redis memory
redis_memory = RedisMemory(
    config=RedisMemoryConfig(
        redis_url="redis://localhost:6379",
        index_name="chat_history",
        prefix="memory",
    )
)
# Add user preferences to memory
await redis_memory.add(
    MemoryContent(
        content="The weather should be in metric units",
        mime_type=MemoryMimeType.TEXT,
        metadata={"category": "preferences", "type": "units"},
    )
)
await redis_memory.add(
    MemoryContent(
        content="Meal recipe must be vegan",
        mime_type=MemoryMimeType.TEXT,
        metadata={"category": "preferences", "type": "dietary"},
    )
)
model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
)
# Create assistant agent with ChromaDB memory
assistant_agent = AssistantAgent(
    name="assistant_agent",
    model_client=model_client,
    tools=[get_weather],
    memory=[redis_memory],
)
stream = assistant_agent.run_stream(task="What is the weather in New York?")
await Console(stream)
await model_client.close()
await redis_memory.close()
```
```
---------- TextMessage (user) ----------
What is the weather in New York?
---------- MemoryQueryEvent (assistant_agent) ----------
[MemoryContent(content='The weather should be in metric units', mime_type=<MemoryMimeType.TEXT: 'text/plain'>, metadata={'category': 'preferences', 'type': 'units'})]
---------- ToolCallRequestEvent (assistant_agent) ----------
[FunctionCall(id='call_1R6wV3uDOK8mGK2Vh2t0h4ld', arguments='{"city":"New York","units":"metric"}', name='get_weather')]
---------- ToolCallExecutionEvent (assistant_agent) ----------
[FunctionExecutionResult(content='The weather in New York is 23 °C and Sunny.', name='get_weather', call_id='call_1R6wV3uDOK8mGK2Vh2t0h4ld', is_error=False)]
---------- ToolCallSummaryMessage (assistant_agent) ----------
The weather in New York is 23 °C and Sunny.
```
# RAG Agent: Putting It All Together[#](#rag-agent-putting-it-all-together)

The RAG (Retrieval Augmented Generation) pattern which is common in building AI systems encompasses two distinct phases:

1. **Indexing**: Loading documents, chunking them, and storing them in a vector database
2. **Retrieval**: Finding and using relevant chunks during conversation runtime

In our previous examples, we manually added items to memory and passed them to our agents. In practice, the indexing process is usually automated and based on much larger document sources like product documentation, internal files, or knowledge bases.

Note: The quality of a RAG system is dependent on the quality of the chunking and retrieval process (models, embeddings, etc.). You may need to experiement with more advanced chunking and retrieval models to get the best results.


## Building a Simple RAG Agent[#](#building-a-simple-rag-agent)

To begin, let’s create a simple document indexer that we will used to load documents, chunk them, and store them in a `ChromaDBVectorMemory` memory store.

```
import re
from typing import List
import aiofiles
import aiohttp
from autogen_core.memory import Memory, MemoryContent, MemoryMimeType
class SimpleDocumentIndexer:
    """Basic document indexer for AutoGen Memory."""
    def __init__(self, memory: Memory, chunk_size: int = 1500) -> None:
        self.memory = memory
        self.chunk_size = chunk_size
    async def _fetch_content(self, source: str) -> str:
        """Fetch content from URL or file."""
        if source.startswith(("http://", "https://")):
            async with aiohttp.ClientSession() as session:
                async with session.get(source) as response:
                    return await response.text()
        else:
            async with aiofiles.open(source, "r", encoding="utf-8") as f:
                return await f.read()
    def _strip_html(self, text: str) -> str:
        """Remove HTML tags and normalize whitespace."""
        text = re.sub(r"<[^>]*>", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    def _split_text(self, text: str) -> List[str]:
        """Split text into fixed-size chunks."""
        chunks: list[str] = []
        # Just split text into fixed-size chunks
        for i in range(0, len(text), self.chunk_size):
            chunk = text[i : i + self.chunk_size]
            chunks.append(chunk.strip())
        return chunks
    async def index_documents(self, sources: List[str]) -> int:
        """Index documents into memory."""
        total_chunks = 0
        for source in sources:
            try:
                content = await self._fetch_content(source)
                # Strip HTML if content appears to be HTML
                if "<" in content and ">" in content:
                    content = self._strip_html(content)
                chunks = self._split_text(content)
                for i, chunk in enumerate(chunks):
                    await self.memory.add(
                        MemoryContent(
                            content=chunk, mime_type=MemoryMimeType.TEXT, metadata={"source": source, "chunk_index": i}
                        )
                    )
                total_chunks += len(chunks)
            except Exception as e:
                print(f"Error indexing {source}: {str(e)}")
        return total_chunks
```
Now let’s use our indexer with ChromaDBVectorMemory to build a complete RAG agent:

```
import os
from pathlib import Path
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.memory.chromadb import ChromaDBVectorMemory, PersistentChromaDBVectorMemoryConfig
from autogen_ext.models.openai import OpenAIChatCompletionClient
# Initialize vector memory
rag_memory = ChromaDBVectorMemory(
    config=PersistentChromaDBVectorMemoryConfig(
        collection_name="autogen_docs",
        persistence_path=os.path.join(str(Path.home()), ".chromadb_autogen"),
        k=3,  # Return top 3 results
        score_threshold=0.4,  # Minimum similarity score
    )
)
await rag_memory.clear()  # Clear existing memory
# Index AutoGen documentation
async def index_autogen_docs() -> None:
    indexer = SimpleDocumentIndexer(memory=rag_memory)
    sources = [
        "https://raw.githubusercontent.com/microsoft/autogen/main/README.md",
        "https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/agents.html",
        "https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/teams.html",
        "https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/termination.html",
    ]
    chunks: int = await indexer.index_documents(sources)
    print(f"Indexed {chunks} chunks from {len(sources)} AutoGen documents")
await index_autogen_docs()
```
```
Indexed 70 chunks from 4 AutoGen documents
```
```
# Create our RAG assistant agent
rag_assistant = AssistantAgent(
    name="rag_assistant", model_client=OpenAIChatCompletionClient(model="gpt-4o"), memory=[rag_memory]
)
# Ask questions about AutoGen
stream = rag_assistant.run_stream(task="What is AgentChat?")
await Console(stream)
# Remember to close the memory when done
await rag_memory.close()
```
```
---------- TextMessage (user) ----------
What is AgentChat?
---------- MemoryQueryEvent (rag_assistant) ----------
[MemoryContent(content='e of the AssistantAgent , we can now proceed to the next section to learn about the teams feature in AgentChat. previous Messages next Teams On this page Assistant Agent Getting Result Multi-Modal Input Streaming Messages Using Tools and Workbench Built-in Tools and Workbench Function Tool Model Context Protocol (MCP) Workbench Agent as a Tool Parallel Tool Calls Tool Iterations Structured Output Streaming Tokens Using Model Context Other Preset Agents Next Step Edit on GitHub Show Source so the DOM is not blocked --> © Copyright 2024, Microsoft. Privacy Policy | Consumer Health Privacy Built with the PyData Sphinx Theme 0.16.0.', mime_type='MemoryMimeType.TEXT', metadata={'chunk_index': 16, 'mime_type': 'MemoryMimeType.TEXT', 'source': 'https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/agents.html', 'score': 0.6237251460552216, 'id': '6457da13-1c25-44f0-bea3-158e5c0c5bb4'}), MemoryContent(content='h Literature Review API Reference PyPi Source AgentChat Agents Agents # AutoGen AgentChat provides a set of preset Agents, each with variations in how an agent might respond to messages. All agents share the following attributes and methods: name : The unique name of the agent. description : The description of the agent in text. run : The method that runs the agent given a task as a string or a list of messages, and returns a TaskResult . Agents are expected to be stateful and this method is expected to be called with new messages, not complete history . run_stream : Same as run() but returns an iterator of messages that subclass BaseAgentEvent or BaseChatMessage followed by a TaskResult as the last item. See autogen_agentchat.messages for more information on AgentChat message types. Assistant Agent # AssistantAgent is a built-in agent that uses a language model and has the ability to use tools. Warning AssistantAgent is a “kitchen sink” agent for prototyping and educational purpose – it is very general. Make sure you read the documentation and implementation to understand the design choices. Once you fully understand the design, you may want to implement your own agent. See Custom Agent . from autogen_agentchat.agents import AssistantAgent from autogen_agentchat.messages import StructuredMessage from autogen_agentchat.ui import Console from autogen_ext.models.openai import OpenAIChatCompletionClient # Define a tool that searches the web for information. # For simplicity, we', mime_type='MemoryMimeType.TEXT', metadata={'chunk_index': 1, 'mime_type': 'MemoryMimeType.TEXT', 'source': 'https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/agents.html', 'score': 0.6212755441665649, 'id': 'ab3a553f-bb69-41ff-b6a9-8397b4cb3cb1'}), MemoryContent(content='Literature Review API Reference PyPi Source AgentChat Teams Teams # In this section you’ll learn how to create a multi-agent team (or simply team) using AutoGen. A team is a group of agents that work together to achieve a common goal. We’ll first show you how to create and run a team. We’ll then explain how to observe the team’s behavior, which is crucial for debugging and understanding the team’s performance, and common operations to control the team’s behavior. AgentChat supports several team presets: RoundRobinGroupChat : A team that runs a group chat with participants taking turns in a round-robin fashion (covered on this page). Tutorial SelectorGroupChat : A team that selects the next speaker using a ChatCompletion model after each message. Tutorial MagenticOneGroupChat : A generalist multi-agent system for solving open-ended web and file-based tasks across a variety of domains. Tutorial Swarm : A team that uses HandoffMessage to signal transitions between agents. Tutorial Note When should you use a team? Teams are for complex tasks that require collaboration and diverse expertise. However, they also demand more scaffolding to steer compared to single agents. While AutoGen simplifies the process of working with teams, start with a single agent for simpler tasks, and transition to a multi-agent team when a single agent proves inadequate. Ensure that you have optimized your single agent with the appropriate tools and instructions before moving to a team-based approach. Cre', mime_type='MemoryMimeType.TEXT', metadata={'mime_type': 'MemoryMimeType.TEXT', 'chunk_index': 1, 'source': 'https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/teams.html', 'score': 0.5267025232315063, 'id': '554b20a9-e041-4ac6-b2f1-11261336861c'})]
---------- TextMessage (rag_assistant) ----------
AgentChat is a framework that provides a set of preset agents designed to handle conversations and tasks using a variety of response strategies. It includes features for managing individual agents as well as creating teams of agents that can work collaboratively on complex goals. These agents are stateful, meaning they can manage and track ongoing conversations. AgentChat also includes agents that can utilize tools to enhance their capabilities.
Key features of AgentChat include:
- **Preset Agents**: These agents are pre-configured with specific behavior patterns for handling tasks and messages.
- **Agent Attributes and Methods**: Each agent has a unique name and description, and methods like `run` and `run_stream` to execute tasks and handle messages.
- **AssistantAgent**: A built-in general-purpose agent used primarily for prototyping and educational purposes.
- **Team Configurations**: AgentChat allows for the creation of multi-agent teams for tasks that are too complex for a single agent. Teams run in preset formats like RoundRobinGroupChat or Swarm, providing structured interaction among agents.
Overall, AgentChat is designed for flexible deployment of conversational agents, either singly or in groups, across a variety of tasks. 
TERMINATE
```
This implementation provides a RAG agent that can answer questions based on AutoGen documentation. When a question is asked, the Memory system retrieves relevant chunks and adds them to the context, enabling the assistant to generate informed responses.

For production systems, you might want to:

1. Implement more sophisticated chunking strategies
2. Add metadata filtering capabilities
3. Customize the retrieval scoring
4. Optimize embedding models for your specific domain

# Mem0Memory Example[#](#mem0memory-example)

`autogen_ext.memory.mem0.Mem0Memory` provides integration with `Mem0.ai`’s memory system. It supports both cloud-based and local backends, offering advanced memory capabilities for agents. The implementation handles proper retrieval and context updating, making it suitable for production environments.

In the following example, we’ll demonstrate how to use `Mem0Memory` to maintain persistent memories across conversations:

```
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.memory import MemoryContent, MemoryMimeType
from autogen_ext.memory.mem0 import Mem0Memory
from autogen_ext.models.openai import OpenAIChatCompletionClient
# Initialize Mem0 cloud memory (requires API key)
# For local deployment, use is_cloud=False with appropriate config
mem0_memory = Mem0Memory(
    is_cloud=True,
    limit=5,  # Maximum number of memories to retrieve
)
# Add user preferences to memory
await mem0_memory.add(
    MemoryContent(
        content="The weather should be in metric units",
        mime_type=MemoryMimeType.TEXT,
        metadata={"category": "preferences", "type": "units"},
    )
)
await mem0_memory.add(
    MemoryContent(
        content="Meal recipe must be vegan",
        mime_type=MemoryMimeType.TEXT,
        metadata={"category": "preferences", "type": "dietary"},
    )
)
# Create assistant with mem0 memory
assistant_agent = AssistantAgent(
    name="assistant_agent",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4o-2024-08-06",
    ),
    tools=[get_weather],
    memory=[mem0_memory],
)
# Ask about the weather
stream = assistant_agent.run_stream(task="What are my dietary preferences?")
await Console(stream)
```
The example above demonstrates how Mem0Memory can be used with an assistant agent. The memory integration ensures that:

1. All agent interactions are stored in Mem0 for future reference
2. Relevant memories (like user preferences) are automatically retrieved and added to the context
3. The agent can maintain consistent behavior based on stored memories

Mem0Memory is particularly useful for:

- Long-running agent deployments that need persistent memory
- Applications requiring enhanced privacy controls
- Teams wanting unified memory management across agents
- Use cases needing advanced memory filtering and analytics

Just like ChromaDBVectorMemory, you can serialize Mem0Memory configurations:

```
# Serialize the memory configuration
config_json = mem0_memory.dump_component().model_dump_json()
print(f"Memory config JSON: {config_json[:100]}...")
```
