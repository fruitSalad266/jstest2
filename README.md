# JSTEST API 2
This is an API hosted on [render](https://render.com) built with [FastAPI](https://fastapi.tiangolo.com/).
It is designed to be called by [Reddit Query](https://github.com/fruitsalad266/redditquery)

The service is live at [https://jstest2.render.com](https://jstest2.onrender.com).
Documentation can be found on the [deployed docs](https://jstest2.onrender.com/docs).

## Local Hosting
Clone the repo. Use `pip install -r requirements.txt` for dependencies.

Local hosting requires you go into `server.py` and uncomment the last lines of code.
Then run `python3 server.py` or equivalent alias.

Alternatively, if you have uvicorn, leave the code as-is and run
```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```
The default port is 'localhost:8000'. 

