from flask import Flask

# __name__ == "__main__"
app = Flask(__name__)

@app.route("/") # rota criada.
def hello_world():
  return "Hello World"

@app.route("/about") 
def about():
  return "Sobre"

if __name__ == "__main__":
  app.run(debug=True)