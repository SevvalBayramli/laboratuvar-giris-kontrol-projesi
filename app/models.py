from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime, timezone



class Gorevli(models.Model):
    image=models.ImageField(upload_to="lab")
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150,unique=True)
    card_num=models.CharField(max_length=150,unique=True)#kart numarasının uzunluğunu ayarla
    status=models.BooleanField(default=0)
    def __str__(self) -> str:
        full_name=self.first_name+" "+self.last_name
        return full_name


class Lab(models.Model):

    isim=models.CharField(max_length=150)
    gorevli=models.ManyToManyField(Gorevli,blank=True)
    slug=models.SlugField(blank=True,unique=True,db_index=True,editable=False)
    def __str__(self) -> str:
        return f"{self.isim}"
    
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.isim)
        super().save(*args,**kwargs)


class Sorumlu(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    lab=models.ForeignKey(Lab,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.user}"
    
    
class Log(models.Model):
    lab=models.ForeignKey(Lab,null=True,on_delete=models.SET_NULL)
    lab_gorevli=models.ForeignKey(Gorevli,null=True,on_delete=models.SET_NULL) 
    zaman=models.DateTimeField(auto_now=True)
    durum=models.BooleanField(null=True,default=None)
    
    def __str__(self) -> str:
        string=str(self.lab)+" "+str(self.lab_gorevli)
        return string
    
                    
        


   
