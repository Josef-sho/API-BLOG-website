from django.shortcuts import render, get_object_or_404,redirect
from django import forms
from datetime import date
from django.core.validators import URLValidator
from .models import BlogPost
from bson import ObjectId

blog_posts = BlogPost.objects.all()

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.URLInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

    title = forms.CharField(label='Blog Post Title')
    subtitle = forms.CharField(label='Subtitle')
    author = forms.CharField(label='Your Name')
    img_url = forms.URLField(label='Blog Image URL')
    body = forms.CharField(widget=forms.Textarea(), label='Blog Content')
    # submit = forms.SubmitField(label='Submit Post', widget=forms.TextInput(attrs={'class': 'form-control'}))

def get_all_posts(request):
    form = CreatePostForm(request.POST or None) 
    posts = blog_posts
    return render(request, 'templates\index.html', {'form': form,'all_posts':posts})

def show_post(request, post_id):
    requested_post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "post.html", {"post": requested_post})

def post(request):
    form = CreatePostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.date = date.today().strftime('%Y-%m-%d')
        new_post.save()
        return redirect('get_all_posts')

    return render(request, 'make-post.html', {'form': form})

def edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    edit_form = CreatePostForm(request.POST or None, instance=post)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('show_post', post_id=post.id)
    return render(request, 'make-post.html', {'form': edit_form, 'is_edit': True})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    post.save()
    return redirect('get_all_posts')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')