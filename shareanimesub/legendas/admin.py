from django.contrib import admin

from legendas.models import Legenda


class LegendaAdmin(admin.ModelAdmin):
    list_filter = ('projeto','fansub')
    ordering = ['episodio']
    readonly_fields = ['usuario']

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if not context['adminform'].form.initial:
            context['adminform'].form.instance = Legenda(usuario=request.user)

        return super(LegendaAdmin, self).render_change_form(request, context, add, change, form_url, obj)

    def save_form(self, request, form, change):
        form.instance.usuario = request.user

        return super(LegendaAdmin, self).save_form(request, form, change)

admin.site.register(Legenda, LegendaAdmin)
