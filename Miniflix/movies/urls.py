from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . models import *

urlpatterns = [

    path('register/', views.register, name="register"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    url(r'^movies', views.movies, name='myMovies'),
    url(r'^movie/(\d+)', views.single_movie, name='oneMovie')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
