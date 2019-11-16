from django.contrib import admin
from .models import Application, Error


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'token', )


# Skoree vsego udalit
class ErrorAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'app', )


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Error, ErrorAdmin) # Skoree vsego udalit
