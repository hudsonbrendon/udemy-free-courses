import uuid

from django.db import models
from django.conf import settings

from core.models import BaseModel


class Course(BaseModel):

    identifier = models.CharField('ID', max_length=100, unique=True)
    title = models.CharField('Published title', max_length=100)
    url = models.CharField('Url', max_length=100)
    image_240x135 = models.URLField('Image 240x135')
    image_480x270 = models.URLField('Image 480x270')

    def __str__(self):
        return self.title

    @property
    def message(self):
        url = '{udemy_url}{url}'.format(udemy_url=settings.UDEMY_URL, url=self.url)
        message = 'New free course available! \n {url}'.format(url=url)
        return message

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
