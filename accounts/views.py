from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your account was created successfully. You can now log in.")
        return response


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ("username", "email", "first_name", "last_name", "course")
    template_name = "accounts/profile_form.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self, queryset=None):
        return self.request.user
