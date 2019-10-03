FROM python:3

ADD ranter-bot.py /
ADD helpers.py /

RUN python3 -m pip install -U discord.py
RUN pip install requests

CMD [ "python", "./ranter-bot.py" ]