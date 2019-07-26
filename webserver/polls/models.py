from datetime import timedelta

from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, IntegerField, Model
from django.utils.timezone import now


class Question(Model):
    text = CharField(max_length=200)
    publication_date = DateTimeField()

    def was_published_recently(self):
        current_time = now()
        return current_time - timedelta(days=1) <= self.publication_date <= current_time

    def __str__(self):
        return self.text


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.text
