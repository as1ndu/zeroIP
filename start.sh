#!/bin/bash
nc localhost 56733 < /dev/null; echo $?  # check if port is available
app="flask-app.nym.service1"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}
docker ps  # list docker instances