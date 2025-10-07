from django.shortcuts import render
from .models import Contact
from django.db.models import Q

def contacts(request):
    context = {
        'contacts': Contact.objects.all().order_by('-pk')
    }
    return render(request, template_name="contacts.html", context=context)


def search(request):
    query = request.GET.get("query", '')
    context = {
        'contacts': Contact.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
    }
    return render(request, template_name="partials/contact_list.html", context=context)