FROM python:3.12
WORKDIR /frontend
COPY . /frontend
RUN pip install --no-cache-dir --upgrade -r /frontend/requirements.txt
CMD ["streamlit", "run", "main.py"]