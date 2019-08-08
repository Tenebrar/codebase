from datetime import timedelta

from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, IntegerField, Model
from django.utils.timezone import now


class Question(Model):
    text = CharField(max_length=200, default=None, blank=False, null=False)
    publication_time = DateTimeField(default=now, blank=False, null=False)

    def was_published_recently(self) -> bool:
        """ Returns whether the Question was published in the last day (and not in the future) """
        current_time = now()
        return current_time - timedelta(days=1) <= self.publication_time <= current_time
    was_published_recently.admin_order_field = 'publication_time'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self) -> str:
        return str(self.text)


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE, blank=False, null=False)
    text = CharField(max_length=200, default=None, blank=False, null=False)
    votes = IntegerField(default=0, blank=True, null=False)

    def __str__(self) -> str:
        return str(self.text)
