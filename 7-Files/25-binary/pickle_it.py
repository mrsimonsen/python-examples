# Pickle It
# Demonstrates pickling and shelving data

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
with open("pickles1.dat", "wb") as file:
	pickle.dump(variety, file)
	pickle.dump(shape, file)
	pickle.dump(brand, file)

print("\nUnpickling lists.")
with open("pickles1.dat", "rb") as file:
	variety = pickle.load(file)
	shape = pickle.load(file)
	brand = pickle.load(file)
print(variety)
print(shape)
print(brand)

print("\nShelving lists.")
s = shelve.open("pickles2.bin")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()    # make sure data is written

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()

