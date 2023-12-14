FROM python:3.10
RUN apt update && apt upgrade -y
RUN apt install git -y
RUN  pip install --upgrade pip

RUN pip install ffmpeg
RUN pip install openai==0.28
RUN pip install spotipy
RUN pip install yt_dlp
RUN pip install spotdl
RUN pip instalL pafy
RUN pip install pytube 
RUN pip install youtube-search


COPY requirements.txt /requirements.txt

RUN cd /
RUN pip install -U pip && pip install -U -r requirements.txt
WORKDIR /app

COPY . .
CMD ["python3", "bot.py"]
