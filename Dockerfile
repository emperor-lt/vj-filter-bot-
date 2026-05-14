# Don't Remove Credit @SUPREME_BOTz
# Subscribe YouTube Channel For Amazing Bot @SUPREME_BOTz
# Ask Doubt on telegram @SUPREME_BOTz

FROM python:3.11-slim

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /SUPREME-BOTz
WORKDIR /SUPREME-BOTz
COPY . /SUPREME-BOTz
CMD ["python", "bot.py"]
