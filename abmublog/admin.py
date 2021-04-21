from django.contrib import admin
from .models import *
admin.site.register(Order),
admin.site.register(Product),
admin.site.register(Customer),
admin.site.register(Profile),
admin.site.register(MakeOrder),
admin.site.register(Suggestion),

# Register your models here.
