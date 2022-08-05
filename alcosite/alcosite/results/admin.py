from django.contrib import admin

from .models import Results


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('result',)
    list_display_links = ('result',)


admin.site.register(Results, ResultsAdmin)
