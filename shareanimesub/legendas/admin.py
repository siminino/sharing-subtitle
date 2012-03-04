from django.contrib import admin

from legendas.models import Legenda


class LegendaAdmin(admin.ModelAdmin):
    list_filter = ('projeto',)

admin.site.register(Legenda, LegendaAdmin)
