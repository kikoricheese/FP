import os
import time

os.system('cls')
bulan = lambda x : x // 30 
tahun = lambda x : x // 365         #hari                bulan                  #tahun
full_convert_date = lambda x : ((x-tahun(x)*365)- ((x-tahun(x)*365)//30)*30, (x-tahun(x)*365)// 30 ,tahun(x))

def tabel():
    print("============================")
    print("====PROGRAM KONVERSI HARI===")
    print("============================")
    print("| 1. Hari ke Tahun         |")
    print("| 2. Hari ke Bulan         |")
    print("| 3. Hari ke Tahun & Bulan |")
    print("============================")

def menuConvert():
    tabel()
    menuFn = True
    while menuFn is not None:
        hari = hariInp()
        menuFn =choice()
        menuFn(hari)
        time.sleep(5)
        os.system('cls')
        tabel()

def menu1(hari):
    print(f'Perubahan {hari} Hari ke tahun adalah {tahun(hari)} tahun')
    
def menu2(hari):
    print(f'Perubahan {hari} Hari ke bulan adalah {bulan(hari)} bulan')

def menu3(hari):
    temp = full_convert_date(hari)
    print(f'Perubahan {hari} Hari ke tanggal adalah {temp[2]} tahun, {temp[1]} bulan, {temp[0]} hari' )

def hariInp():
    inp = input("Masukan hari :")
    return int(inp) if inp.isdigit() else 0

def choice()->int:
    inp = input("Masukan No menu :")
    i = int(inp) if inp.isdigit() else 4
    return menu1 if i==1 else menu2 if i ==2 else menu3 if i ==3 else doNothing

def doNothing(_):
    print("Masukan tidak valid")

def display():
    menuConvert()

if __name__ == '__main__':
    display()