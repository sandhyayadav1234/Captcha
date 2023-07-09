from django.shortcuts import render
from .form import ContactForm
# Create your views here.
def ContactView(request):
    temp_name='app1/contact.html'
    form=ContactForm
    context={'form':form}
    return render(request,temp_name,context)