from django.contrib import admin
from .models import employee, party, machine, beam_inward, yarn, wages_report, machine_maintenance_report
from .models import design, party_bill_delivery, machine_operator, bill_details, maintenance_inventory

#registering of models
myModels =[ employee, party, machine, beam_inward, yarn, wages_report, machine_maintenance_report
            , design, party_bill_delivery,  machine_operator, bill_details, maintenance_inventory ]

admin.site.register(myModels)