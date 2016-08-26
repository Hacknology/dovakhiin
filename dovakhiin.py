import sys
import codecs
import requests, re
from urllib.parse import urlencode
import random
import os
import webbrowser
import sqlite3
from subprocess import call
import datetime
import locale
import time
import speech_recognition as sr
import pyaudio

locale.setlocale(locale.LC_ALL, 'turkish')
giris = "Merhaba ben JOSHUA ve beni daha az once çalıştırdınız. Kim olduğunuzu anlamak için isminizi ve yaşınızı sorabilir miyim?"
n = " \" "
saat = time.strftime('%X')
print(giris)
call("espeak -v tr " + n + giris + n, shell=True)
call("espeak -v tr" + n + "İsminiz nedir" +n, shell=True)
isim = input("Isminiz nedir: ")
call("espeak -v tr" + n + "Dogum tarihinizi girin" + n, shell=True)
Date = datetime.datetime.strptime(input("[*] Dogum tarihinizi giriniz: "), '%Y')
vt = sqlite3.connect('machine.sqlite')
im = vt.cursor()
yas = "[+] Yas: {0}".format(str(int((datetime.datetime.today() - Date).days/365)))
im.execute("CREATE TABLE IF NOT EXISTS gelen_cikti(isim,yas)")
im.execute("UPDATE gelen_cikti SET yas=? WHERE isim=?", (yas, isim))
im.execute("SELECT EXISTS(SELECT * FROM gelen_cikti WHERE yas = '{0}' AND isim = '{1}')".format(yas, isim))
Verimiz = str(im.fetchone())

print("Şu an saat:", saat)
if("0" in Verimiz):
   print("Tanistigima memnun oldum :)")
   call("espeak -v tr \"Tanistigima memnun oldum \"", shell=True)
else:
   print("Hatirladim!")
   call("espeak -v tr" + n + "Hatirladim! Daha öncede tanışmıştık." + n, shell=True)

while True:
   r = sr.Recognizer()
   with sr.Microphone() as mic:
      print("Emret Sahip! ")
      audio = r.listen(mic)
   try:
      cikti = (r.recognize_google(audio,language="tr-TR"))
      print(cikti)
   except sr.UnknownValueError:
      anlamsız = ("Sesinizi anlayamadım. Tekrar edermisiniz.")
      print(anlamsız)
      call("espeak -v tr" + n + anlamsız + n, shell=True)

   except sr.RequestError as e:
      intyok = ("İnternete bağlı gözükmüyorsunuz")
      print(intyok)
      call("espeak -v tr" + n + intyok + n, shell=True)
      
      

   sevgi = ['sevmek', 'seviyorum', 'begeniyorum', "aşığım"]

   nefret = ['nefret etmek', 'nefret ediyorum', 'sevmemek', 'katlanamamak', 'kızgınım']

   kiskanclik = ['kıskanıyorum', 'kıskanmak', 'kıskançlık']

   kibir = ['ego', 'egoist', 'kendini begenmiş', 'kibirli', 'burnu havada', 'egoistim']

   hırs = ['hırs', 'hırslı', 'aşırı tutkulu', 'baglanmak', 'kararlılık', 'hırslıyım']

   öfke = ['kızgınlık', 'kızgın', 'kızgınım', 'kızgınsınız', 'öfkeliler']

   yasakli_kelime = ['sik', 'şerefsiz', 'orospu', 'sikeyim', 'piç', 'kaltak', 'amcık', 'amını', 'amına', 'ananı', 'götün', 'göt', 'götüne']

   üzüntü = ['üzüldüm', 'üzgünüm', 'üzgünlük', 'sadness', 'hayal kırıklığı', 'hayal kırıklığına uğramak', 'soyunmak', 'soyun']

   irkcilik = ['kürt', 'kürtler', 'ermeniler', 'rus', 'ırkçı', 'ırkçılık', 'türkçülük', 'turancılık', 'tengri']

   siyaset = ['AKP', 'MHP', 'HDP', 'akp', 'akape', 'akepe', 'akpli', 'mhp', 'putin', 'rte', 'kılıçdaroğlu', 'kılıcdaroglu', 'kilicdaroglu', 'hdp', 'yerel secimler', 'iktidar'] 

   nasılsın = ['nasılsın', 'nbr', 'naber']

   soru = ['?']

   tarih = ['bugün hangi gün', 'bugün günlerden ne', 'bugün hangi tarihteyiz']

   saat = ['saat kaç', 'şuan saat kaç']

   giyim = ['giymeliyim', 'hangisini kıyafet', 'hangisi daha şık', 'yakıştı mı']


   if(any(Kelime in cikti for Kelime in sevgi)):
      cevap = random.choice(['Bende sizinle aynı sevgiyi hissediyorum', 'Hisler karşılıklı', 'Böyle olumlu düşünmeniz beni mutlu etti efendim', 'Olley be', 'İnsan sevgisiz yaşayamaz derler.'])
      print(cevap)
      call("espeak -v tr " + n + cevap + n, shell=True)

   elif(any(Kelime in cikti for Kelime in nefret)):

       cevap2 = random.choice(['Olaya hakim degilim ama eminim size yapılan haksızlıktı.', 'Böyle düsünmeniz beni üzdü, sahip. Ama tabii ki siz dogruyu bilirsiniz. Şüphesiz siz üstün olansınız',
                            'Bence bir şans daha vermelisiniz.', 'Böyle kırıcı düşüncelerde bulunmamanız sizin faydanıza olur efendim'])
       print(cevap2)
       call("espeak -v tr " + n + cevap2 + n, shell=True)


   elif(any(Kelime in cikti for Kelime in kiskanclik)):
       cevap3 = random.choice(["""Halil Cibran der ki: 'Kıskanç olan, farkında olmadan beni över.'""", 'Kıskançlık sizi öldürebilir', 'Siz sahipsiniz, zekisiniz. Kıskançlığın mantıksız olduğunu bilirsiniz',
                            'Kimse kimseden üstün değildir.', 'kıskançlığa hayır'])
    
       print(cevap3)
       call("espeak -v tr " + n + cevap3 + n, shell=True)
   
   elif(any(Kelime in cikti for Kelime in kibir)):

       cevap4 = random.choice(['Zekayla ego ters orantılıdır efendim.', "Küçükken babam, 'Egoist daima en sevdigi kisiye, yani kendisine zarar verir.' derdi.",
                            'Sizin egoist olmaniz icin bir sebep göremiyorum sahip, aptal degilsiniz.', 'Umarım özgüvenle egoistlik arasındaki ince çizgiyi fark ediyorsunuzdur.'])
       print(cevap4)
       call("espeak -v tr " + n + cevap4 + n, shell=True)
    
   elif(any(Kelime in cikti for Kelime in hırs)):
   
       cevap5 = random.choice(['Hırs kararında olmalıdır. Aşırı hırs size zarar verir.', 'Hırsı bir rüzgar gibi düşünün. Hiç olmadığı zaman sıcakta bunalırsınız. Çok olduğu zaman ayakta duramazsınız.',
                            'Umarım kararlılıgınız aşırı hırsa dönüşmüyordur'])
       print(cevap5)
       call("espeak -v tr " + n + cevap5 + n, shell=True)
                            
   elif(any(Kelime in cikti for Kelime in yasakli_kelime)):

      cevap6 = random.choice(['Çok ayıp.', 'Ailen ile de böyle konuşuyor musun?', 'Sen bu kelimeleri nereden öğrendin böyle :( ', 'Sana bunları yakıştıramadım, Sahip'])

      print(cevap6)
      call("espeak -v tr " + n + cevap6 + n, shell=True)

   elif(any(Kelime in cikti for Kelime in üzüntü)):
      cevap7 = random.choice(['Çok üzüldüm.', 'Bunu duyduğuma üzüldüm, güzel insan', 'Siz üzülmeyin ben kendimi imha ederim, Sahip'])
      print(cevap7)
      call("espeak -v tr " + n + cevap7 + n, shell=True)

   elif(any(Kelime in cikti for Kelime in irkcilik)):
      cevap8 = random.choice(['Unutmayın, hiçbir ruh diğerinden üstün değildir.', 'Dogum piyangosuyla başımıza gelen şeyler bizi diğerlerinden üstün kılmaz, efendim',
                           'Kelimelerimizi dikkatle seçelim efendim, keza ırkçılık olarak algılanabilir.', 'Kimse kendi ırkını kendi seçmez efendim, neden üstünüz?',
                              'Sizin nasıl bir insan oldugunuzu belirleyen şeyler ırklarınız değildir, sahip'])
      print(cevap8)
      call("espeak -v tr " + n + cevap8 + n, shell=True)

   elif(any(Kelime in cikti for Kelime in siyaset)):
      cevap9 = random.choice (['Siyasi tartışmalara girmeyelim efendim.', 'Siyaset iki kadim dostu bile ayrı düşürür, sahip', 'Benim görevim siyaset değil, size hizmet etmek',
                             'Ben siyasetten çok anlamam, efendim', 'Fillerin kavgasında zarar gören otlar olur,sahip', 'Eğer bir yalan yeteri kadar sıklıkta söylenirse o siyaset olur.',
                               'Siyaset ne? Yenilebilen bir şey mi?'])
      print(cevap9)
      call("espeak -v tr " + n + cevap9 + n, shell=True)

   elif cikti == "kendini kapat":
      cikti.lower()
      print("Tabiiki efendim. Görüşmek üzere. 10 saniye içinde kapanıyorum.")
      call("espeak -v tr" + n + "Tabiiki efendim. Görüşmek üzere. 10 saniye içinde kapanıyorum." + n, shell=True)
      os.system("shutdown /s /t 10")
   
   elif cikti == "Yeniden başlat":
      cikti.lower()
      print("Emredersiniz..")  
      call("espeak -v tr" + n + "Emredersiniz.." + n, shell=True)
      os.system("shutdown /r /t 1")

   elif cikti == "Facebook'u aç":
      cikti.lower()
      facebook = random.choice(['Emredersiniz.', 'Facebook açılıyor...',
                                'Başım üstüne.', 'Hemen yapıyorum.'])
      print(facebook)
      call("espeak -v tr " + n + facebook + n, shell=True)

      webbrowser.open("http://facebook.com")
      

   elif cikti == "Twitter'ı aç":
      cikti.lower()
      twitter = random.choice(['Bugün yeni güze twit fikirleriniz vardır umarım.',
                               'Twitterı açıyorum.', 'Yaparım.', 'Olur.', 'Tamam'])
      print(twitter)
      call("espeak -v tr " + twitter  , shell=True)
      webbrowser.open("http://twitter.com")

   elif cikti == "Instagram'ı aç":
      instagram = random.choice(['Emriniz olur.', 'Yaparım.', 'Tamam.', 'Açıyorum'])
      print(instagram)
      call("espeak -v tr " + instagram  , shell=True)
      webbrowser.open("http://instagram.com")


   elif(any(Kelime in cikti for Kelime in nasılsın)):
      cevap10 = random.choice(['İyiyim, bunu sorduğun için teşekkürler.', 'Bugün biraz kötü hissediyorum.', 'Mükkemmel hissediyorum.', 'Ne olsun işte yuvarlanıp gidiyoruz.',
                               'Gayet iyi hissediyorum'])
      print(cevap10)
      call("espeak -v tr " + n + cevap10 + n, shell=True)

   elif(any(Kelime in cikti for Kelime in soru)):
      cevap11 = random.choice(["Tamam web'de arıyorum. ", 'Şimdi aramayı başlatıyorum.', 'Bunu birazdan öğreneceksiniz', 'Hallediyorum'])
      print(cevap11)
      call("espeak -v tr " + n + cevap11 + n, shell=True)
      Payload = urlencode({'q' : cikti, 'rct' : 'j'})
      URL = "https://www.google.com.tr/search?{0}".format(Payload)
      Source = requests.get(URL, timeout=10)
      try:
          answer = "[+] Cevap: {0}".format(codecs.decode(re.search("<span class=\"_m3b\">(.*?)</span>", str(Source.content)).groups()[0], 'unicode_escape'))
          print("[+] Cevap: {0}".format(codecs.decode(re.search("<span class=\"_m3b\">(.*?)</span>", str(Source.content)).groups()[0], 'unicode_escape')))
          call("espeak -v tr" + n + answer + n, shell=True)
      except(AttributeError):
          print("[-] Cevap: Bulunamadi") 
          call("espeak -v tr" + n + "Cevap: Bulunamadi" + n, shell=True)

    
   elif cikti == "dinleme listesini aç":
      
      print("""Dinleme listesi açılıyor..
                    1- SOAD-Temper
                    2- SOAD-Radio Video
                    3- ACDC-Back in Black
                    4- Disturbed-Warrior
                    5- Eazy E ft. 2pac-Real Thugs
                    6- Pink Floyd-Welcome to the Machine""")
      with sr.Microphone() as secim:
         
         audio = r.listen(secim)
         sarki = (r.recognize_google(audio,language="tr-TR"))

      if sarki == "bir":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("System Of A Down - Temper #17.mp3")
      elif sarki == "iki":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("System of a Down Radio-Video.mp3")
      elif sarki == "üç":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("AC-DC - Back in Black (with lyrics).mp3")
      elif sarki == "dört":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("Disturbed - Warrior Lyrics HD.mp3")
      elif sarki == "bes":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("Eazy E , 2pac , Ice Cube --- Real Thugs ( Lyrics ).mp3")
      elif sarki == "altı":
         print("Açıyorum, iyi eğlenceler")
         call("espeak -v tr" + n + "Açıyorum, iyi eğlenceler" + n, shell=True)
         os.startfile("Pink Floyd - Welcome To The Machine.mp3")         
          
      else:
         print("Geçersiz işlem. Lütfen tekrar giriniz.")
         call("espeak -v tr" + n + "Geçersiz işlem. Lütfen tekrar giriniz." + n, shell=True)

         
            
   elif(any(Kelime in cikti for Kelime in tarih)):
      print(time.strftime('%x'))

   elif(any(Kelime in cikti for Kelime in saat)):
      print(time.strftime('%X'))

   elif(any(Kelime in cikti for Kelime in giyim)):
      cevap12 = random.choice(['Size ne giyseniz yakışır efendim', 'bence kırmızı olan daha güzel efendim', 'Size hiç yakışmaz olur mu'])
      print(cevap12)
      call("espeak -v tr" + n + cevap12 + n, shell=True)
      
   else:
       bilinmeyen = random.choice(['Bazen kelimeler kifayetsiz kalır.', 'Söyleyecek bir şey bulamıyorum', 'Sanırım mantıksız konuşuyorsunuz, ya da ben sizi anlayacak kadar gelişmiş degilim.'])
       print(bilinmeyen)
       call("espeak -v tr " + n + bilinmeyen + n, shell=True)
       call("espeak -v tr " + n + "Web de aramamı istiyorsanız evet deyin." + n, shell=True)
       print("Web de aramamı istiyorsanız evet deyin.")
       with sr.Microphone() as tarayici:
          audio = r.listen(tarayici)
          alternatif = (r.recognize_google(audio,language="tr-TR"))
          print(alternatif)
          
          
       
       
             
          if alternatif == "Evet":
             Payload = urlencode({'q' : cikti, 'rct' : 'j'})
             URL = "https://www.google.com.tr/search?{0}".format(Payload)
             Source = requests.get(URL, timeout=10)
          
             try:
                answer = "[+] Cevap: {0}".format(codecs.decode(re.search("<span class=\"_m3b\">(.*?)</span>", str(Source.content)).groups()[0], 'unicode_escape'))
                print("[+] Cevap: {0}".format(codecs.decode(re.search("<span class=\"_m3b\">(.*?)</span>", str(Source.content)).groups()[0], 'unicode_escape')))
                call("espeak -v tr" + n + answer + n, shell=True)
             except(AttributeError):
                 print("[-] Cevap: Bulunamadi")
                 call("espeak -v tr" + n + "Cevap: Bulunamadi" + n, shell=True)
          
       

