# pseudo database

We decided to use [pysonDB](https://github.com/fredysomy/pysonDB) as a placeholder database. Each `.json` file represents collection in NoSQL database.

## Default user

By default there is provided one user, with username "test" and password "test".

## Adding user

```py
password = "new user password"
username = "new user name"

from passlib.hash import bcrypt
from pysondb import db

users = db.getDb("db/users.json")
hashed = bcrypt.hash(password)
users.add({
    "name": username,
    "password": hashed
})
```

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
