# from django.db import models

from health_monitor.models import Health, HealthTest


class BodyHealth(Health):
    pass


class Heart(HealthTest):
    test = 'heart'
    groups = ['doctor']
    health_model = BodyHealth

    def score(self, heartrate):
        heartrate = int(heartrate)
        if heartrate > 120:
            return 4
        elif heartrate > 100:
            return 3
        elif heartrate > 80:
            return 2
        else:
            return 1


class Sleep(HealthTest):
    test = 'sleep'
    groups = ['doctor']
    health_model = BodyHealth

    def score(self, hours):
        hours = int(hours)
        if hours < 4:
            return 4
        elif hours < 6:
            return 3
        elif hours < 8:
            return 2
        else:
            return 1