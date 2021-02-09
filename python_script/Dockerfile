FROM python:3.7
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# CMD ["python", "./main.py"]
ENTRYPOINT ["python", "./main.py"]

# CMD ["sh", "-C", "python ./main.py"]
