from django.contrib import admin


from .models import Snack


class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'purchaser']


admin.site.register(Snack, SnackAdmin)

