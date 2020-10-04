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
```json
{
    "code": 400,
    "name": "BadRequest",
    "description": "Something went wrong!"
}
```
