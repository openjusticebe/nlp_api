from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Document(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"text": "Welcome to the NLP API of OpenJustice"}

# curl -d '{"text": "prout prout"}' -H "Content-Type: application/json" \
# -X POST http://127.0.0.1:8002/tools/tokenisation
@app.post("/tools/tokenisation")
def tokenisation(data: Document):
    return {
        "text": data.text,
        "tokens": data.text.split()
    }


@app.post("/tools/sentiment_analysis")
def sentiment_analysis(data: Document):
     return {
        "text": data.text,
        "sentiment_analysis": "positive or not"
    }
