from django.contrib import admin
from django.urls import path, include

from users import views as users_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('register/', users_views.register, name="blog-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name="blog-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name="blog-logout"),
    path('profile/<slug:authorname>/', users_views.profile, name='blog-profile'),
    path('profile/', users_views.profile, name='blog-profile'),

    path('updateprofile/',users_views.updateprofile,name='blog-updateprofile')

]


