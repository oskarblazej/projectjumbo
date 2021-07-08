# pseudo database

We decided to use [pysonDB](https://github.com/fredysomy/pysonDB) as a placeholder database. Each `.json` file represents collection in NoSQL database.

## Default user

By default there is provided one user, with username "test" and password "test".

## Models

user:
```js
{
    "id": 198396844763547629,
    "name": "username", // unique
    "password": "hashed-password",
}
```

todo:
```js
{
    "id": 476354762919839684,
    "user": 198396844763547629,
    "done": false,
    "content": "todo text",
}
```
