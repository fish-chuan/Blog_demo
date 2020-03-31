from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Artical, Like_Artical
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    data = Artical.objects.all()
    user = str(request.user)
    print(user)
    return render(request, 'index.html', {'data': data})


def post(request, post_id):
    find = Artical.objects.filter(id=post_id)
    check = Like_Artical.objects.filter(post=post_id, user=request.user)
    if len(check) == 0:
        is_like = False
    else:
        is_like = True
    return render(request, 'post.html', {'Arti': find, 'is_like': is_like})

def intro(request):
    return render(request, 'intro.html')

def jump_login(request):
    return redirect('/accounts/login')


def jump_register(request):
    return redirect('/accounts/register')


def jump_logout(request):
    return redirect('/accounts/logout')

def re_post(request):
    return redirect("/postlist")

def postlist(request):
    if request.method == 'POST':
        user = str(request.user)
        target_id = request.POST['post_id']
        num = int(target_id)
        target_arti = Artical.objects.get(id=num)

        target_user = str(target_arti.auth)
        if user == target_user:
            target_arti.delete()
            arti_like = Like_Artical.objects.filter(post=num)
            arti_like.delete()
        return redirect('/postlist')
    else:
        data = Artical.objects.filter(auth=request.user)
        return render(request, 'post_list.html', {'lists': data})

@login_required
def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES['img']
        content = request.POST['content']
        auth = request.POST['author']
        data = Artical.objects.create(title=title, img=img, content=content, auth=auth)
        data.save()
        return redirect('/')
    else:
        return render(request, 'newpost.html')


@login_required
def postlike(request):
    if request.method == 'POST':
        target = request.POST['target']
        find_tar = int(target)
        find = Like_Artical.objects.filter(user=request.user, post=find_tar)
        if len(find) == 0:
            add = Artical.objects.get(id=target)
            add.like += 1
            add.save()
            the_user = str(request.user)
            press = Like_Artical.objects.create(user=the_user, post=target)
            press.save()
            return redirect('/post/'+target)
        else:
            add = Artical.objects.get(id=target)
            add.like -= 1
            add.save()
            find.delete()
            return redirect('/post/'+target)
    else:
        return redirect('/')


@login_required
def about(request):
    info = User.objects.filter(username=request.user)
    return render(request, 'aboutme.html', {'info': info})
