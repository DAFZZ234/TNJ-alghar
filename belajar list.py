# list with int as element's data type
list_1 = [2, 4, 8, 10]

# list with str as element's data type
list_2 = ["gojek", "gojek", "tin", "duar"]

# list with various data type in the element
list_3 = [21, False, "hello pythoon"]

print(list_2)

print(list_1[2])

print(list_2[3])

print(list_3[0])

list_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

print(list_hari[2])

print("hari ini hari",list_hari[5])

Nama_depan = "marimar"

nama_belakang = "juniot"

agama = "mboten ngertos"

umur = 34

accept = False

profil = [Nama_depan, nama_belakang, umur, accept]

profil.append(agama)

print(profil)

buah = ["mangga", "pisang", "jeruk", "anggur"]

buah[0] = "durian"

buah[2] = "manggis"

print(buah)

print(len(buah))

buah.append("apel")

print(buah)

print(buah[4])

buah.remove("pisang")

print(buah)
