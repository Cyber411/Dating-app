from urllib import request
from django.shortcuts import render , redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import Profile
from.models import Post
from.models import Message,Like
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q, Max
from django.contrib import messages
from django.views.decorators.http import require_POST

#Time logic
@login_required
def home(request):
  now=datetime.now()
  current_hour=now.hour

  return render(request, 'lovers/home.html',{'morning':current_hour>=4 and current_hour<=11,'afternoon':current_hour>=12 and current_hour<=16,'evening':current_hour >=17 and current_hour<=23})
  


# Create your views here.

def welcome(request):
 return render(request, 'lovers/welcome.html')

def signup(request):
 
 if request.method == "POST":
  username=request.POST.get('username')
  email=request.POST.get('email')
  password1=request.POST.get('password1')
  password2=request.POST.get('password2')
  if password1 == password2:
   password=password1
   user=User.objects.create_user(username=username,email=email,password=password,)
   user.save()
   return render(request,'lovers/login.html')
  
  else:
   return HttpResponse("Fail")

 else:
  return   render(request, 'lovers/signup.html')  
 
def login_view(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=authenticate(request, username=username,password =password)
    if user is not None:

     login(request, user)
     
     return redirect('home')
    else:
      return redirect('login')
    
    
  return render(request,'lovers/login.html')
  
def logout_view(request):
  logout(request) 
  return redirect('login') 






profiles=Profile.objects.all()
 
@login_required 

def profile(request):
 users=User.objects.all()
 
 
 return render(request, 'lovers/profile.html',{'users':users})


@login_required
def edit_profile(request):
 if request.method == 'POST':
  profile_pic=request.FILES.get('profile_pic')
  Course=request.POST.get('bio')

  request.user.profile.profile_pic=profile_pic
  request.user.profile.Course=Course

  request.user.profile.save()
  
  return render(request, 'lovers/profile.html',{'profiles':profiles})
 else:
       
        return render(request, 'lovers/edit_profile.html',{'profiles':profiles}) 


@login_required 
def pick(request):
  
  current_user=request.user
  users=User.objects.exclude(id=current_user.id)
  return render(request, 'lovers/pick.html',{'users':users})


@login_required
def posts(request):
  posts=Post.objects.all()
  return render(request,'lovers/posts.html',{'posts':posts})
    


def create_post(request):
  
  if request.method== 'POST':
    title=request.POST.get('title')
    body=request.POST.get('body')
    author=request.user
    if body:
      p=Post(title=title,body=body,author=author)
      p.save()
    else:
         return redirect('posts')

    
    posts=Post.objects.all()

    return render(request,'lovers/posts.html',{'posts':posts})
  
  return render(request,'lovers/createpost.html')

@login_required
def view_profile(request,author_id):
  person=get_object_or_404(User, id=author_id)
 
  return render(request, 'lovers/viewprofile.html',{'person':person})

@login_required
def send_message(request, receiver_id):

  receiver=get_object_or_404(User, id=receiver_id)
  if request.method== 'POST':

     message=request.POST.get('content')
     if message:
       Message.objects.create(sender=request.user,receiver=receiver,content=message,)
       return redirect('chatlist')

  return render(request, 'lovers/sendmessage.html',{'receiver':receiver})






def chat_list(request):
    user = request.user

    
    conversations = Message.objects.filter(
        Q(sender=user) | Q(receiver=user)
    ).values('sender', 'receiver') .annotate(latest_time=Max('time')).order_by('-latest_time')

    chats = []
    seen_conversations = set() 

    for message in conversations:
        sender_id = message['sender']
        receiver_id = message['receiver']

       
        if (sender_id, receiver_id) not in seen_conversations and (receiver_id, sender_id) not in seen_conversations:
        
            latest_chat = Message.objects.filter(
                Q(sender_id=user, receiver_id=receiver_id) |
                Q(sender_id=sender_id, receiver_id=user)
            ).latest('time') 

            chats.append(latest_chat)
            seen_conversations.add((sender_id, receiver_id)) 

    return render(request, 'lovers/chatlist.html', {'chats': chats})




def chat_detail(request, user_id):
  
    user = request.user

    
    chat_partner = get_object_or_404(User, id=user_id)

    
    conversation = Message.objects.filter(
        Q(sender=user, receiver=chat_partner) | Q(sender=chat_partner, receiver=user)
    ).order_by('time')

   
    return render(request, 'lovers/chatdetail.html', {
        'conversation': conversation,
        'chat_partner': chat_partner
    })
"""@login_required
@require_POST
def like_post(request):
  post_id=request.POST.get('post_id')
  post=get_object_or_404(Post, id=post_id)
  if Like.objects.filter(post=post, liker=request.user).exists():
    Like.objects.filter(post=post, liker=request.user).delete()
  else:
      Like.objects.create(post=post, liker=request.user)
    
  return JsonResponse({'status':'success'})"""
  



