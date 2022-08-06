from django.contrib import admin
from project_api.models import Project, Technology


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


class TechnologyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)