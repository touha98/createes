from django.contrib import admin
from .models import Agent


class agentAdmin(admin.ModelAdmin):
    list_display = ('id', "__str__", 'location', 'phone')
    list_display_links = ('id', "__str__")
    list_search = ('__str__', "location")
    list_per_page = 10


admin.site.register(Agent, agentAdmin)
