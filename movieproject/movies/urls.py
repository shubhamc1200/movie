
from django.contrib import admin
from django.urls import path,include
from . import views

app_name="movies"

urlpatterns = [
    path('',views.movie_list,name='list'),
   path('create',views.movie_create,name='create'),
   path('<slug:slug>', views.movie_details,name='details'),
   path('<slug:slug>/comment', views.add_comment_to_movie, name='add_comment_to_movie'),
   path('<slug:slug>/delete', views.movie_delete, name='delete'),
   path('<slug:slug>/update', views.movie_update, name='update'),
]
