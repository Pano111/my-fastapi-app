from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI() 

class Word(BaseModel):
    data: str

@app.post("/webhook")
def get_word(payload: Word):
   
    original_text = payload.data
    
    
    char_list = list(original_text)
    char_list.sort()

    
    return {"word": char_list}
