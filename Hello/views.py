from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>hello</h1>")
#
#
# def about(request):
#     return HttpResponse("hello about")
from django.shortcuts import render


def index(request):
    # params = {'name': 'Arpan', 'place': 'Nadiad'}
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    print(request.GET.get('text', 'default'))

    return HttpResponse("remove punc")


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse("newline remover")
#
#
# def spaceremover(request):
#     return HttpResponse("space remover")
#
#
# def charcount(request):
#     return HttpResponse("charcount")
