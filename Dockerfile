FROM python:3.10-slim

WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0"]
