#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
<<<<<<< HEAD
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
=======
    print("\t{}: ({}) - {}".format(key,type(my_model_json[key]),my_model_json[key]))
>>>>>>> d371fc684d780557007d78f8471c9a9326f91b59
