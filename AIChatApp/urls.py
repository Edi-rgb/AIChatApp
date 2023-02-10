from django.urls import path,include

from . import views
from .api import routes

urlpatterns = [
    path('', views.front_page, name='FrontPage'),

    # the api routing
    path('api/', include(routes)),
]