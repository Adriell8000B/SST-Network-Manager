FROM ubuntu:latest

RUN apt-get update && \
		apt-get upgrade -y && \
		apt-get install -y python3 python3-pip python3-venv

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m venv $VIRTUAL_ENV

COPY requirements.txt ./
COPY requirements.in ./

COPY prisma ./prisma
RUN MONGODB_URI="mongodb://placeholder:27017/db" \ 
		pip install --no-cache-dir -r requirements.txt && \
		prisma generate

COPY . .

CMD [ "gunicorn", "-w", "1", "main:flask" ]