import json

class HealthTask:
    def __init__(self, task_id, title, description, clinician_id, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.clinician_id = clinician_id
        self.due_date = due_date

    @staticmethod
    def validate_title(title):
        return len(title.strip()) > 0

    def save(self):
        with open('data/health_tasks.json', 'r+') as f:
            data = json.load(f)
            data[self.task_id] = {
                'title': self.title,
                'description': self.description,
                'clinician_id': self.clinician_id,
                'due_date': self.due_date
            }
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)
