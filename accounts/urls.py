from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserProfileView, AddFollower, RemoveFollower, ListFollowers

app_name = "accounts"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),

    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name="add-follower"),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name="remove-follower"),

    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name="followers-list"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)