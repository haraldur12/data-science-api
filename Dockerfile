FROM python:3.7
COPY . /service
WORKDIR .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]