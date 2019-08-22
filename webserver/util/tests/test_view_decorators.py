from http import HTTPStatus
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import Mock, patch

from django.http import HttpRequest, HttpResponse

from webserver.util.view_decorators import required_get_parameters, template_view


class TemplateViewTest(TestCase):
    VIEW_NAME = 'polls/detail.html'
    CONTEXT = {'a': 'a'}
    PARAMETER1_EXPECTED_VALUE = 'test1'
    PARAMETER2_EXPECTED_VALUE = 'test2'

    def test_template_view(self) -> None:
        @template_view(self.VIEW_NAME)
        def mock_template_view() -> Dict[str, Any]:
            return self.CONTEXT

        request = Mock()
        response = Mock()

        with patch('webserver.util.view_decorators.render', return_value=response) as render_patch:
            result = mock_template_view(request)

        assert result is response
        render_patch.assert_called_once_with(request, self.VIEW_NAME, self.CONTEXT)

    def test_template_view_parameters(self) -> None:
        @template_view(self.VIEW_NAME)
        def mock_template_view_with_parameters(*, parameter1: str, parameter2: str) -> Dict[str, Any]:
            assert parameter1 == self.PARAMETER1_EXPECTED_VALUE
            assert parameter2 == self.PARAMETER2_EXPECTED_VALUE
            return self.CONTEXT

        request = Mock(GET = {
            'parameter1': self.PARAMETER1_EXPECTED_VALUE,
            'parameter2': self.PARAMETER2_EXPECTED_VALUE,
        })
        response = Mock()

        with patch('webserver.util.view_decorators.render', return_value=response) as render_patch:
            result = mock_template_view_with_parameters(request,
                                                        # Order should not matter as they have to be passed as keyword
                                                        parameter2=self.PARAMETER2_EXPECTED_VALUE,
                                                        parameter1=self.PARAMETER1_EXPECTED_VALUE)

        assert result is response
        render_patch.assert_called_once_with(request, self.VIEW_NAME, self.CONTEXT)


class RequiredGetParametersTest(TestCase):
    PARAMETER1_NAME = 'parameter1'
    PARAMETER1_EXPECTED_VALUE = 'test1'

    def test_required_get_parameters_missing(self) -> None:
        request = Mock(GET={})

        @required_get_parameters(self.PARAMETER1_NAME)
        def mock_get_view(request_param: HttpRequest, *, parameter1: str) -> HttpResponse:
            assert request_param is request
            assert parameter1 == RequiredGetParametersTest.PARAMETER1_EXPECTED_VALUE
            return HttpResponse('success')

        response = mock_get_view(request)

        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_required_get_parameters_present(self) -> None:
        request = Mock(GET={self.PARAMETER1_NAME: self.PARAMETER1_EXPECTED_VALUE})

        @required_get_parameters(self.PARAMETER1_NAME)
        def mock_get_view(request_param: HttpRequest, *, parameter1: str) -> HttpResponse:
            assert request_param is request
            assert parameter1 == RequiredGetParametersTest.PARAMETER1_EXPECTED_VALUE
            return HttpResponse('success')

        response = mock_get_view(request)

        assert response.status_code == HTTPStatus.OK

    def test_required_get_parameters_logging(self) -> None:
        request = Mock(GET={})

        with self.assertLogs() as cm:
            @required_get_parameters(self.PARAMETER1_NAME)
            def mock_get_view(request_param: HttpRequest, *, parameter1: str) -> HttpResponse:
                assert request_param is request
                assert parameter1 == RequiredGetParametersTest.PARAMETER1_EXPECTED_VALUE
                return HttpResponse('success')

            response = mock_get_view(request)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert len(cm.output) == 1
        assert cm.output[0].startswith('WARNING:webserver.util.view_decorators:No parameter1 in call to ')
        assert cm.output[0].endswith(' with parameters {}')

    def test_required_get_parameters_logging_to_param(self) -> None:
        request = Mock(GET={})
        logs = []

        @required_get_parameters(self.PARAMETER1_NAME, logging_function=logs.append)
        def mock_get_view(request_param: HttpRequest, *, parameter1: str) -> HttpResponse:
            assert request_param is request
            assert parameter1 == RequiredGetParametersTest.PARAMETER1_EXPECTED_VALUE
            return HttpResponse('success')

        response = mock_get_view(request)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert len(logs) == 1
        assert logs[0].startswith('No parameter1 in call to ')
        assert logs[0].endswith(' with parameters {}')
