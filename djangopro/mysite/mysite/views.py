#file for the frontend view
from django.http import HttpResponse
def index(reuest):
    return HttpResponse("hello")
