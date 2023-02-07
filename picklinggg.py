import pickle

# Pickling a python object

# cars = ["Audi", "BMW", "Lambogini", "Tesla car"]
# # file = "mycars.pkl"
# file = "mycars.txt"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()

# fil = "mycars.pkl"
fil = "mycars.txt"
fileob = open(fil, "rb")
cer = pickle.load(fileob)
print(cer)
fileob.close()
print(type(cer))
