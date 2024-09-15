from django.shortcuts import render
from .models import Profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "user"
    template_name = "detail_user_profile.html"

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = "users"
    template_name = "list_user_profile.html"

class ProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profile

    fields = [
        "company",
        "job",
        "country",
        "college",
        "profile_picture"
    ]
    
    template_name = 'change_profile.html'
