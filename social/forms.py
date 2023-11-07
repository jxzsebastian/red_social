from accounts.models import Profile
from django import forms
from django.contrib.auth import get_user_model
from .models import SocialComment, SocialPost

class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Say Something...'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        'multiple': True
        }),
        required=False
        )

    class Meta:
        model=SocialPost
        fields=['body']

class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Comment Something...'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']