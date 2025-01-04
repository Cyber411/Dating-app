from django.urls import path

from . import views
from django.conf.urls.static import static
 
urlpatterns=[
    path("",views.welcome, name='welcome'),
    path("signup",views.signup, name='signup'),
    path("login",views.login_view, name='login'),
    path("profile",views.profile, name='profile'),
    path("editprofile",views.edit_profile, name='editprofile'),
    path("pick",views.pick, name='pick'),
    path("posts",views.posts, name='posts'),
    path("createpost",views.create_post,name='createpost' ),
    path('viewprofile/<int:author_id>/',views.view_profile, name='viewprofile'),
    path('sendmessage/<int:receiver_id>/',views.send_message, name='sendmessage'),
    path('chatlist',views.chat_list,name='chatlist'),
    path('home', views.home, name='home'),
    path('chat/<int:user_id>/', views.chat_detail, name='chat_detail'),
    path('logout/',views.logout_view, name='logout' ),
        
]


