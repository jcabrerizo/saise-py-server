# Saise a Scheisse 💩 game

This is the backend app for a dice game I knew at the beginning as saise, a bad mispronunciation of german word Scheisse

## Code

This API uses [FastAPI](https://fastapi.tiangolo.com) written bu [@tiangolo](https://twitter.com/tiangolo) (Sebastián Ramírez).

It's based on the [first steps tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/)

### How to install

Using pipenv:

```bash
pipenv --python 3.9
pipenv shell
pipenv install fastapi uvicorn

uvicorn main:app --reload
```

That should expose the server, try the [dice endpoint](http://127.0.0.1:8000/api/v1/roll/6)
