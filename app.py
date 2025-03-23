from fastapi import FastAPI



app = FastAPI()




@app.get("/")
def home():
    return "45"


@app.post("search_grants")
def grants():
    return "search"