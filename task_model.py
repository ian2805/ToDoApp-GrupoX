class TaskModel:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def mark_as_complete(self):
        self.is_completed = True
