from django.shortcuts import render
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User 
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "detail_user_profile.html"

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = "profiles"
    template_name = 'all_user_profile.html'

class ProfileUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profile

    fields = [
        "bio",
        "company",
        "job",
        "country",
        "college",
        "profile_picture"
    ]
    
    template_name = 'change_user_profile.html'
    permission_required = 'user_profile.change_profile'

    def get_object(self, queryset=None):
        profile = super().get_object(queryset)
        profile_user = User.objects.get(pk=profile.user.id)
        if profile_user != self.request.user:
            raise PermissionDenied
        return profile
    
    def get_success_url(self):
        return reverse_lazy('details_user_profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['bio'].widget.attrs.update({'class': 'form-control form-textarea'})
        form.fields['company'].widget.attrs.update({'class': 'form-control form-textarea-sm'})
        form.fields['job'].widget.attrs.update({'class': 'form-control form-textarea-sm'})
        form.fields['country'].widget.attrs.update({'class': 'form-control form-textarea-sm'})
        form.fields['college'].widget.attrs.update({'class': 'form-control form-textarea-sm'})
        form.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})
        return form