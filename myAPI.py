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
    wordFinal = "".join(wordArray)

    return {
         "status": "success",
        "original": wordOriginal,
        "processed_word": wordFinal    
    }
