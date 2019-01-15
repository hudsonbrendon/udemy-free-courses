from django.test import TestCase

from courses.models import Course
from courses.factories import CourseFactory


class CourseTestCase(TestCase):

    def test_create_course(self):
        course = CourseFactory()
        self.assertIsInstance(course, Course)   
        self.assertEquals(course.title, course.__str__())