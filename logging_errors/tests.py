from rest_framework.test import APITestCase
from django.test import TestCase, Client
from django.urls import reverse

from .models import Application, Error
from authentication.models import User


class ApplicationCreateTest(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(username='lalala', email="lalala@lala.la", password='lalala', id=1)
        self.client = Client()
        self.logged_in = self.client.login(username='lalala', password='lalala')
        self.application = Application.objects.create(name='TestApp', token='123456', author=self.author)
        self.application.save()

    def tearDown(self):
        self.author.delete()
        self.application.delete()

    def test_create_application(self):
        response = self.client.post(reverse('app_list'), {'addnewapp': 'Test'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.logged_in, True)
        self.assertEqual(Application.objects.count(), 2)


class RequestsTest(APITestCase):
    def test_get_request(self):
        response_crash = self.client.get('http://127.0.0.0:8000/api/crash/token/')
        self.assertEqual(response_crash.status_code, 405)


class ErrorCreateTest(APITestCase):

    def setUp(self):
        self.author = User.objects.create_user(username='lalala', email="lalala@lala.la", password='lalala', id=1)
        self.client = Client()
        self.logged_in = self.client.login(username='lalala', password='lalala')

    def tearDown(self):
        self.author.delete()

    def test_create_error(self):
        application = Application(name='TestApplication', token='123456789', author=self.author)
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
