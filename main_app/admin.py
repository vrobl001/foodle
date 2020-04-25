from django.contrib import admin
from .models import Item, Cart, Timeslot, Customer, Volunteer, Store, Photo

admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Volunteer)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Timeslot)
admin.site.register(Photo)
