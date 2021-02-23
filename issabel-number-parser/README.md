## Number Parser

Very simple service to parse text (spoken) numbers into actual digits.

Docker Run:
```
docker run --name number-parser -d -p8000:8000 issabel/number-parser:latest
```

Example:

```
curl -X POST  'http://127.0.0.1:8000/number' -d 'data=dos mil quinientos treinta y seis'
```

Response:

```
2536
```

Supports English, Spanish, Hindi and Russian
