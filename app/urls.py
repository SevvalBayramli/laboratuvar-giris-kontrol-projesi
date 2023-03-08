from django.contrib import admin
from django.urls import path

from app import views


urlpatterns = [
    
    path('',views.index,name="index"),
    path('log/',views.log,name="log"),
    path('giris/<int:id>',views.giris,name="giris"),
    path('cikis/<int:id>',views.cikis,name="cikis"),
    path('ekle/',views.ekle,name="ekle"),
    path('varolan/',views.varolan,name="varolan"),
    path('varolanekle/<int:id>',views.varolanekle,name="varolanekle"),
    path('sil/<int:id>',views.sil,name="sil"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('gorevliduzenle/',views.gorevliduzenle,name="gorevliduzenle"),
    
]
