from fastapi import FastAPI
app=FastAPI()


@app.get("/")
def read():
    return "HII"

@app.get("/add/")
def add(a : float,b: float):
    return "Addition : "+str(a+b) 

@app.get("/sub/")
def sub(a : float,b: float):
    return "Subtraction : "+str(a-b)

@app.get("/div/")
def div(a : float,b: float):
    return "Division : "+str(a/b)

@app.get("/mult/")
def mul(a : float,b: float):
    return "Multiplication : "+str(a*b)









