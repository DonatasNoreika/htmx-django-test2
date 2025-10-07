from django.shortcuts import render
from .models import Contact
from django.db.models import Q
from .forms import ContactForm
from django.views.decorators.http import require_http_methods


def contacts(request):
    context = {
        'contacts': Contact.objects.all().order_by('-pk'),
        'form': ContactForm(),
    }
    return render(request, template_name="contacts.html", context=context)


def search(request):
    query = request.GET.get("query", '')
    context = {
        'contacts': Contact.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
    }
    return render(request, template_name="partials/contact_list.html", context=context)


@require_http_methods(['POST'])
def delete_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    context = {
        'contacts': Contact.objects.all().order_by('-pk')
    }
    return render(request, template_name="partials/contact_list.html", context=context)

@require_http_methods(['POST'])
def create_contact(request):
    form = ContactForm(request.POST)
    context = {
        'contacts': Contact.objects.all().order_by('-pk'),
        'form': form,
    }
    if form.is_valid():
        form.save()
        print("Išsaugojo")
        response = render(request, template_name='partials/contact_list.html', context=context)
        response['HX-Trigger'] = 'success'
        return response