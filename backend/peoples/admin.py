from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

from peoples.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'branch']
    list_display_links = ['name']
    ordering = ['id']


# register all the models from this app
app_models = apps.get_app_config("peoples").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
