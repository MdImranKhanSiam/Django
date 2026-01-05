from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import get_object_or_404, render

def members_func(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('imran.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# def details_func(request, id):
#     mymember = Member.objects.get(id=id)
#     template = loader.get_template('details.html')
#     context = {
#         'mymember': mymember,
#     }
#     return HttpResponse(template.render(context, request))

def details_func(request, id):
    mymember = get_object_or_404(Member, id=id)
    context = {
        'mymember': mymember,
    }
    return render(request, 'details.html',context)
