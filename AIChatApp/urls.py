from django.urls import path,include

from . import views
from .api import routes

urlpatterns = [
    path('', views.front_page, name='FrontPage'),
    path('ong', views.ong_page, name='OngPage'),
    path('about_us', views.about_us, name='about_us'),

    # the api routing
    path('api/', include(routes)),
]