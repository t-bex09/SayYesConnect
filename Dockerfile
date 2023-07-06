FROM python:3.11

ENV HOME /root
WORKDIR /root

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
CMD /wait && python -u server.py
#CMD [ "python", "./your-daemon-or-script.py" ]