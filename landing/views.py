from django.contrib import messages
from django.shortcuts import render, redirect

from landing.forms import ContactForm


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has sent successfully")
            return redirect('/#contact')
        else:
            messages.error(request, "Please, retry again")
    else:
        form = ContactForm()
    return render(request, 'landing/home.html', {'form': form})
