FROM python:3.9-slim

WORKDIR /usr/app

COPY ./src .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "src/brain.py"]
