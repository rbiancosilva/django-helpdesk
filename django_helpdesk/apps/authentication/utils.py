from django_helpdesk.apps.user_profile.models import Profile
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login


def register_check_form(username: str, email: str, role: str, password1: str, password2: str):

    if User.objects.filter(username=username).exists():
        raise Exception("Username already taken.")
    
    if User.objects.filter(email=email).exists():
        raise Exception("Email already taken.")
    
    if password1 != password2:
        raise Exception("Passwords do not match.")
    
    new_user = User.objects.create_user(username=username, email=email, password=password1)
    new_user_profile = Profile.objects.create(user=new_user)

    

    if role == "USR":
        group = Group.objects.get(name='user')
        group.user_set.add(new_user)
        new_user_profile.role = 'user'
    else:
        group = Group.objects.get(name='operator')
        group.user_set.add(new_user)
        new_user_profile.role = 'operator'

    new_user.save()
    new_user_profile.save()
    group.save()

    return True

def login_check_form(email: str, password: str):
    
    if not User.objects.filter(email=email).exists():
        raise Exception("Email not registered")

    user = User.objects.get(email=email)
    user_auth = authenticate(username=user.username, password=password)

    if user_auth is None:
        raise Exception("Password incorrect")

    return user_auth
    
    
    

    



