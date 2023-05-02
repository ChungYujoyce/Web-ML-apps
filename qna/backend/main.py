from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gunicorn
from roberta import nlp_qna
import numpy as np

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/answer/{context}/{question}")
def answer(context, question):

    print("Context: {}\nQuestion: {}\n".format(context, question))

    result = nlp_qna(context, question)

    if not result:
        raise HTTPException(status_code=400)

    return result