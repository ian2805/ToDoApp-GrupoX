from task_model import TaskModel

# Crear una tarea
tarea = TaskModel("Estudiar Git con VS Code")
print("Antes de completar:", tarea.is_completed)

# Marcar como completada
tarea.mark_as_complete()
print("Después de completar:", tarea.is_completed)

tarea = TaskModel("Estudiar Git con VS Code")
print("Antes:", getattr(tarea, "is_done", False))

tarea.set_done()
print("Después:", tarea.is_done)
