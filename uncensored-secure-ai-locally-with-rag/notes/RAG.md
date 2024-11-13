
# RAG - Retrieval-Augmented Generation

> [Reference](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)

Retrieval-augmented generation (RAG) is a technique for enhancing the accuracy and reliability of generative AI models with facts fetched from external sources. 

Since LLMs are neural networks measured by the number of parameters they contain, and those parameters represent the pattern of how humans use words to form sentences, diving deeper into a specific topic is a task LLM can't do.

RAG gives modes sources they can cite that clarify ambiguity from a user query. That reduces the possibility a model will make a wrong guess (hallucination).

RAG avoids the model's need to retrain it again with additional datasets and lets users hot-swap new sources on the fly by having conversations with data repositories.

## How RAG works

When users ask an LLM a question, the AI model sends the query to another model that converts it into a numeric format so machines can read it. The numeric version of the query is sometimes called an embedding or a vector.

The embedding model then compares these numeric values to vectors in a machine-readable index of an available knowledge base. When it finds a match or multiple matches, it retrieves the related data, converts it to human-readable words and passes it back to the LLM.

Finally, the LLM combines the retrieved words and its own response to the query into a final answer it presents to the user, potentially citing sources the embedding model found.

![NVIDIA RAG](../images/NVIDIA-RAG.jpg "NVIDIA-RAG.jpg")

> Behind the scenes, the sources must be kept up to date by creating and updating indices (vector databases) for new and updated knowledge bases as they become available.
