from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def startup():
    return '<h1>Loaded</h1>'

if __name__=="__main__":
    app.run(debug=True)