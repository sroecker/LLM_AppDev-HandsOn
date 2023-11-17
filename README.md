# Introduction

In this workshop we'll learn how to build a simple chatbot that can answer questions based on documents.
We will use streamlit and a local LLM via Ollama.

# Deployment
## Podman

Build the container based on UBI9 Python 3.11:
```
podman build -t linuxbot-app .
```

Since we create the embeddings locally we need to increase shared memory for Pytorch in order to get it running:
```
podmanrun -p 8080:8080 --shm-size=2gb -it linuxbot-app
```

# References

- https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/

