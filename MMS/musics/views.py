from django.template import loader
from django.http import HttpResponse
from .models import Music


def musics(request):
    my_musics = Music.objects.all().values()
    template = loader.get_template('all_musics.html')
    context = {
        'my_musics':my_musics,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_musics = Music.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_musics' : my_musics
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'musics':['Good Graces', 'Coincidence', 'Taste']
    }
    return HttpResponse(template.render(context, request))

