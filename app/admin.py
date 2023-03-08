from django.contrib import admin
from django.utils.safestring import mark_safe
from app.models import  Lab,Gorevli, Log, Sorumlu

# Register your models here.
class LabAdmin(admin.ModelAdmin):
    list_display=("isim","labgorevli")
    
    def labgorevli(self,obj):
        html="<ul>"
        for gorevli in obj.gorevli.all():
            html+="<li>"+str(gorevli.first_name)+" "+str(gorevli.last_name)+"</li>"
        html+="</ul>"
        return mark_safe(html)
    
class GorevliAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email",)
    
    

admin.site.register(Lab,LabAdmin)
admin.site.register(Gorevli,GorevliAdmin)
admin.site.register(Sorumlu)
admin.site.register(Log)