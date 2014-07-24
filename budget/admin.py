"""
budget module admin UI

"""

from budget.models import (
        LodgingBudget,
        SavingScenario,
        TransportationBudget,
        TravelBudget,
        Trip,
        UserBudget,
    )

from django.contrib import admin

admin.site.register(LodgingBudget)
admin.site.register(SavingScenario)
admin.site.register(TransportationBudget)
admin.site.register(TravelBudget)
admin.site.register(Trip)
admin.site.register(UserBudget)
