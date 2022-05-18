from django.shortcuts import render
from .form import ContactForm

def profile(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'store/suceess.html')
    form = ContactForm()
    cart = {'form': form}
    return render(request,'store/index.html',cart)

