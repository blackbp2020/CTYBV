
from django.urls import path, URLPattern
from . import views



urlpatterns = [
    path('', views.index, name='index' ),
    path('about', views.about, name='about' ),
    path('service', views.service, name='service' ),
    path('lienhe', views.lienhe, name='lienhe' ),  

    # URL pattern to handle dynamic pages
    path('news', views.news, name='news' ),
    path('newsdetail/<int:pk>/', views.newsdetail, name='newsdetail'),
      
]
