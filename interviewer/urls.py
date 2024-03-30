from django.urls import path
from .views import *


app_name = 'interviewer'

urlpatterns = [
    path(''         ,HomePageView.as_view(),name='home'),
]