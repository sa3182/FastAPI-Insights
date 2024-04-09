from fastapi import FastAPI

app = FastAPI() #instance

@app.get('/')
def index():
    return {"message": "Hello"}

@app.get('/about')
def about():
    return {'data': {'about': 'This is the information of the application'}}