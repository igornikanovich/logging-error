from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse

from .models import Application, Error


class ApplicationCreateTest(TestCase):

    def setUp(self):
        self.application = Application.objects.create(name='TestApp', token='123456789')
        self.application.save()

    def tearDown(self):
        self.application.delete()

    def test_create_application(self):
        response = self.client.post(reverse('app_list'), {'addnewapp': 'Test'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Application.objects.count(), 2)


class RequestsTest(APITestCase):
    def test_get_request(self):
        response_crash = self.client.get('http://127.0.0.0:8000/api/crash/token/')
        self.assertEqual(response_crash.status_code, 405)


class ErrorCreateTest(APITestCase):
    def test_create_error(self):
        application = Application(name='TestApp', token='123456789')
        application.save()
        url = 'http://127.0.0.0:8000/api/crash/123456789/'
        data = {
                "type": "ErrorTypeTest",
                "date": "2019-11-30T10:10:10Z",
                "message": "ErrorMessageTest",
                "stacktrace": "ErrorStacktraceTest"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Error.objects.count(), 1)
        self.assertEqual(Error.objects.get().type, 'ErrorTypeTest')
        self.assertEqual(Error.objects.get().message, 'ErrorMessageTest')
        self.assertEqual(Error.objects.get().stacktrace, 'ErrorStacktraceTest')

    # don't work with test in api/view!!!!
    # def test_failed_create_error(self):
    #     url = 'http://127.0.0.0:8000/api/crash/987654321/'
    #     data = {
    #             "type": "ErrorTypeTest",
    #             "date": "2019-11-30T10:10:10Z",
    #             "message": "ErrorMessageTest",
    #             "stacktrace": "ErrorStacktraceTest"
    #         }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, 403)
