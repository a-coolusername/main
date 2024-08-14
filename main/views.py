import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.contrib.auth import authenticate, login
from django.contrib import messages


def log_in(request):
    return render(request, 'login.html')


@login_required
def mainpage(request):
    return render(request, 'mainpage.html')


@login_required
def tagview(request):
    tags = TAGinfo.objects.all()
    return render(request, 'ALLTAGS.html', {'tags': tags})


@login_required
def newtag(request):
    return render(request, 'NEWTAG.html')


@login_required
def savetag(request):
    tname = request.POST.get('username')
    tcreated_date = datetime.datetime.now()
    TAGinfo.objects.create(tag_NAME=tname, created_date=tcreated_date, USERID=request.user)
    return redirect('/main/TagView/')


@login_required
def articleview(request):
    articles = ARTICLEinfo.objects.all()
    return render(request, 'ALLARTICLES.html', {'articles': articles})


@login_required
def newarticle(request):
    tag_info = TAGinfo.objects.all()
    return render(request, 'NEWARTICLE.html', {'tags': tag_info})


@login_required
def savearticle(request):
    name = request.POST.get('title')
    # created_date = datetime.datetime.now()     || auto_now_add=True in models
    content = request.POST.get('content')
    image = request.FILES.get('image')
    tags = request.POST.getlist('tagschosen')
    articleinit = ARTICLEinfo.objects.create(title=name, content=content, image=image,
                                             USERID=request.user)

    tag_objects = TAGinfo.objects.filter(id__in=tags)
    articleinit.tags_associated.add(*tag_objects)

    return redirect('/main/ArticleView/')


def auth_user(request):
    print("sudfghj")
    if request.user.is_authenticated:
        return redirect('/main/mainpage/')
    else:
        if request.method == "POST":
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            print("before authoroizing")
            # Authenticate using the custom backend
            user = authenticate(request, username=username, password=password)
            print("after authoroizing")

            if user is not None:
                print("succesful login")
                login(request, user)
                return redirect('/main/mainpage/')
            else:
                print("unsuccesful login")
                messages.error(request, "There was an error logging in. Check your username and password.")
                return redirect('/main/')
        else:
            return render(request, 'login.html', {})


@login_required
def deletetag(request, id):
    tag = get_object_or_404(TAGinfo, id=id)
    tag.delete()
    return redirect('/main/TagView/')


@login_required
def updatetag(request, id):
    tag = get_object_or_404(TAGinfo, id=id)
    return render(request, 'updatetag.html', {'tag': tag})


@login_required
def saveupdatetag(request, id):
    if request.method == 'POST':
        tag = get_object_or_404(TAGinfo, id=id)
        new_tag_name = request.POST.get('newtag')
        if new_tag_name:
            tag.tag_NAME = new_tag_name
            tag.save()
    return redirect('/main/TagView/')


@login_required
def deletearticle(request, id):
    article = get_object_or_404(ARTICLEinfo, id=id)
    article.delete()
    return redirect('/main/ArticleView/')


@login_required
def updatearticle(request, id):
    article = get_object_or_404(ARTICLEinfo, id=id)
    tag = TAGinfo.objects.all()
    return render(request, 'updatearticle.html', {'article': article,'tags': tag})


# # # FFIX views for input article more fields
@login_required
def saveupdatearticle(request, id):
    if request.method == 'POST':
        article = get_object_or_404(ARTICLEinfo, id=id)
        new_article_title = request.POST.get('newarticle')
        new_content = request.POST.get('editor')
        new_image = request.FILES.get('image')
        new_tags = request.POST.getlist('tagschosen')
        if new_article_title:
            article.title = new_article_title
            article.save()
        if new_content:
            article.content = new_content
            article.save()
        if new_image:
            article.image = new_image
            article.save()
        if new_tags:
            article.tags_associated.set(new_tags)
    return redirect('/main/ArticleView/')
