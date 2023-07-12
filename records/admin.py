from django.contrib import admin
from .models import results


class resultsAdmin(admin.ModelAdmin):
    list_display=('project_name','test_name','duration','test_outcome','longrep','created_at','employee_id','employee_name','plat_form','python')
    

admin.site.register(results,resultsAdmin)

