import datetime
from django.core.management.base import BaseCommand
from labs.models import User, ActivityPeriod
import json
from django.utils import timezone

def format_date(input_date):
    d = datetime.datetime.strptime(input_date, '%b %d %Y %I:%M%p')
    return timezone.make_aware(d, timezone.get_current_timezone())

class Command(BaseCommand):
    help = 'Create user and useraActivity'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as stream:
            user_activities = json.load(stream)
            for activity in user_activities:
                user, created = User.objects.update_or_create(real_name=activity['real_name'])
                user.tz = activity['tz']
                user.save()
                periods = activity['activity_periods']

                for period in periods:
                    act_period = ActivityPeriod.objects.create(user=user, start_time=format_date(period['start_time']), end_time=format_date(period['end_time']))

        self.stdout.write(self.style.SUCCESS('Successfully created user and user activity'))