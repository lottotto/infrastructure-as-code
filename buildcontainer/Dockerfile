FROM python:3.7.5-slim

ENV AWS_ACCESS_KEY_ID XXXXXXXXXXXXXXXX
ENV AWS_SECRET_ACCESS_KEY XXXXXXXXXXXXXXXXXXXXXXXXXX
ENV AWS_DEFAULT_REGION ap-northeast-1

# install npm
RUN apt-get update \ 
 && apt-get install  -y --no-install-recommends \
    npm \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/*

# install aws cdk
RUN npm install -g aws-cdk

CMD ["bash"]