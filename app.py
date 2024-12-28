from flask import Flask, request
from models.tasks import Tasks
# __name__ == "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar e Apagar.
# Tarefa

tasks = [] # Vamos salvar os dados aqui.

@app.route("/tasks", methods = ["POST", "GET", "PUT"])
def create_task():
  data = request.get_json()
  print(data)
  return "Test"

if __name__ == "__main__":
  app.run(debug=True)