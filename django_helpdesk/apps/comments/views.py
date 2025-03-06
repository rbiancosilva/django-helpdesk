from django import forms
from .models import Comment
from django.shortcuts import redirect
from django_helpdesk.apps.posts.models import Post
from django_helpdesk.apps.notifications.models import Notification 
from django.contrib.auth.decorators import login_required

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-textarea'}))

@login_required(login_url='login_authentication')
def new_comments(request, post_id):
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            post = Post.objects.get(pk=post_id)

            new_comment = Comment.objects.create(user=user,
                                                 post=post,
                                                 content=content,
                                                 user_name=str(user.username))
            
            new_comment.save()

            if user.profile.role == "operator":
                notify_user = post.created_by
            else:
                notify_user = post.responsible

            new_notification = Notification.objects.create(title="New comment on post",
                                                           content=f'/posts/details/{post_id}/',
                                                           sent_to=notify_user)

            return redirect(f'/posts/details/{post_id}/')

    return redirect(f'/posts/details/{post_id}/')

