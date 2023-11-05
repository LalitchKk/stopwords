from fastapi import FastAPI, Request

from app.stopWords import getstopWords

app = FastAPI()

@app.get('/api/getStopWords')
async def read_str(request : Request):
        item = await request.json()
        item_str = item['str']
        str = getstopWords(item_str)
        return {str}