# Developer:  Alex Scotland <alex@scotland.ca>
ARG WORKER_COUNT

FROM python:3.9.9

WORKDIR /app/

# Update apt-get
RUN apt-get update

# Install dependencies
# RUN apt-get install -y software-properties-common

COPY build/backend/requirements.txt .

RUN pip3 install -r requirements.txt

COPY itemtracker .

# CMD tail -f /dev/null

WORKDIR /app/itemtracker

CMD ["gunicorn", "--workers", $WORKER_COUNT, "--bind", "0.0.0.0:3000", "myproject.wsgi:application"]