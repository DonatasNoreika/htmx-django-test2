from django.shortcuts import render
from .models import Contact

def contacts(request):
    context = {
        'contacts': Contact.objects.all().order_by('-pk')
    }
    return render(request, template_name="contacts.html", context=context)