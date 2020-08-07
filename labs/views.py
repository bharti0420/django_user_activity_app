from django.shortcuts import render
from .models import ActivityPeriod
from .serializers import ActivityPeriodSerializer
from rest_framework import mixins, viewsets, permissions, generics

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
