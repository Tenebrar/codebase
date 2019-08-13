from datetime import timedelta
from http import HTTPStatus
from typing import List, Optional

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from webserver.polls.models import Choice, Question

# For use with create_question if the exact number of days does not matter
PAST = -30
FUTURE = 30


def create_question(text: str, days: int) -> Question:
    """
    :param text: question text
    :param days: offset from now (negative for published in the past, positive for yet to be published)
    :return: A Question with the given `text` and published the given number of `days` offset to now
    """
    time = now() + timedelta(days=days)
    return Question.objects.create(text=text, publication_time=time)


def get_content(response: HttpResponse) -> str:
    """ Returns a str version of the content of the response """
    return response.content.decode()


class PollsIndexViewTest(TestCase):
    # UTILS
    INDEX_PATH = reverse('polls:index')

    EXPECTED_INDEX_SIZE = 5
    NO_QUESTIONS_RESPONSE = 'No polls are available.'

    def call_index(self) -> HttpResponse:
        return self.client.get(self.INDEX_PATH)

    def assert_response(self, response: HttpResponse, expected_status_code: Optional[int],
                        expected_content: Optional[str], expected_question_texts: Optional[List[str]]) -> None:
        if expected_status_code is not None:
            assert response.status_code == expected_status_code
        if expected_content is not None:
            assert expected_content in get_content(response)
        if expected_question_texts is not None:
            assert list(map(lambda question: question.text, response.context['questions'])) == expected_question_texts

    # TESTS
    def test_no_questions(self) -> None:
        response = self.client.get(self.INDEX_PATH)

        self.assert_response(response, HTTPStatus.OK, self.NO_QUESTIONS_RESPONSE, [])

    def test_past_question(self) -> None:
        past_question = create_question('Past question.', PAST)

        response = self.call_index()

        self.assert_response(response, HTTPStatus.OK, None, [past_question.text])

    def test_future_question(self) -> None:
        create_question('Future question.', FUTURE)

        response = self.call_index()

        self.assert_response(response, HTTPStatus.OK, self.NO_QUESTIONS_RESPONSE, [])

    def test_future_question_and_past_question(self) -> None:
        past_question = create_question('Past question.', PAST)
        create_question('Future question.', FUTURE)

        response = self.call_index()

        self.assert_response(response, HTTPStatus.OK, None, [past_question.text])

    def test_past_questions_are_sorted(self) -> None:
        past_question1 = create_question('Past question 1.', days=-3)  # Least recent
        past_question2 = create_question('Past question 2.', days=-1)  # Most recent
        past_question3 = create_question('Past question 3.', days=-2)

        response = self.call_index()

        self.assert_response(response, HTTPStatus.OK, None,
                             [past_question2.text, past_question3.text, past_question1.text])

    def test_maximum_questions_shown(self) -> None:
        expected_text = 'Past question.'
        for _ in range(self.EXPECTED_INDEX_SIZE + 2):
            create_question(expected_text, PAST)

        response = self.call_index()

        self.assert_response(response, HTTPStatus.OK, None, [expected_text] * self.EXPECTED_INDEX_SIZE)


class PollsDetailViewTest(TestCase):
    # UTILS
    DETAIL_NAME = 'polls:detail'

    def call_detail(self, question_key: int) -> HttpResponse:
        return self.client.get(reverse(self.DETAIL_NAME, args=(question_key,)))

    def call_vote(self, question_key: int, choice_key: int) -> HttpResponse:
        return self.client.post(reverse(self.DETAIL_NAME, args=(question_key,)), data={'choice': str(choice_key)})

    # TESTS (GET)
    def test_future_question(self):
        future_question = create_question('Future question.', FUTURE)

        response = self.call_detail(future_question.pk)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_no_questions(self):
        response = self.call_detail(1)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_wrong_question(self):
        past_question = create_question('Past Question.', PAST)

        response = self.call_detail(past_question.pk + 1)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_past_question(self):
        past_question = create_question('Past Question.', PAST)

        response = self.call_detail(past_question.pk)

        assert response.status_code == HTTPStatus.OK
        assert past_question.text in get_content(response)
        assert response.context['question'] == past_question

    # TESTS (POST)
    def test_vote_future_question(self):
        future_question = create_question('Future question.', FUTURE)
        choice = Choice.objects.create(question=future_question, text='choice 1')

        response = self.call_vote(future_question.pk, choice.pk)

        assert response.status_code == HTTPStatus.NOT_FOUND

        choice.refresh_from_db()
        assert choice.votes == 0

    def test_vote_no_questions(self):
        response = self.call_vote(1, 2)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_vote_wrong_question(self):
        past_question = create_question('Past Question.', PAST)
        choice = Choice.objects.create(question=past_question, text='choice 1')

        response = self.call_vote(past_question.pk + 1, choice.pk)

        assert response.status_code == HTTPStatus.NOT_FOUND

        choice.refresh_from_db()
        assert choice.votes == 0

    def test_vote_past_question_right_choice(self):
        past_question = create_question('Past Question.', PAST)
        choice = Choice.objects.create(question=past_question, text='choice 1')

        response = self.call_vote(past_question.pk, choice.pk)

        assert response.status_code == HTTPStatus.FOUND
        assert response.url == reverse('polls:results', args=(past_question.pk,))

        choice.refresh_from_db()
        assert choice.votes == 1

    def test_vote_past_question_wrong_choice(self):
        past_question = create_question('Past Question.', PAST)
        choice = Choice.objects.create(question=past_question, text='choice 1')

        response = self.call_vote(past_question.pk, choice.pk + 1)

        assert response.status_code == HTTPStatus.OK
        assert past_question.text in get_content(response)
        assert response.context['question'] == past_question

        choice.refresh_from_db()
        assert choice.votes == 0


class PollsResultsViewTest(TestCase):
    # UTILS
    RESULTS_NAME = 'polls:results'

    def call_results(self, question_key: int) -> HttpResponse:
        return self.client.get(reverse(self.RESULTS_NAME, args=(question_key,)))

    # TESTS
    def test_future_question(self):
        future_question = create_question('Future question.', FUTURE)

        response = self.call_results(future_question.pk)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_no_questions(self):
        response = self.call_results(1)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_wrong_question(self):
        past_question = create_question('Past Question.', PAST)

        response = self.call_results(past_question.pk + 1)

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_past_question(self):
        past_question = create_question('Past Question.', PAST)

        response = self.call_results(past_question.pk)

        assert response.status_code == HTTPStatus.OK
        assert response.context['question'] == past_question
