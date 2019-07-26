import datetime

from django.test import TestCase
from django.utils import timezone

from ..models import Question


class QuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        question = Question(publication_date=future_time)

        assert question.was_published_recently() == False
