FROM python:3.9

COPY main.py .

RUN pip install python-dotenv requests

CMD [ "python", "main.py" ]