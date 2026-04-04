
Gmail iletilerinizi topluca çöp kutusuna taşıyan python betiği ⚡🗑️

## Ne yapar?

- Gmail API ile OAuth kullanarak kimlik doğrular
- `filterFrom.txt` içindeki e-posta adreslerini okur
- bu adreslerin `from:` veya `to:` alanında geçtiği iletileri arar
- tüm eşleşmeleri Gmail Çöp Kutusu’na taşır
- kaç ileti bulunduğunu ve kaçının taşındığını yazdırır

## Video rehberi

Kurulum ve işlemlerin nasıl yapılacağını adım adım anlattığım video: **[Kurulum ve kullanım videosu](#)**  

## Kurulum ve kullanım

**Bilgisayarınızda Python kurulu olduğundan emin olun**.

1. **Adım:** GitHub’dan proje dosyalarını indirin (veya depoyu klonlayın).
2. **Adım:** [Google Cloud Console](https://console.cloud.google.com/)’da projenizde **Gmail API**’yi etkinleştirin.
3. **Adım:** **Credentials (Kimlik bilgileri)** bölümünden yeni OAuth istemcisi oluştururken **Desktop app** türünü seçin.
4. **Adım:** Size verilen JSON dosyasını proje dizinine **`credentials.json`** adıyla kaydedin.
5. **Adım:** Oluşturduğunuz masaüstü istemcisinin ayarlarına gidip **veri erişim izinlerini** verin ve kendi Google hesabınızı **test kullanıcısı** olarak ekleyin (OAuth ekranı gerekiyorsa).
6. **Adım:** `filterFrom.txt` dosyasını açıp silme işlemi uygulamak istediğiniz eposta adresini yazın.
7. **Adım:** Terminalde proje klasöründeyken şunu çalıştırın:

```bash
python mail_deleter.py
```

İlk çalıştırmada tarayıcıda Google yetkilendirmesi açılır; onaydan sonra `token files` klasörüne bir token dosyası kaydedilir.

Detaylı anlatım için yukarıdaki **video rehberi**ne bakabilirsiniz.

## Gereksinimler

- Python 3
- Google Cloud’da Gmail API’nin açık olması
- OAuth **Desktop app** kimlik bilgileri → proje kökünde `credentials.json`

Bağımlılıklar:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Filtre davranışı

Her satır, kabaca şu Gmail sorgusuna dönüştürülür:

```text
(from:ornek@gmail.com OR to:ornek@gmail.com)
```

Yani hem o adresten **gelen** hem de o adrese **giden** mailler eşleşir. Birden fazla satır `OR` ile birleştirilir.

**Özelleştirme:** Kodu yalnızca **gönderilen** veya yalnızca **gelen** maillerin silinmesi (taşınması) için `mail_deleter.py` içindeki sorguyu buna göre düzenleyebilirsiniz; böylece davranışı ihtiyacınıza göre daraltırsınız.

## Özel sorgular

Kendi Gmail arama sorgunuzu kullanmak isterseniz [Gmail arama operatörleri](https://support.google.com/mail/answer/7190?hl=tr) dokümanına bakıp `mail_deleter.py` içinde üretilen sorguyu değiştirebilirsiniz.

## Uyarı

Eşleşen mailler otomatik olarak Çöp Kutusu’na taşınır!
