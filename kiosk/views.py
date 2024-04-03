from django.http import HttpResponse


def index(request):
    return HttpResponse("키오스크 view")
