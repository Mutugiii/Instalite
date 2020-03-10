from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/<int:profile_id>', views.update_profile, name='updateProfile'),
    path('post/', views.upload_post, name='post'),
    path('post/<int:post_id>', views.specificpost, name='specificpost'),
    path('search/', views.search, name='search'),
    path('profile/<str:user_name>', views.other_profile, name='otherprofile'),
    path('post/comment/<int:post_id>', views.comments, name='comment'),
    path('user/<int:user_id>/follow', views.follow, name='follow'),
    path('user/follow/<int:user_id>', views.follow, name='follow'),
    path('user/unfollow/<int:user_id>', views.unfollow, name='unfollow'),
]