# main.py
from typing import Optional
from fastapi import FastAPI, Path

import random

app = FastAPI()

@app.get("/roll/{number}")
async def roll(
    number: int = Path(..., title="Number of dices to return")
):
    dice = []
    for i in range(number):    
       dice.append(random.randint(1, 6))
        
    return {'dice':dice}

app.mount("/api/v1", app)