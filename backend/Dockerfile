FROM python:3.12
WORKDIR /backend
COPY . /backend
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]