from fastapi import FastAPI



app = FastAPI()




@app.get("/")
def home():
    return "home"


@app.post("search_grants")
def grants():
    return "search"


@app.delete("delete")
def delete():
    return ""