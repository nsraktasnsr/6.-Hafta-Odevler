print('b.')
'''
         Sayi Tahmin
		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi 
		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin 
		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)

		Ornek:

			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece 
			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz. 
			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)

			 Pc'nin tahmini = 89
			 Kullanicinin inputu = -
			 Pc'nin tahmini = 45
			 Kullanicinin inputu = +
			 Pc'nin tahmini = 56
			 Kullanicinin inputu = "Enter"
'''
print('>>>>>>>> SAYI TAHMIN OYUNU <<<<<<<<<')
while True:
    print('\n----------------------------------------------------------------------')
    print('0-100 arasinda aklindan bir sayi tut')
    cvp = input('sayi tuttun mu?....evet="y"...hayir="n"...>>>').lower()
    if cvp == 'n':
        continue
    else:
        max = 100
        min = 0
        tahmin = int((100 - 0) / 2)
        cvp=input('\ntuttugunuz sayi 50 mi?....evet="y"...hayir="n"...>>>').lower()
        if cvp=='y' :
            print('ilk denemede bildim')
        elif cvp=='n':
            while True:
                print('tuttugun sayi {} mi?'.format(tahmin))
                cvp=input('doru mu?...dogru ise:"y"..yanlis ise:"n"').lower()
                if cvp =='y':
                    quit()
                elif cvp=='n':
                    yon = input('asagi mi?... cikayim...yukari mi?...asagi icin (-)...yukari icin (+)...>>>')
                    if yon == '-':
                        max = tahmin
                    elif yon == '+':
                        min = tahmin
                    else:
                        print('!!!...HATA...!!!...lutfen asagi icin (-)...yukari icin (+)')
                    tahmin = int((max + min) / 2)
                else:
                    print('!!!HATA!!!...dogru ise:"y"..yanlis ise:"n"')
        else:
            print('!!! HATA !!!...yanlis giris yaptiniz....evet="y"...hayir="n"')
            print('~'*25,'bastan basliyoruz','~'*25)
