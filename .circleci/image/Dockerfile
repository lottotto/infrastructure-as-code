FROM python:3.7.5-slim

# install npm
RUN apt-get update \ 
 && apt-get install  -y --no-install-recommends \
    npm \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/*

# install aws cdk
RUN npm install -g aws-cdk

CMD ["bash"]