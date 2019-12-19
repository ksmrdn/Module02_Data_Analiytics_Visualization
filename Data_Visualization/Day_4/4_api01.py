import requests
print("Selamat Datang")
print("Silahkan pilih konversi yang akan anda lakukan: ")
print("(1) IDR Indonesia => USD US\n(2) USD US => IDR ID\n(3) USD US => Bitcoin")
optional = input("Pilihin Anda (1/2/3): ") #str
kode = input('Ketik nama Bank: ')
url = 'https://kurs.web.id/api/v1/'
data = requests.get(url+kode)
bank = data.json()
buy =  data.json()['beli']
print(bank)

def opsi(apa):
    if apa == '1':
        uang = int(input('Ketik nominal rupiah: Rp.'))
        konversi1 = uang/int(buy)
        print(f"Hasil konversi ID Rp.{uang} adalah US ${konversi1}")
    elif apa == '2':
        money = int(input('Ketik nominal dollar: US $'))
        konversi2 = int(money*int(buy))
        print(f"Hasil konversi US ${money} adalah ID Rp.{konversi2}")
    elif apa == '3':
        money0 = int(input('Ketik nominal dollar: US $'))
        url0 = 'https://blockchain.info/tobtc?currency=USD&value='
        data0 = requests.get(url0+money0)
        # print(type(data0))
        # cur = data0.text()
        # print(type(cur))
        cur = 0.0001186
        konversi3 = money0*cur
        print(f"Hasil konversi US${money0} adalah Bitcoin {konversi3}")
    else:
        print("ERROR")
opsi(optional)

def usd2bitcoin(apa):
    money0 = int(input('Ketik nominal dollar: US $'))
    url1 = 'https://blockchain.info/tobtc?currency=USD&value='
    data1 = requests.get(url1+money0)
    bit = data1.json()


# for current in bank:
#     print(current)
#     konversi = current['jual']
#       print(f'Total rupiah: {current['jual']}')
