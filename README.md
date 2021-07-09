# projectjumbo

## Run with frontend

```sh
# checkout submodule from git
git submodule update --init

# setup frontend
cd web
echo "VITE_API_URL=" > .env.local
npm install
npm run build
cd ..

# setup backend
echo "SECRET_KEY=$(openssl rand -hex 32)" > .env
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt

# run server
uvicorn app.main:app --reload
```

## Development

Create `.env` file, and put `SECRET_KEY` in it
```sh
echo "SECRET_KEY=$(openssl rand -hex 32)" > .env
```

Create `venv`, install dependencies and run server
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
python-dotenv
aiofiles
```

## Docker

```
docker build -t fastapi
docker run -p 8000:80 fastapi # app is available at localhost:8000
```

## Origin of files

- [`.gitignore`](https://github.com/github/gitignore/blob/master/Python.gitignore)
- [`.Dockerignore`](https://github.com/GoogleCloudPlatform/getting-started-python/blob/main/optional-kubernetes-engine/.dockerignore)
