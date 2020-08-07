from django.contrib import admin
from .models import User, ActivityPeriod

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class ActivityPeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
