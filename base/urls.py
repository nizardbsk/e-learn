from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login-page/',views.loginpage,name='login-page'),
    path('create-account/',views.createaccount,name='create-account'),
    path('profile-page/<str:profile_id>/',views.profilepage,name='profile-page'),
    path('logout/',views.logoutpage,name='logout'),
    path('edit-profile/<str:profile_id>/',views.editprofile,name='edit-profile'),
    path('create-tutorial/',views.createtutorial,name='create-tutorial'),
    path('tutorial-page/<str:tutorial_id>/',views.tutorialpage,name='tutorial-page'),
    path('create-video/<str:tutorial_id>/',views.createvideo,name='create-video'),
    path('tutorials/',views.tutorials,name='tutorials'),
]