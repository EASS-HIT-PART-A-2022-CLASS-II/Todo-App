from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"message":"hello world","method":"GET"}


@app.post("post")
def post_root():
        return {"message":"hello world","method":"POST"}
