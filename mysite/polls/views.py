from django.http import HttpResponse

def index(requst):
    return HttpResponse("hello world ,you are at the polls index.")

