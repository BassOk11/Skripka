name = input("имя ")   # где имя "Mars"
year_of_birth  = int(input("Год вашего рождения "))   # где год рождения 1977
mi_dikt = {"имя ":name,"Год рождения ":year_of_birth}
print(mi_dikt)
print(mi_dikt.get("имя "))
print(mi_dikt.get('', 678))
cena = mi_dikt['price1'] = 300
cena_2 = mi_dikt['price2'] = 350
print(mi_dikt.pop("price1"))
print(mi_dikt)

mi_set = {name,year_of_birth,cena,cena_2,"Mars",1977}  # значения "Mars",1977" повторяющиеся
print(mi_set)








