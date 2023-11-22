# Introduction

In this workshop we'll learn how to build a simple chatbot that can answer questions based on documents.
We will use streamlit, llamaindex and a local LLM via Ollama.

# Setup

Please download ollama from [ollama.ai](https://ollama.ai) and start a server with ``ollama serve``. For the local example have a look at the folder `streamlit` and install the requirements:

```
pip install -r requirements.txt
```

Then start streamlit with:
```
streamlit run app.py
```

Modify the system prompt and copy different data sources to `docs/` in order to create your own version of the chatbot.
You can set the ollama host via the enviroment variable `OLLAMA_HOST`.

You can download models locally with `ollama pull zephyr` or via API:

```
curl -X POST http://ollama:11434/api/pull -d '{"name": "zephyr"}'
```

To test the ollama server you can call the generate API:

```
curl -X POST http://ollama:11434/api/generate -d '{"model": "zephyr", "prompt": "Why is the sky blue?"}'
```

# Deployment
## Podman

Build the container based on [UBI9 Python 3.11](https://catalog.redhat.com/software/containers/ubi9/python-311/63f764b03f0b02a2e2d63fff?architecture=amd64&image=654d1ee47c3bfba06c9c59ea):

```
podman build -t linuxbot-app .
```
If you're building on arm64 Mac and deploy on amd64 don't forget to add `--platform`:

```
podman build --platform="linux/amd64" -t linuxbot-app .
```


Since we create the embeddings locally we need to increase shared memory for Pytorch in order to get it running:

```
podman run -p 8080:8080 --shm-size=2gb -it linuxbot-app
```
NOTE: You need to create a network to access a running ollama container.

## OpenShift

``
oc apply -f deployments/ollama.yaml
``

``
oc apply -f deployments/streamlit.yaml
``

# References

- [Build a chatbot with custom data sources, powered by LlamaIndex](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/)
- [SQL Query Engine with LlamaIndex + DuckDB](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/struct_indices/duckdb_sql_query.html)

