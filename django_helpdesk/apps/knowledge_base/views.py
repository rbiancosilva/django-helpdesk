from django.shortcuts import render, redirect
from .models import Article
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

@login_required(login_url='login_authentication')
@permission_required('knowledge_base.change_article', raise_exception=True)
def new_article_knowledge_base(request):
    if request.method == 'POST':
        
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if 'file_attachment' in form.files:
                file_attachment = form.files['file_attachment']
            else:
                file_attachment = None
            if 'image_attachment' in form.files:
                image_attachment = form.files['image_attachment']
            else:
                image_attachment = None

            new_article = Article.objects.create(title=title,
                                                 content=content,
                                                 image_attachment=image_attachment,
                                                 file_attachment=file_attachment,
                                                 created_by=request.user,
                                                 user_name=str(request.user.username))
            
            new_article.save()
            return redirect(f'/knowledge_base/details/{new_article.id}')
        
        messages.error(request, "Invalid form")
        return render(request, "new_knowledge_base.html", {'form': ArticleForm()})
    
    return render(request, "new_knowledge_base.html", {'form': ArticleForm()})

        

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    template_name = "index_knowledge_base.html"

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == "user":    
            raise PermissionDenied
        queryset = Article.objects.filter(created_by=user)
        return queryset
    
class AllArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = "articles"
    template_name = "index_knowledge_base.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = "article"
    template_name = "details_knowledge_base.html"

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    file_attachment = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': "form-control"}))
    image_attachment = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': "form-control"}))

