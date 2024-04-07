FROM python:3.10-slim
WORKDIR /frontend
COPY . /frontend
RUN pip install --no-cache-dir --upgrade -r /frontend/requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]