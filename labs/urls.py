from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from .views import ClientRequestList, UserList, UserDetail
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers


router = DefaultRouter()
router.register(r'activityperiods', views.ActivityPeriodViewSet, basename='activityperiod')


urlpatterns = [
	path('', include(router.urls)),
    path('activity',views.ActivityPeriodList.as_view(), name='activity_list'),
	
]
