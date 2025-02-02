
credit_card=input('credit card anda : ')
# credit_card="2323-2005-7766-3554"
credit_card_split=credit_card.split('-')
credit_card_number=credit_card.replace('-','')

# pengecekan lenght credit card
if len(credit_card_number) > 16:
    print('credit card tidak valid')
    exit()

for angka in credit_card_number:
    try:
        int(angka)
    except ValueError:
        print('credit card tidak valid')
        exit()

def balik_value (value):
    karakter_terbalik=''
    for angka in reversed(value):
        karakter_terbalik = karakter_terbalik + angka
    return karakter_terbalik


def hitung_value (value):
    total=0
    for angka in value:
        total = total + int(angka)
    return total

def ubah_value_genap (value):
    output=''
    for index, angka in enumerate(value):
        # cek bilangan genap
        if (index + 1) % 2 == 0:
            output = output + str(int(angka) * 2)  
        else:
            output = output + angka 
    return output

print(
    balik_value(credit_card_split[0])
    + ' ' +
    balik_value(credit_card_split[1])
)

print(ubah_value_genap( balik_value(credit_card_split[0]) ) 
    + ' ' +
     ubah_value_genap( balik_value(credit_card_split[1]) )
)

print(hitung_value(credit_card_split[0]))
print( hitung_value(credit_card_split[0] + credit_card_split[1] + credit_card_split[2] + credit_card_split[3]) ) 


# print(karakter_terbalik)