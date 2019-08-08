from datetime import datetime, timedelta

from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils.timezone import now
from freezegun import freeze_time
from pytest import raises
from pytz import timezone

from webserver.polls.models import Choice, Question
from webserver.settings import TIME_ZONE


class QuestionTest(TestCase):
    def test_text_required(self):
        with raises(IntegrityError):
            Question.objects.create()

    def test_text_set(self):
        question = Question.objects.create(text='test')

        assert question.text == 'test'

    @freeze_time(now())
    def test_publication_time_default(self):
        question = Question.objects.create(text='test')

        assert question.publication_time == now()

    def test_publication_time_set(self):
        publication_time = timezone(TIME_ZONE).localize(datetime(2019, 8, 7, 23, 28, 35))
        question = Question.objects.create(text='test', publication_time=publication_time)

        assert question.publication_time == publication_time

    def test_was_published_recently_with_future_question(self) -> None:
        future_time = now() + timedelta(days=30)
        future_question = Question(publication_time=future_time)

        assert future_question.was_published_recently() is False

    def test_was_published_recently_with_old_question(self) -> None:
        old_time = now() - timedelta(days=1, seconds=1)
        old_question = Question(publication_time=old_time)

        assert old_question.was_published_recently() is False

    @freeze_time(now())
    def test_was_published_recently_with_recent_question(self) -> None:
        recent_time = now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publication_time=recent_time)

        assert recent_question.was_published_recently() is True


class ChoiceTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text='test')

    def test_question_required(self):
        with raises(IntegrityError):
            Choice.objects.create(text='test')

    def test_question_set(self):
        choice = Choice.objects.create(question=self.question, text='test')

        assert choice.question == self.question

    def test_text_required(self):
        with raises(IntegrityError):
            Choice(question=self.question).save()

    def test_text_set(self):
        choice = Choice.objects.create(question=self.question, text='test')

        assert choice.text == 'test'

    def test_votes_default(self):
        choice = Choice.objects.create(question=self.question, text='test')

        assert choice.votes == 0

    def test_question_cascade_delete(self):
        choice = Choice.objects.create(question=self.question, text='test')

        assert Choice.objects.count() == 1

        self.question.delete()

        assert Choice.objects.count() == 0
