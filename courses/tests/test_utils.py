import requests_mock

from django.test import TestCase

from courses.models import Course
from courses.factories import CourseFactory
from courses.utils import create_course


class CreateCourseTestCase(TestCase):

    @requests_mock.Mocker()
    def test_create_course(self, request_mock):
        url = 'https://www.udemy.com/api-2.0/courses/?category=Development&ordering=newest&page=1&page_size=1&price=price-free&'
        data = {
            'results': [{
                'id': 10,
                'title': 'Test Course',
                'url': '/test/course/',
                'image_240x135': 'http://image_240x135.com',
                'image_480x270': 'http://image_480x270.com'
            }]
        }
        request_mock.get(url, json=data)

        twitter_url = 'https://api.twitter.com/1.1/statuses/update.json'

        twitter_response_data = {}

        request_mock.post(twitter_url, json=twitter_response_data)

        create_course()

        self.assertEquals(Course.objects.count(), 1)
        self.assertEquals(Course.objects.first().title, 'Test Course')