from django.shortcuts import render
from .models import ActivityPeriod, User
from .serializers import ActivityPeriodSerializer, UserSerializer
from rest_framework import  viewsets, permissions, generics
import json

# Create your views here.

'''
    format_date function will convert datetime into human redailble form like 'Aug 07 2020 01:20PM'
'''
def format_date(input_date):
    return input_date.strftime("%b %d %Y %I:%M%p")


'''
    get_activity finction is for getting all activity of a user from ActivityPeriod model based on user id.
'''
def get_activity(id):
    data = ActivityPeriod.objects.filter(user=id)
    final_data = []
    for i in data:
        one_instace = {}
        one_instace["start_time"] = str(format_date(i.start_time))
        one_instace["end_time"] = str(format_date(i.end_time))
        final_data.append(one_instace)
    return final_data


class UserDetailList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_obj = User.objects.all()
        
        user_activity_data = []
        for i in user_obj:
            one_instance = {
                "id" : str(i.id),
                "real_name" : str(i.real_name),
                "tz" : str(i.tz),
                "activity_period" : get_activity(i.id)
            }
            user_activity_data.append(one_instance)
        
        return user_activity_data 
