# pastePyAPI
API that looks for pastes on pastebin

## How to use

The simplest way is to deploy it locally with `fastapi dev main.py` command. After deploying we can send requests with topics that we want to find. Example:

```bash
curl 127.0.0.1:8000/search?q=eminem
```

## Issues

This script does not automatically changes your cookies. You need to have an account on pastebin to search your phrases and add your cookies to files specified in `main.py`
