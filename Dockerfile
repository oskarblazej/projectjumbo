FROM python:3.9-alpine

EXPOSE 80

WORKDIR /app/
COPY . /app/

# required to build bcrypt and cryptography
# TODO: staged build
RUN apk add --no-cache make gcc musl-dev libffi-dev rust cargo openssl-dev
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]