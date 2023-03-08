
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app.models import Gorevli, Lab, Log,Sorumlu
from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        messages.success(request, 'Başarılı bir şekilde kaydedildi!')
        context={
            "lab":Sorumlu.objects.get(user=request.user).lab,
            "gorevliler":Sorumlu.objects.get(user=request.user).lab.gorevli.filter(status=1),
            
        }
        return render(request,"index.html",context)
    else:
        return redirect("login")



def ekle(request):
    if request.method=="POST" and request.FILES['image']:
        cardnum=request.POST["cardnum"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        image=request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        gorevli=Gorevli(image=image,card_num=cardnum,first_name=firstname,last_name=lastname,email=email)
        try:
            gorevli.save()
            gorevli_id=str(gorevli.id)
            sorumlu_id=str(Sorumlu.objects.get(user=request.user).lab.id)
            
            sql = "Insert  into  app_lab_gorevli (lab_id,gorevli_id) values (%s,%s)"
            
            #Sorguyu veritabanında çalıştır
            with connection.cursor() as cursor:
                cursor.execute(sql, [sorumlu_id,gorevli_id])
                #rows = cursor.fetchall()
            
            context={
                "success":'Görevli başarıyla eklendi'
            }
            
            return render(request,"app/gorevliekle.html",context)
        except IntegrityError:
            context={
                "danger":'Email adresi veya Kart numarası kayıtlı'
            }
            return render(request,"app/gorevliekle.html",context)
    
    context={
                "logs":Log.objects.all(),
                "lab":Sorumlu.objects.get(user=request.user).lab,
            }  
    return render(request,"app/gorevliekle.html",context)

def varolanekle(request,id):
    sorumlu_id=str(Sorumlu.objects.get(user=request.user).lab.id)
    
    sql = "Insert  into  app_lab_gorevli (lab_id,gorevli_id) values (%s,%s)"
    #Insert  into  TabloAdı (Kolonadi1,Kolonadi2,Kolonadi3...)  values (deger1,deger2,deger3..)
    #Sorguyu veritabanında çalıştır
    with connection.cursor() as cursor:
        cursor.execute(sql, [sorumlu_id,id])
        #rows = cursor.fetchall()
    return redirect("index")

def varolan(request):
    
    gorevli=[]
    
    olanGorevli=Sorumlu.objects.get(user=request.user).lab.gorevli
    
    for a in Gorevli.objects.all():
        if a not in olanGorevli.all():
            gorevli.append(a)
            
   
    
    context={
        "gorevliler":gorevli,
    }

    return render(request,"app/varolan.html",context)



def log(request):
    
    print(Sorumlu.objects.get(user=request.user).lab)
    context={
        "logs":Log.objects.all().order_by('-id'),
        "lab":Sorumlu.objects.get(user=request.user).lab,
    }
    return render(request,"app/log.html",context)



def gorevliduzenle(request):
    gorevli=Sorumlu.objects.get(user=request.user).lab.gorevli
    if request.method=="POST":
        gorevliara=request.POST["gorevliara"]
          
        context={
            "gorevliler":gorevli.filter(last_name=gorevliara)
        }   
    else:
        context={
            "gorevliler":gorevli.all(),
        }
    return render(request,"app/gorevliduzenle.html",context)

def sil(request,id):
    gorevli_id=str(id)
    sorumlu_id=str(Sorumlu.objects.get(user=request.user).lab.id)
    sql = "DELETE FROM app_lab_gorevli WHERE lab_id=%s and gorevli_id=%s"
    with connection.cursor() as cursor:
            cursor.execute(sql, [sorumlu_id,gorevli_id])
            
    gorevli=Sorumlu.objects.get(user=request.user).lab.gorevli
    
    
    if request.method=="POST":
        gorevliara=request.POST["gorevliara"]
          
        context={
            "gorevliler":gorevli.filter(last_name=gorevliara)
        }   
    else:
        context={
            "gorevliler":gorevli.all(),
            "success":"Görevli başarıyla laboratuvardan çıkarıldı"
        }
    return render(request,"app/gorevliduzenle.html",context)

def edit(request,id):
    if request.method=="POST" :
        cardnum=request.POST["cardnum"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        
        Gorevli.objects.filter(id=id).update(card_num=cardnum,first_name=firstname,last_name=lastname,email=email)
        
        gorevli=Sorumlu.objects.get(user=request.user).lab.gorevli
        
        context={
            "gorevliler":gorevli.all(),
            "success":"Görevli başarıyla düzenlendi"
        }
        return render(request,"app/gorevliduzenle.html",context)
        
    gorevli=Sorumlu.objects.get(user=request.user).lab.gorevli.filter(id=id).get()
    context={
        "gorevli":gorevli
    }
    print(gorevli.first_name)
    #return render(request,"gorevliduzenle.html",context)
    return render(request,"app/edit.html",context)
    
    
    
    
def giris(request,id):
    gorevli=Gorevli.objects.all().filter(id=id).get()
    print(gorevli.status)
    _lab=Sorumlu.objects.get(user=request.user).lab
    zaman=datetime.now()
    
    if gorevli.status==False:
        Gorevli.objects.all().filter(id=id).update(status=True)
        log=Log(lab=_lab,lab_gorevli=gorevli,zaman=zaman,durum=True)
        log.save()
        
    else:
        return HttpResponse(gorevli.first_name+" "+gorevli.last_name+" bu Llboratuvara daha önce giriş yapmıştır ")
    
    
    return HttpResponse(gorevli.first_name+" "+gorevli.last_name+" "+str(_lab)+" laboratuvarına giriş yaptı")
    
def cikis(request,id):
    gorevli=Gorevli.objects.all().filter(id=id).get()
    print(gorevli.status)
    _lab=Sorumlu.objects.get(user=request.user).lab
    zaman=datetime.now()
    
    if gorevli.status==True:
        Gorevli.objects.all().filter(id=id).update(status=False)
        log=Log(lab=_lab,lab_gorevli=gorevli,zaman=zaman,durum=False)
        log.save()
        
    else:
        return HttpResponse(gorevli.first_name+" "+gorevli.last_name+" bu laboratuvara daha önce çıkış yapmıştır ")
    
    
    return HttpResponse(gorevli.first_name+" "+gorevli.last_name+" "+str(_lab)+" labına çıkış yaptı")
