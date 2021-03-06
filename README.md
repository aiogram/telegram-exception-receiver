# Telegram Exception Receiver
Receive and store actual Telegram exceptions

## Json Schema
```json
{
    "title": "TelegramException",
    "type": "object",
    "properties": {
        "code": {"title": "Code", "type": "integer"},
        "name": {"title": "Name", "type": "string"},
        "description": {"title": "Description", "type": "string"},
        "required": ["code", "name", "description"]
    }
}
```

## Post Json Example
To post an exception send POST request with json object to `http://{host}/exception` path.
E.g:
```json
{
    "code": 400,
    "name": "BadRequest",
    "description": "Something went wrong!"
}
```
Also you can send a list of objects. E.g:
```json
[
    {
        "code": 400,
        "name": "BadRequest",
        "description": "Something went wrong!"
    },
    {
        "code": 401,
        "name": "AnotherBadRequest",
        "description": "Something went wrong again!"
    }
]
```


## Get exceptions
To get all stored exceptions send GET request to `http://{host}/exception` path.
Method will return a JSON with a list of exception objects.
