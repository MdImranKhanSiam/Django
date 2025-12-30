from django.http import HttpResponse
from django.template import loader

def members_func(request):
    template = loader.get_template('imran.html')
    return HttpResponse(template.render())