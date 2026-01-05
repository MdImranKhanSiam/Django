from django.http import HttpResponse
from django.template import loader
from .models import Member

def members_func(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('imran.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details_func(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
