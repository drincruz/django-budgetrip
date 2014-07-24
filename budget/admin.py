
from budget.models import (
        LodgingBudget, TransportationBudget,
        TravelBudget, Trip,
    )

from django.contrib import admin

admin.site.register(LodgingBudget)
admin.site.register(TransportationBudget)
admin.site.register(TravelBudget)
admin.site.register(Trip)
