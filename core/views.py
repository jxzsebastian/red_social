from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social.forms import SocialPostForm
from social.models import Image, SocialPost, SocialComment

#LoginRequiredMixin significa que si un usuario no logeado entra a la vista lo mandara al login
class HomeView(LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        #Obtener usuario Logeado
        logged_in_user = request.user
        form = SocialPostForm()
        posts = SocialPost.objects.all()

        context = {
            'form': form,
            'posts': posts,
        }

        return render(request, 'pages/index.html', context)
    
    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = SocialPost.objects.all()


        form = SocialPostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user    
            new_post.save()

            for f in files:
                img = Image(image=f)
                img.save()
                new_post.image.add(img)
                
            new_post.save()

        context = {
            'form': form,
            'posts': posts,
        }

        return redirect('/')
