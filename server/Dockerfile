FROM python:3.9-alpine

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python3", "/app/app.py"]
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
