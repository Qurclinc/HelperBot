FROM python3.12:slim

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]