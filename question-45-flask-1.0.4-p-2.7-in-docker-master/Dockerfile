FROM python:2.7.11-slim

EXPOSE 8080

ARG workspace="none"

RUN apt-get update \
    && apt-get install --assume-yes wget bash-completion unzip

# Install Workspace for Python 

RUN if [ $workspace = "theia" ] ; then \
	wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/theia/pre-build.sh \
    && chmod 775 ./pre-build.sh && sh pre-build.sh ; fi

WORKDIR /var/

RUN if [ $workspace = "theia" ] ; then \
	wget https://codejudge-starter-repo-artifacts.s3.ap-south-1.amazonaws.com/theia/build.sh \
    && chmod 775 ./build.sh && sh build.sh ; fi

# End Install for Workspace 

RUN mkdir -p /var/app
WORKDIR /var/app

ADD requirements.txt /var/app
RUN pip install -r requirements.txt

ADD . .

CMD python restapi.py