from task_model import TaskModel

tarea = TaskModel("Estudiar Git con VS Code")
print("Antes:", getattr(tarea, "is_done", False))

tarea.set_done()
print("Después:", tarea.is_done)
