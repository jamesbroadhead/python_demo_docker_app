FROM python:3
ADD my_app.py /
RUN pip install pymongo
CMD [ "python", "./my_app.py" ]


