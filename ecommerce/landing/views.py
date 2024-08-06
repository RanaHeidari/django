
from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from . import form


def landing(request):
        form1 = form.landingForm()

        return render(request, 'index.html', context={ 'form1':form1 })

def SendMessage(request):
        if request.method == 'POST':
                name = request.POST.get('name')
                email = request.POST.get('email')
                PhoneNumber = request.POST.get('PhoneNumber')
                message = request.POST.get('message')
                instance = models.message.objects.create(name=name, email=email,
                                  PhoneNumber=PhoneNumber, message=message)
                instance.save()
                messages.success(request, 'پیام شما موفقیت آمیز ثبت شد ')
                return redirect('landing')
        else:
                messages.success(request, 'اشکالی پیش امد ')
                return redirect('landing')
