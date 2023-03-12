# Laboratuvar Giriş Kontrol Projesi

Bu proje, Django web çerçevesi kullanılarak yazılmış bir laboratuvar giriş kontrol projesidir. Proje, laboratuvar sorumlusunun labControl web sayfasında giriş yaparak laboratuvarda bulunan görevlileri görüntüleyebildiği, görevli ekleyip silip düzenleyebildiği ve giriş çıkış yapan görevlilerin loglarını görebildiği bir programdır.

## **Gereksinimler**

Projenin çalışması için aşağıdaki yazılım bileşenleri gereklidir:

- Python 3.x
- Django 3.x
- PostgreSQL (veritabanı olarak kullanılmıştır)

## **Kurulum**

- Öncelikle, projeyi GitHub üzerinden indirin veya kopyalayın:

```bash
$ git clone https://github.com/SevvalBayramli/laboratuvar-giris-kontrol-projesi.git
```

- Proje dizinine gidin
- Sanal ortamı oluşturun:

```bash
$ python3 -m venv myenv
```

- Sanal ortamı etkinleştirin:

```bash
$ source myenv/bin/activate
```

- Gereksinimleri yükleyin
- Veritabanını oluşturun:

```bash
$ python manage.py makemigrate
$ python manage.py migrate
```

- Yönetici hesabı oluşturun:

```bash
$ python manage.py createsuperuser
```

- Sunucuyu başlatın:

```bash
$ python manage.py runserver
```

- Tarayıcınızda **`http://127.0.0.1:8000/`** adresini açın.

## **Kullanım**

Proje, laboratuvar sorumlusunun girişi ile başlar. Giriş sayfasında laboratuvar sorumlusu, kullanıcı adı ve şifresi ile giriş yapabilir.

Laboratuvar sorumlusu, labControl web sayfasında aşağıdaki işlevleri yerine getirebilir:

- Görevlileri görüntüleme, ekleme, silme ve düzenleme
- Giriş-çıkış yapan görevlilerin loglarını görüntüleme

## **Katkıda Bulunma**

Bu proje açık kaynaklıdır ve katkıda bulunmak isteyen herkes hoşgeldiniz. Herhangi bir hata veya öneri için GitHub üzerinden bir konu açabilirsiniz.
![admin](https://user-images.githubusercontent.com/72937239/223791433-d88058a1-1378-48fb-ad00-23a80fa1a29d.PNG) ![edit](https://user-images.githubusercontent.com/72937239/223791546-b1588284-0c64-49d5-8220-38831f8727a9.PNG)
![ekle](https://user-images.githubusercontent.com/72937239/223791552-4a5591a6-56c6-4ccd-b44e-a98097a747c5.PNG)
![log](https://user-images.githubusercontent.com/72937239/223791557-a28229dc-dab4-4338-b7bc-98c8d0de670a.PNG)
![var-olan](https://user-images.githubusercontent.com/72937239/223791559-d2dfd1a6-e346-4927-bd35-da6d2da9cb6b.PNG)
![ekle-alert](https://user-images.githubusercontent.com/72937239/223791625-f9831772-9c31-4055-9331-844045adce84.PNG)
![ekle-alert2](https://user-images.githubusercontent.com/72937239/223791629-6fbfe079-9c79-4289-aa0f-b3b93974a51c.PNG)
![Capture](https://user-images.githubusercontent.com/72937239/223791602-37fd1331-f2c5-4f7f-ade2-ad1d70dd794e.PNG)
