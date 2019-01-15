from courses.utils import create_course

from celery.decorators import periodic_task
from celery.task.schedules import crontab


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="create-course-every-1-minute",
    ignore_result=True
)
def create_course_every_1_minute():
    create_course()
    