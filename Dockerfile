FROM python:3.12
WORKDIR /code
COPY ./requirments_dev.txt /code/requirments_dev.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirments_dev.txt
COPY  . /code/

CMD ["uvicorn", "api_integration:app", "--host", "0.0.0.0", "--port", "8000"]