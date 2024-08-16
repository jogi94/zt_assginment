from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form = form.save()  # Save the user to the database
        return super().form_valid(form)