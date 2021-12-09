#!/usr/bin/python3
import pickle
f = open("pickled.txt", "wb") #open a txt file called pickled in binary form
new_dict ={"name":"Eliud", "age": 27, "sex": "male", "weight": 95} 
pickle.dump(new_dict, f) #serialize the dict into the open file
f.close


f=open("pickled.txt","rb")
d=pickle.load(f) #load/deserialize from the binary text in the file
print (d)
f.close()