from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import get_object_or_404, render

def members_func(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('member.html')
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

def details_func(request, slug):
    mymember = get_object_or_404(Member, slug=slug)
    context = {
        'mymember': mymember,
    }
    return render(request, 'details.html',context)

def main_func(request):
    context = {

    }

    return render(request, 'main.html', context)

def testing_func(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    ip_address = request.META.get('REMOTE_ADDR', 'Unknown')
    Age = 25
    Users = Member.objects.all().values()
    Name = 'Imran\nKhan'
    Number = '01323401969'
    context = {
        'Name': Name,
        'user_agent': user_agent,
        'ip_address': ip_address,
        'Age': Age,
        'Number': Number,
        'Users': Users,
    }

    return render(request, 'testing.html', context)
