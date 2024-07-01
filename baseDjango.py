print(" I Don't know anything about this code cause it is in the Django which i don't knwo!! ")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")