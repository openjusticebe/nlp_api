from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Document(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"text": "Welcome to the NLP API of OpenJustice"}

@app.post("/tools/tokenisation")
def tokenisation(doc: Document):
    return {"text": "Tokens"}


@app.post("/tools/sentiment_analysis")
def sentiment_analysis(doc: Document):
#    return {"doc_name": doc.name, "doc_id": doc_id}
    return {"text": "Sentiment analysis"}

