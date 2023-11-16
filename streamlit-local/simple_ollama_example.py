from llama_index.llms import Ollama

llm = Ollama(model="zephyr")

resp = llm.complete("Who is Linus Torvalds?")
print(resp)
