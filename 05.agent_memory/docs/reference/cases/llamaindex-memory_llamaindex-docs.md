# Memory (LlamaIndex agents)

- 제목: Memory (LlamaIndex agents)
- 발행: LlamaIndex Docs
- 발행일: 상시 갱신
- URL: https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents/memory/
- 수집일: 2026-10-27
- 그룹: 3. 오픈소스 메모리 프레임워크/서비스
- 유형: docs
- 수집 방식: HTML 본문 추출 (trafilatura, 내비게이션·푸터 제거). 요약하지 않은 원문. 이미지·일부 서식은 빠졌을 수 있음.

---

# Memory

## Concept

[Section titled “Concept”](#concept)

Memory is a core component of agentic systems. It allows you to store and retrieve information from the past.

In LlamaIndex, you can typically customize memory by using an existing `BaseMemory` class, or by creating a custom one.

As the agent runs, it will make calls to `memory.put()` to store information, and `memory.get()` to retrieve information.

**NOTE:** The `ChatMemoryBuffer` is deprecated. In a future release, the default will be replaced with the `Memory` class, which is more flexible and allows for more complex memory configurations. Examples in this section will use the `Memory` class. By default, the `ChatMemoryBuffer` is used across the framework, to create a basic buffer of chat history, which gives the agent the last X messages that fit into a token limit. The `Memory` class operates similarly, but is more flexible and allows for more complex memory configurations.

Using the `Memory` class, you can create a memory that has both short-term memory (i.e. a FIFO queue of messages) and optionally long-term memory (i.e. extracting information over time).

### Configuring Memory for an Agent

[Section titled “Configuring Memory for an Agent”](#configuring-memory-for-an-agent)

You can set the memory for an agent by passing it into the `run()` method:

### Managing the Memory Manually

[Section titled “Managing the Memory Manually”](#managing-the-memory-manually)

You can also manage the memory manually by calling `memory.put_messages()` and `memory.get()` directly, and passing in the chat history.

### Retrieving the Latest Memory from an Agent

[Section titled “Retrieving the Latest Memory from an Agent”](#retrieving-the-latest-memory-from-an-agent)

You can get the latest memory from an agent by grabbing it from the agent context:

## Customizing Memory

[Section titled “Customizing Memory”](#customizing-memory)

### Short-Term Memory

[Section titled “Short-Term Memory”](#short-term-memory)

By default, the `Memory` class will store the last X messages that fit into a token limit. You can customize this by passing in `token_limit` and `chat_history_token_ratio` arguments to the `Memory` class.

- `token_limit` (default: 30000): The maximum number of short-term and long-term tokens to store.
- `chat_history_token_ratio` (default: 0.7): The ratio of tokens in the short-term chat history to the total token limit. If the chat history exceeds this ratio, the oldest messages will be flushed into long-term memory (if long-term memory is enabled).
- `token_flush_size` (default: 3000): The number of tokens to flush into long-term memory when the chat history exceeds the token limit.

### Long-Term Memory

[Section titled “Long-Term Memory”](#long-term-memory)

Long-term memory is represented as `Memory Block` objects. These objects receive the messages that are flushed from short-term memory, and optionally process them to extract information. Then when memory is retrieved, the short-term and long-term memories are merged together.

Currently, there are three predefined memory blocks:

- `StaticMemoryBlock`: A memory block that stores a static piece of information.
- `FactExtractionMemoryBlock`: A memory block that extracts facts from the chat history.
- `VectorMemoryBlock`: A memory block that stores and retrieves batches of chat messages from a vector database.

By default, depending on the `insert_method` argument, the memory blocks will be inserted into the system message or the latest user message.

This sounds a bit complicated, but it’s actually quite simple. Let’s look at an example:

Here, we’ve setup three memory blocks:

- `core_info`: A static memory block that stores some core information about the user. The static content can either be a string or a list of `ContentBlock` objects like `TextBlock`, `ImageBlock`, etc. This information will always be inserted into the memory.
- `extracted_info`: An extracted memory block that will extract information from the chat history. Here we’ve passed in the `llm` to use to extract facts from the flushed chat history, and set the `max_facts` to 50. If the number of extracted facts exceeds this limit, the `max_facts` will be automatically summarized and reduced to leave room for new information.
- `vector_memory`: A vector memory block that will store and retrieve batches of chat messages from a vector database. Each batch is a list of the flushed chat messages. Here we’ve passed in the `vector_store` and `embed_model` to use to store and retrieve the chat messages.

You’ll also notice that we’ve set the `priority` for each block. This is used to determine the handling when the memory blocks content (i.e. long-term memory) + short-term memory exceeds the token limit on the `Memory` object.

When memory blocks get too long, they are automatically “truncated”. By default, this just means they are removed from memory until there is room again. This can be customized with subclasses of memory blocks that implement their own truncation logic.

- `priority=0`: This block will always be kept in memory.
- `priority=1, 2, 3, etc`: This determines the order in which memory blocks are truncated when the memory exceeds the token limit, to help the overall short-term memory + long-term memory content be less than or equal to the `token_limit`.

Now, let’s pass these blocks into the `Memory` class:

As the memory is used, the short-term memory will fill up. Once the short-term memory exceeds the `chat_history_token_ratio`, the oldest messages that fit into the `token_flush_size` will be flushed and sent to each memory block for processing.

When memory is retrieved, the short-term and long-term memories are merged together. The `Memory` object will ensure that the short-term memory + long-term memory content is less than or equal to the `token_limit`. If it is longer, the `.truncate()` method will be called on the memory blocks, using the `priority` to determine the truncation order.

Once the memory has collected enough information, we might see something like this from the memory:

Which will print something like this:

Here, the memory was inserted into the system message, with specific sections for each memory block.

## Customizing Memory Blocks

[Section titled “Customizing Memory Blocks”](#customizing-memory-blocks)

While predefined memory blocks are available, you can also create your own custom memory blocks.

Here, we’ve defined a memory block that counts the number of times a user mentions a specific name.

Its truncate method is basic, just returning an empty string.

### Remote Memory

[Section titled “Remote Memory”](#remote-memory)

By default, the `Memory` class is using an in-memory SQLite database. You can plug in any remote database by changing the database URI.

You can customize the table name, and also optionally pass in an async engine directly. This is useful for managing your own connection pool.

### Custom Chat Store

[Section titled “Custom Chat Store”](#custom-chat-store)

If SQLAlchemy isn’t a fit for your infrastructure, implement the `AsyncDBChatStore` interface and pass it as `chat_store`. The SQL-specific arguments (`table_name`, `async_database_uri`, `async_engine`, `db_schema`) are ignored when a `chat_store` is given.

## Memory vs. Workflow Context

[Section titled “Memory vs. Workflow Context”](#memory-vs-workflow-context)

At this point in the documentation, you may have encountered cases where you are using a Workflow and are serializing a `Context` object to save and resume a specific workflow state. The workflow `Context` is a complex object that holds runtime information about the workflow, as well as key/value pairs that are shared across workflow steps.

In comparison, the `Memory` object is a simpler object, holding only `ChatMessage` objects, and optionally a list of `MemoryBlock` objects for long-term memory.

In most practical cases, you will end up using both. If you aren’t customizing the memory, then serializing the `Context` object will be sufficient.

In other cases, like when using `FunctionAgent`, `AgentWorkflow`, or `ReActAgent`, if you customize the memory, then you will want to provide that as a separate runtime argument (especially since beyond the default, the `Memory` object is not serializable).

Lastly, there are cases ([like human-in-the-loop](/python/framework/understanding/agent/human_in_the_loop)) where you will need to provide both the `Context` (to resume the workflow) and the `Memory` (to store the chat history).

## (Deprecated) Memory Types

[Section titled “(Deprecated) Memory Types”](#deprecated-memory-types)

In `llama_index.core.memory`, we offer a few different memory types:

- `ChatMemoryBuffer`: A basic memory buffer that stores the last X messages that fit into a token limit.
- `ChatSummaryMemoryBuffer`: A memory buffer that stores the last X messages that fit into a token limit, and also summarizes the conversation periodically when it gets too long.
- `VectorMemory`: A memory that stores and retrieves chat messages from a vector database. It makes no guarantees about the order of the messages, and returns the most similar messages to the latest user message.
- `SimpleComposableMemory`: A memory that composes multiple memories together. Usually used to combine `VectorMemory` with `ChatMemoryBuffer` or `ChatSummaryMemoryBuffer`.

## Examples

[Section titled “Examples”](#examples)

You can find a few examples of memory in action below:

**NOTE:** Deprecated examples:
