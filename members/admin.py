from django.contrib import admin

# Register your models here.
from .models import Members


class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','mobile_no', 'goods', 'address', 'express_no', 'created_time')



admin.site.register(Members, MembersAdmin)
