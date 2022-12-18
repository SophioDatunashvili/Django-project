from django.shortcuts import render
from django.http import HttpResponse
from user.forms import UserForm

#
# def userhome(request):
#     return render(request, 'userhome.html')


def userform(request):
    uform = UserForm
    return render(request, 'userform.html', {'uform': uform})

def saveform(request):
    uform = UserForm(request.POST)
    uform.save()
    return HttpResponse('form data saved')



