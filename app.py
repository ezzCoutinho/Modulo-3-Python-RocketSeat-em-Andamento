from flask import Flask, request, jsonify
from models.tasks import Tasks
# __name__ == "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar e Apagar.
# Tarefa

tasks = [] # Vamos salvar os dados aqui.
id_tasks_control = 1 # Deixando ela aqui, para evitar cópias dela, dentro do 
# corpo create_task

@app.route("/tasks", methods = ["POST"])
def create_tasks():
  global id_tasks_control
  data = request.get_json()
  new_task = Tasks(id_tasks_control, data.get("title"), data.get("description"), data.get("completed"))
  id_tasks_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso!"})

@app.route("/tasks", methods = ["GET"])
def get_tasks():
  task_list = []
  for task in tasks:
    task_list.append(task.to_dict())

  output = {
              "tasks": task_list,
              "total_tasks": len(task_list)
            }
  return jsonify(output)

@app.route("/tasks/<int:id>", methods = ["GET"])
def get_task(id):
  task = None
  for item in tasks:
    if item.id == id:
      return jsonify(item.to_dict())
  return jsonify({"message:": "Não foi possível encontrar a atividade"}), 404 

if __name__ == "__main__":
  app.run(debug=True)