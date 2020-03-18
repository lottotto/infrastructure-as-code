FROM python:3.7.5-slim

# install npm
RUN apt-get update \ 
 && apt-get install  -y --no-install-recommends \
    npm=5.8.0+ds6-4 \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/*

# install aws cdk
RUN npm install -g aws-cdk@1.28.0