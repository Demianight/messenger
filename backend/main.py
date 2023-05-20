from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return 'There is a messanger'
