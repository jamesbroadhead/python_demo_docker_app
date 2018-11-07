FROM python:3
ADD my_app /
ADD my_app.py /
RUN pip install pymongo
CMD [ "python", "my_app.py" ]
#CMD exec /bin/bash -c "./my_app & trap : TERM INT; sleep infinity & wait"
