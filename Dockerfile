FROM python:3
ADD my_app /
ADD my_app.py /
RUN pip install pymongo
CMD [ "./my_app"  ]
#CMD exec /bin/bash -c "./my_app & trap : TERM INT; sleep infinity & wait"
