"""
budget module models

"""

from django.contrib.auth.models import User
from django.db import models

class Trip(models.Model):
    """
    Trip data model

    """
    created = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=256)
    modified = models.DateTimeField(auto_now=True)
    origin = models.CharField(max_length=256)
    travel_begin = models.DateTimeField(blank=False)
    travel_end = models.DateTimeField(blank=False)
    user = models.ForeignKey(User, to_field='id', related_name='+')

    def __unicode__(self):
        return "%s: %s -> %s %s" % (self.user, self.origin, self.destination, self.travel_begin)

class Budget(models.Model):
    """
    Budget abstract data model

    """
    max_budget = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, to_field='id', related_name='+')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    trip = models.ForeignKey(Trip, to_field='id', related_name='+')

    class Meta:
        abstract = True

class LodgingBudget(Budget):
    """
    Lodging data model; can probably itemize further for different types of lodging

    """
    def __unicode__(self):
        return "%s Lodging Budget: $%d" % (self.trip, self.max_budget)

class TransportationBudget(Budget):
    """
    Transportation data model; can probably itemize further for different types of taxis, rental cars

    """
    def __unicode__(self):
        return "%s Transportation Budget: $%d" % (self.trip, self.max_budget)

class TravelBudget(Budget):
    """
    Travel data model; can probably itemize further for different types of travel (flight, train, etc.)

    """
    def __unicode__(self):
        return "%s Travel Budget: $%d" % (self.trip, self.max_budget)

class UserBudget(models.Model):
    """
    User's trip budget data model

    """
    trip = models.ForeignKey(Trip, to_field='id', related_name='+')
    lodging = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transportation = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    travel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        """
        Override save() to auto-populate the total field

        """
        self.total = sum([self.lodging, self.transportation, self.travel])
        super(UserBudget, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s Travel Budget: $%d" % (self.trip, self.total)
