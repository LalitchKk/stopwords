FROM python:3.10.12-slim-bullseye

WORKDIR /stopWords

COPY ./requirements.txt /stopWords/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /stopWords/requirements.txt

# 
COPY ./app /stopWords/app

ENV PYTHONPATH "${PYTHONPATH}:/stopWords"

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]