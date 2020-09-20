from django.urls import path, include
from core.views import *

urlpatterns = [

    path('', index, name='home'),
    path('create/', post, name='post'),
    path('resume/', resume, name='resume'),
]
