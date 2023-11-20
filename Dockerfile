FROM registry.access.redhat.com/ubi9/python-311

# Add application sources with correct permissions for OpenShift
USER 0
ADD streamlit .
RUN chown -R 1001:0 ./
USER 1001

# Install the dependencies
RUN pip install -U "pip>=23.3.1" && \
    pip install -r requirements.txt

EXPOSE 8080

# Run the application
ENTRYPOINT ["streamlit",  "run", "app.py", "--server.port=8080"]
