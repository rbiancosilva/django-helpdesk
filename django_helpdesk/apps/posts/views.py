from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django_helpdesk.apps.posts.models import Post
from django.views.generic.edit import UpdateView, FormMixin
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django_helpdesk.apps.comments.views import CommentForm
from django_helpdesk.apps.notifications.models import Notification


@login_required(login_url='login_authentication')
@permission_required('posts.add_post', raise_exception=True)
def new_posts(request):
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = request.user
            if 'attachment' in form.files:
                attachment = form.files['attachment']
            else:
                attachment = None 

            new_post = Post.objects.create(title=title, 
                                               content=content, 
                                               attachment=attachment, 
                                               created_by=user,
                                               user_name=str(user.username),
                                               status="new")
            
            new_post.save()

            new_notification = Notification.objects.create(title="New post by you",
                                                           content=f'/posts/details/{new_post.id}/',
                                                           sent_to=new_post.created_by)
            
            new_notification.save()

            return redirect('index_posts')
        
        messages.error(request, "Invalid form. Try again")
        return render(request, 'new_posts.html', {'form': PostForm()})
    
    return render(request, 'new_posts.html', {'form': PostForm()})

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index_posts.html"

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == "user":    
            queryset = Post.objects.filter(created_by=user)
            return queryset
        
        queryset = Post.objects.filter(responsible=user)
        return queryset
    
class AllPostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "index_posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'All posts'

        return context



class PostDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = Post
    context_object_name = "post"
    template_name = "detail_posts.html"
    form_class = CommentForm

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        user = self.request.user
        if user.profile.role == "user":
            if post.created_by != user:
                raise PermissionDenied
            return post
        return post

    


class PostForm(forms.Form):
    title = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-textarea', 'placeholder':'Content'}))
    attachment = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Attachment'}))
    #responsible = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='operator'), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Responsible'}))


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post

    fields = [
        "responsible",
        "status"
    ]


    
    #choosing permissions
    template_name = 'change_posts.html'
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.responsible != self.request.user:
            raise PermissionDenied
        return post

    #used to get the same queryset as in the form used to create the model
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['responsible'].queryset = User.objects.filter(groups__name='operator')
        form.fields['responsible'].widget.attrs.update({'class': 'form-control'})
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        return form

    #used in order to redirect to a view with the pk as argument
    def get_success_url(self):
        new_notification = Notification.objects.create(title="Post assigned to you",
                                    content=f'/posts/details/{self.object.id}/',
                                    sent_to=self.object.responsible)
        
        new_notification.save()
        
        return reverse_lazy('detail_posts', kwargs={'pk': self.object.pk})

    