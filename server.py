from flask import Flask, render_template, redirect, request
app=Flask(__name__)

@app.route('/')
def index():
    return "HEllo World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<flask>')
def say(flask):
    if flask=='flask':
        return "Hi Flask"
    if flask=='michael':
        return "Hi Michael"
    if flask=='john':
        return "Hi John"
    return "Bye"

@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    return word*int(num)

if __name__ == '__main__':
    app.run(debug=True)
    
