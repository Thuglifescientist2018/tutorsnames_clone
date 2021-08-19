from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse
# Create your views here.


class Contact(CreateView):
    model = Contact
    fields = "__all__"
    template_name = 'contact.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(Contact, self).get_form(form_class)
        form.fields['name'].widget.attrs = {
            'placeholder': 'Type your Full Name...', }
        form.fields['email'].widget.attrs = {
            'placeholder': 'Type your email/gmail...', }

        return form

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super().form_valid(form)
