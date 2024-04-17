#!/usr/bin/env python3
from models.base_model import BaseModel
from models import storage
base1 = BaseModel()
base1_dic = base1.to_dict()
dic = {'name':"California"}
dic.update(base1_dic)
base = BaseModel(**dic)
base.save()
#print(base)
print(base.__dict__)
base.delete()
print(storage.all())
