from django.contrib import admin
from .models import Customer, Contact, Opportunity, Task

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Opportunity)
admin.site.register(Task)

