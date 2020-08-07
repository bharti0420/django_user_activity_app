from rest_framework import serializers
from .models import ActivityPeriod, User

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # activityperiod = ActivityPeriodSerializer(read_only=True)
    activity_period = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = User
        depth = 1
        fields = ('id', 'real_name', 'tz', 'activity_period')