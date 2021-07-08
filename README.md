# projectjumbo

## Development

```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Dependencies

```
fastapi
uvicorn
pysondb
passlib[bcrypt]
python-jose[cryptography]
```

## Docker

```
docker build -t fastapi
docker run -p 8000:80 fastapi # app is available at localhost:8000
```

## Origin of files

- [`.gitignore`](https://github.com/github/gitignore/blob/master/Python.gitignore)
- [`.Dockerignore`](https://github.com/GoogleCloudPlatform/getting-started-python/blob/main/optional-kubernetes-engine/.dockerignore)
