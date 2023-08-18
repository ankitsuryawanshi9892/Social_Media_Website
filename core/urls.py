from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name= 'signup'),
    path('',views.index, name= "index"),
    path('logout',views.logout,name= 'logout'),
    path('upload',views.upload,name= 'upload'),
    path('search',views.search,name= 'search'),
    path('follow',views.follow,name= 'follow'),
    path('profile/<str:pk>',views.profile,name= 'profile'),
    path('like-post/',views.like_post,name= 'like-post'),
    path('signin',views.signin,name= 'signin'),
    path('settings',views.settings ,name= 'settings')
]