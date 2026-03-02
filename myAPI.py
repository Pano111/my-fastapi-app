from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI() 

class Word(BaseModel):
    data: str

@app.post("/webhook")
def get_word(payload: Word):

    wordOriginal = payload.data

    wordArray = list(wordOriginal)
    wordArray.sort()
    return {
        "word": wordArray    
    }
