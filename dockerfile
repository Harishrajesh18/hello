FROM python:latest

WORKDIR /calc

COPY . .

EXPOSE 9000

RUN pip install flask

CMD ["python", "app.py"]