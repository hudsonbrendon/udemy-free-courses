from django.http import HttpResponse

from courses.utils import create_course


def index(request):
    create_course()
    return HttpResponse()