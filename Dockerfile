FROM python:3
ADD calculator.py /
RUN pip install pystrich
CMD [ "python", "./calculator.py" ]