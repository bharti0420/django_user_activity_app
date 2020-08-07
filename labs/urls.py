from django.urls import path, include
from django.conf.urls import url
from . import views




urlpatterns = [
    path('useractivity/',views.UserDetailList.as_view(), name='user_list'),
	
]
