from fastapi import FastAPI

app = FastAPI() #instance



@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/about')
def about():
    return {'data': {'about': 'This is the information of the application'}}

@app.get('/blog/{id}')
def show(id):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id
    return {'data': {'comments':{'Some comments'}}}

