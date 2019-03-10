from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from .models import Bookmark
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<str:username>/', views.bookmark_user, name = 'marcador_bookmark_user'),
    path('', views.bookmark_list, name='marcador_bookmark_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='marcador/bookmark_list.html'), name="logout"),
    path('create/', views.bookmark_create, name='marcador_bookmark_create'),


]
