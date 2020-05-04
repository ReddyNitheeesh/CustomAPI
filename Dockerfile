FROM python:3.7-alpine

# expose the app port
EXPOSE 5001

WORKDIR /
copy requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
COPY . /
#ENTRYPOINT [ "python3" ]
#CMD [ "app.py" ]

# run the app server
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "app:app"]
