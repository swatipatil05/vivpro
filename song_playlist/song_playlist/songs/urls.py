from django.urls import path
from songs import views

urlpatterns = [
    path('', views.home, name="home page"),
    path('populate_data/', views.insert_data, name='Populate All Data'),
    path('songs/', views.song_list),
    path('rate_song/<int:pk>', views.rate_song),
]