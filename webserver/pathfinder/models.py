from django.db.models import Model


class Character(Model):
    def __init__(self):
        super().__init__()

        self.name = "Jos"
