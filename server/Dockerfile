FROM python:3.10.9
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
EXPOSE 8085
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]