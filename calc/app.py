# Put your app in here.
from unittest import result
from flask import Flask,request
from operations import add, sub, mult, div
app=Flask(__name__)
@app.route("/add")
def test_add():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=add(a,b)
    return str(result)


@app.route("/sub")
def test_sub():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    resutl=sub(a,b)
    return str(result)
@app.route("/mult")
def test_mult():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result=mult(a,b)
    return str(result)

@app.route("/div")
def test_div():
    a=int(request.args.get("a"))
    b=int(request.args.get('b'))

    result=div(a,b)
    return str(result)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)