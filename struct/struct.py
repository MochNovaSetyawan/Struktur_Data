def Mahasiswa(name, age, address):
    return {"name" : name, "age" : age, "address" : address}

mhs = Mahasiswa(
    name= "John lenon",
    age= 20,
    address= "Kabupaten Tangerang"
)

print("Name : ", mhs['name'])
print("age : ", mhs['age'])
print("address : ", mhs['address'])