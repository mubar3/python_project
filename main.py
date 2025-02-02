
credit_card="2323-2005-7766-3554"
credit_card_split=credit_card.split('-')

print(credit_card_split)

def balik_value (value):
    karakter_terbalik=''
    for angka in reversed(value):
        karakter_terbalik = karakter_terbalik + angka
    return karakter_terbalik

print(balik_value(credit_card_split[0]))
print(balik_value(credit_card_split[1]))



# print(karakter_terbalik)