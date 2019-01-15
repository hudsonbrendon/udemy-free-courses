from django.conf import settings

from courses.models import Course
from courses.utils import create_course

from pyudemy import Udemy
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="create-course-every-1-minute",
    ignore_result=True
)
def create_course():
    udemy = Udemy(settings.UDEMY_CLIENT_ID, settings.UDEMY_CLIENT_SECRET)

    course = udemy.courses(
                page=1, 
                page_size=1, 
                category='Development', 
                price='price-free', 
                ordering='newest'
            )

    kwargs = {
            'identifier': course['results'][0]['id'],
            'title': course['results'][0]['title'],
            'url': course['results'][0]['url'],
            'image_240x135': course['results'][0]['image_240x135'],
            'image_480x270': course['results'][0]['image_480x270']
        }

    course, _ = Course.objects.get_or_create(**kwargs)