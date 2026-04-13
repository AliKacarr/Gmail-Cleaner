# GMail Cleaner

Gmail iletilerinizi belirlediğiniz e-posta adreslerine göre filtreleyerek topluca çöp kutusuna taşıyan, kullanımı kolay bir Python otomasyon betiği.

## Ne yapar?

Bu betik, tarayıcıda sayfalarca mail seçip silme zahmetini azaltmak için aşağıdaki adımları otomatikleştirir:

- Gmail API ve OAuth 2.0 ile güvenli kimlik doğrulaması yapar
- `filterFrom.txt` dosyasındaki hedef e-posta adreslerini okur
- Bu adreslerin `from:` (gelen) veya `to:` (giden) alanında geçtiği iletileri bulur
- Eşleşen iletileri Gmail Çöp Kutusu'na taşır (kalıcı silme yapmaz)
- İşlem sonunda bulunan ve taşınan ileti sayısını konsola yazar

## Video rehberi

Kurulum, API anahtarı alma ve kullanım süreçlerini adım adım anlattığım videoya aşağıdan ulaşabilirsiniz: 
**[Kurulum ve kullanım videosu](#)**

## Gereksinimler

- Python 3
- Google Cloud Console'da etkinleştirilmiş Gmail API
- OAuth Desktop App kimlik bilgileri (`credentials.json`)

Bağımlılıkları kurmak için:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Kurulum ve kullanım

1. Projeyi indirin veya klonlayın.
2. [Google Cloud Console](https://console.cloud.google.com/) üzerinden Gmail API'yi etkinleştirin.
3. Credentials bölümünden yeni bir OAuth istemcisi oluşturun ve uygulama türü olarak Desktop app seçin.
4. İndirdiğiniz JSON dosyasını `credentials.json` olarak proje köküne koyun.
5. Gerekliyse OAuth onay ekranında hesabınızı test kullanıcısı olarak ekleyin.
6. `filterFrom.txt` dosyasına temizlemek istediğiniz e-posta adresini yazın.
7. Betiği proje dizininde çalıştırın:

```bash
python mail_deleter.py
```

İlk çalıştırmada tarayıcıda yetkilendirme penceresi açılır. Onay sonrası token dosyası `token files` klasörüne kaydedilir.

## Filtre mantığı

`filterFrom.txt` dosyasına yazdığınız e-posta adresi, aşağıdaki sorgu formatına dönüştürülür:

```text
(from:ornek@gmail.com OR to:ornek@gmail.com)
```

Bu sayede yazdığınız adrese ait hem gelen hem giden iletiler kapsanır.

## Özelleştirme

Sadece gelen veya sadece giden mailleri hedeflemek, tarih aralığı eklemek ya da daha gelişmiş filtreleme yapmak için Gmail arama operatörlerini kullanabilirsiniz:  
[Gmail arama operatörleri](https://support.google.com/mail/answer/7190?hl=tr)

Gerekiyorsa `mail_deleter.py` ve `querybuilder.py` içindeki sorgu oluşturma mantığını ihtiyacınıza göre düzenleyebilirsiniz.

## Önemli uyarı

Bu betik eşleşen iletileri otomatik olarak Çöp Kutusu'na taşır. Geniş çaplı temizlikten önce tek bir adresle dar kapsamlı test yapmanız önerilir. Çöp Kutusu'ndaki iletiler Gmail politikasına göre belirli süre geri yüklenebilir.
