# Twitter Catcher

Twitter Catcher ile yapay zeka projeleriniz için twitter içerisinden tweetleri ve twitter api'sinin izin verdiği pek çok bilgiyi çekebilirsiniz.

## Başlarken

Twitter Catcher, Twitter api'sini kullanır. API'nin size sağladığı keyleri ve tokenları `key_token.txt` dosyasına alt alta yazmanız gerekiyor.

**example** klasörü içerisindeki **search.py** dosyasında örnek bir kullanım senaryosu mevcut.

### Sınıfı Tanımlayın

```
bot = twitter_catcher()
```

### Giriş Yapın

Developer hesabınız sayesinde edindiğiniz keyler ve tokenlar ile giriş yapın.

```
api = bot.login()
```

### Arama Tanımlama

`.search()` metodu içerisine üç paremetre alır.

* `api` yukarıda login olduğumuz değişken.
* Aranacak kelime
* çekilecek tweet sayısı. (1000'i geçmeyin.)

```
search = bot.search(api,"#pazartesi",200)
```

### DataFrame Oluşturma

**search** değişkeni ile elde ettiğimiz bilgileri derli toplu göstermeye yarar. Burada **pandas**'tan yararlanılır.

```
df = bot.dataframe(search)
```

### SQL'e aktarma

Edindiğimiz bilgilerin kaybolmaması için SQL içerisinde saklayabilirsiniz. Bunun için oluşturduğunuz dataframe'i `to_sql()` metoduyla SQL'e aktarabilirsiniz.

```
bot.to_sql(df)
```

#### Açıklama

Burada SQLite kullanılmıştır. Ve isimlendirme olarak **Yıl-Hafta Numarası.db** kullanılmıştır.

SQL içerisindeki tablo ismini **search** değişkeninde tanımladığınız **aranan kelime**'den almıştır.



### Gereklilikler Ve Kurulum

Twitter_catcher'ı kullanabilmeniz için 

* Twitter geliştirici hesabına sahip olmanız,

* SQLite'ın bilgisayarınızda kurulu olması,

* **requirements.txt** içerisindeki modüllerin kurulması gerekmektedir.

  * `pip install requirements.txt`
    
    

## Meta

Furkan Tolga Yüce – [@furkantolgayuce](https://twitter.com/furkantolgayuce) – [yucefurkantolga@gmail.com](mailto:yucefurkantolga@gmail.com)

https://github.com/furkantolgayuce/twitter_catcher
