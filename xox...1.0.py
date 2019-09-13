print('b.')
import random as r
print('xox...1.0')
def tablo():
    print('''1,2,3
4,5,6
7,8,9''')
tablo()
tahta = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
def oyun_tahtasi():
    for i in tahta:
        print(*i)
sira=r.randint(0,100)   # kimin once baslayacagina karar verir
x_o=[]      #yapilan hamleleri bir listede topladik
while True:
    if sira % 2 == 0:
        isaret = "X"
    else:
        isaret = "O"
    print(f'sira :   {isaret}')
    if isaret == 'X':
        cvp = input('\n1-9 arasinda bir yer giriniz :')
        if cvp not in x_o:
            # tahtaya hamle yazdirma
            if cvp == '1':
                tahta[0][0] = 'x'
            elif cvp == '2':
                tahta[0][1] = 'x'
            elif cvp == '3':
                tahta[0][2] = 'x'
            elif cvp == '4':
                tahta[1][0] = 'x'
            elif cvp == '5':
                tahta[1][1] = 'x'
            elif cvp == '6':
                tahta[1][2] = 'x'
            elif cvp == '7':
                tahta[2][0] = 'x'
            elif cvp == '8':
                tahta[2][1] = 'x'
            elif cvp == '9':
                tahta[2][2] = 'x'
            # hamle sonrasi tahtayi tekrar yazdirdik
            oyun_tahtasi()

            # kazanma durumunu kontrol et
            for i in tahta[0], tahta[1], tahta[2], \
                     [tahta[0][0], tahta[1][0], tahta[2][0]], \
                     [tahta[0][1], tahta[1][1], tahta[2][1]], \
                     [tahta[0][2], tahta[1][2], tahta[2][2]], \
                     [tahta[0][0], tahta[1][1], tahta[2][2]], \
                     [tahta[0][2], tahta[1][1], tahta[2][0]]:
                if i.count('x') == 3:
                    print(' x kazandi')
                    quit()
                if i.count('o') == 3:
                    print('o  kazandi')
                    quit()

            # beraberlik durumu
            a = []
            for i in tahta:
                for j in i:
                    a.append(j)
                    if a.count('x') == 4 and a.count('o') == 5 or a.count('x') == 5 and a.count('o') == 4:
                        print('>>>...oyun berabere')
                        quit()
            sira += 1
            x_o.append(cvp)

        else:
            print('>>>...orasi dolu...baska hamle seciniz...<<<')
    elif isaret == 'O':
        cvp = input('\n1-9 arasinda bir yer giriniz :')
        if cvp not in x_o:
            # tahtaya hamle yazdirma
            if cvp == '1':
                tahta[0][0] = 'o'
            elif cvp == '2':
                tahta[0][1] = 'o'
            elif cvp == '3':
                tahta[0][2] = 'o'
            elif cvp == '4':
                tahta[1][0] = 'o'
            elif cvp == '5':
                tahta[1][1] = 'o'
            elif cvp == '6':
                tahta[1][2] = 'o'
            elif cvp == '7':
                tahta[2][0] = 'o'
            elif cvp == '8':
                tahta[2][1] = 'o'
            elif cvp == '9':
                tahta[2][2] = 'o'
            oyun_tahtasi()

            # kazanma durumunu kontrol et
            for i in tahta[0], tahta[1], tahta[2], \
                     [tahta[0][0], tahta[1][0], tahta[2][0]], \
                     [tahta[0][1], tahta[1][1], tahta[2][1]], \
                     [tahta[0][2], tahta[1][2], tahta[2][2]], \
                     [tahta[0][0], tahta[1][1], tahta[2][2]], \
                     [tahta[0][2], tahta[1][1], tahta[2][0]]:
                if i.count('x') == 3:
                    print(' x kazandi')
                    quit()
                if i.count('o') == 3:
                    print('o  kazandi')
                    quit()
            # beraberlik durumu
            a = []
            for i in tahta:
                for j in i:
                    a.append(j)
                    if a.count('x') == 4 and a.count('o') == 5 or a.count('x') == 5 and a.count('o') == 4:
                        print('>>>...oyun berabere')
                        quit()
            sira += 1
            x_o.append(cvp)
        else:
            print('>>>...orasi dolu...baska hamle seciniz...<<<')