FROM registry.access.redhat.com/ubi9/python-311

# Add application sources with correct permissions for OpenShift
USER 0
ADD streamlit .
RUN chown -R 1001:0 ./
USER 1001

# Install the dependencies
RUN pip install -U "pip>=22.2.2" && \
    pip install -r requirements.txt

# Run the application
CMD streamlit run app.py --server.port 8080
