from django.contrib import admin
from sales.models import *

# Register your models here.
admin.site.register(Category)

admin.site.register(Monitor)
admin.site.register(Brand)
admin.site.register(Proportions)
admin.site.register(Resolution)
admin.site.register(Refresh_Rate)
admin.site.register(Port)

admin.site.register(Cpu)
admin.site.register(Architecture)
admin.site.register(Platform)
admin.site.register(Socket)
admin.site.register(Cores)

admin.site.register(Spec)