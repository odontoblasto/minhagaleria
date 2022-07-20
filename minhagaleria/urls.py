from django.urls import path
from .views import AddPhotoGamesView, HomeView,CreateProfilePageView,ShowProfilePageView
from . import views

app_name ='minhagaleria'

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('',HomeView.as_view(),name='home'),
    path('<int:pk>/gallery/', views.gallery, name='gallery'),
    path('gallery_test/', views.gallery_test, name='gallery_test'),
    path('photo/', views.viewPhoto, name='photo'),
    path('<int:pk>/add_photogames/',AddPhotoGamesView.as_view(), name='add_photogames'),
    
    path('<int:pk>/create_user_profile_page/',CreateProfilePageView.as_view(),name='create_user_profile_page'),
    path('<int:pk>/show_user_profile_page/',ShowProfilePageView.as_view(),name='show_user_profile_page'),
]