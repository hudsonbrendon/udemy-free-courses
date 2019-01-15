from factory import DjangoModelFactory, Faker

from courses.models import Course


class CourseFactory(DjangoModelFactory):

    class Meta:
        model = Course

    identifier = '10'
    title = 'Course Test'
    url = '/course/test/'
    image_240x135 = 'http://image_240x135.com'
    image_480x270 = 'http://image_480x270.com'
