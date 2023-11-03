from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from .models import User, Profile
from .forms import EditProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from social.forms import SocialPostForm
from social.models import Image, SocialPost, SocialComment

User = get_user_model()

class UserProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        form = EditProfileForm(instance=profile)
        form_post = SocialPostForm()
        posts = SocialPost.objects.filter(author=user)

        context = {
            'user': user,
            'profile' : profile,
            'form' : form,
            'form_post' : form_post,
            'posts' : posts,
        }
        return render(request, 'users/detail.html', context)
    
    def post(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        user_basic_info = User.objects.get(username=user)
        profile = Profile.objects.get(user=user)
        
        if request.method == 'POST':
            form=EditProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                user_basic_info.first_name = form.cleaned_data.get('first_name')
                user_basic_info.last_name = form.cleaned_data.get('last_name')

                profile.picture = form.cleaned_data.get('picture')
                profile.banner = form.cleaned_data.get('banner')
                profile.location = form.cleaned_data.get('location')
                profile.url = form.cleaned_data.get('url')
                profile.bio = form.cleaned_data.get('bio')

                profile.save()
                user_basic_info.save()
                return redirect('users:profile', username=request.user.username)
            else:
                print(form.errors)  # Esto imprimirá los errores del formulario en la consola
                return HttpResponse("El formulario no es válido. Por favor, corrige los errores e inténtalo de nuevo.")


    
