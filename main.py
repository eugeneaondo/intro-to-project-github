from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def merge_pr():
    return {"This pr is merged"}


@app.get("/pr/{pr_id}")
def read_pr(pr_id : int):
    return {"pr_id" : pr_id}
