from django.shortcuts import render
from .models import ActivityPeriod, User
from .serializers import ActivityPeriodSerializer, UserSerializer
from rest_framework import mixins, viewsets, permissions, generics
import json

# Create your views here.

class ActivityPeriodViewSet( 
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    serializer_class = ActivityPeriodSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ActivityPeriod.objects.all()


class ActivityPeriodList(generics.ListAPIView):
    serializer_class = ActivityPeriodSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return ActivityPeriod.objects.all()

def format_date(input_date):
    return input_date.strftime("%b %d %Y %I:%M%p")

def getActivity(id):

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
                "activity_period" : getActivity(i.id)
            }
            user_activity_data.append(one_instance)
        final_user_activity = {
            "ok": True,
            "members": user_activity_data
        }
        return user_activity_data # uj change ho gaya mera ab dekho k

# ocnfirmed vahi issue hai serializer ka suno to dekho kaise krte hai custom sendya fir extra attribute
# yahi ho na haan 
