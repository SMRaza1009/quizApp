from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserResponse)
