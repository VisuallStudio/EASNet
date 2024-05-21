import time

import math
import random

import torch
import torchvision.models

# import torch.nn
#
#
# class CUNET(torch.nn.Module):
#     def __init__(self):
#         super(CUNET, self).__init__()
#         self.conv1=torch.nn.Conv2d(3,1,3,1,1)
#     def forward(self):
#         x = 'rewrqe'
#         print('begin')
#
#         print('end')
#     def f(self):
#         print(self)
# model=CUNET()
# model.f()
# class Fadnet():
#     def __init__(self):
#         super(Fadnet, self).__init__()
#         self.cunet = CUNET()
#
#         self.forward()
#
#     def forward(self):
#         self.cunet.forward(self.feature_extraction)
#
#     def feature_extraction(self, x):
#         print('i am FADNET featurn_extraction' + x)
#
#
# class OFAFADNET(Fadnet):
#     def __init__(self):
#         self.kiss = True
#         super(OFAFADNET, self).__init__()
#
#     def feature_extraction(self, x):
#         print(self.kiss)
#         print('i am ofafadnet' + x)


# net = OFAFADNET()
# def add(x,y):
#     a=4
#     return a+x+y
# def mul(func ,x,y, z):
#     res=func(x,y)
#     return res*z
#
# x=4
# y=4
# z=1
# print(mul(add,x,y,z))

# a=torch.randn(2,2)
# b=torch.randn(2,2)
# print(a)
# print(b)
#
# c=torch.cat((a,b),dim=1)
# print(c)
# print(c.shape)
# list=[1,2,3]
# validate_func_dict = {
#                           'ks_list': sorted({min(list), max(list)}),
#                           }
# print(validate_func_dict)

# subnet_settings = []
# ds = [4, 2, 2]
# es = [8, 8, 2]
# ks = [7, 7, 3]
# ss = [4, 2, 2]
# img_size = 224
# w = 0
# for d, e, k, s in zip(ds, es, ks, ss):
#     subnet_settings.append([{
#         'image_size': img_size,
#         'd': d,
#         'e': e,
#         'ks': k,
#         's': s,
#         'w': w,
#         }, 'R%s-D%s-E%s-K%s-S%s-W%s' % (img_size, d, e, k, s, w)])
# for setting, name in subnet_settings:
#     print(setting)
#     print(name)
# x=torch.randn(1,1,24,48)
# conv=torch.nn.Conv2d(1,1,3,2,1)
# y=conv(x)
# print(y.size())
# deconv=torch.nn.ConvTranspose2d(1,1,4,2,1)
# z=deconv(y)
# print(z.size())
# list=[]
# print(list==None)
# print(list==[])
# print()

# class People():
#     def __init__(self):
#         super(People, self).__init__()
#
#     def info(self, func):
#         x = 1
#         print("Poeple")
#         func(x)
#
#
# class Animal():
#     def __init__(self):
#         super(Animal, self).__init__()
#         self.age = 55
#
#     def info(self, x):
#         print("Animal={}+{}".format(self.age, x))
#
#
# a = Animal()
# p = People()
# # a.info()
# p.info(a.info)
# print(3%1)

# ks_list = [[2,2,2],[2,2,2]]
# print(ks_list)
# print(max(ks_list))
# c=ks_list.copy()
# print(c)


# x=torch.randn(2,2,2,2)
# print(x)
# importance=torch.sum(torch.abs(x),dim=(0,2,3))
# print(importance)

# x=torch.tensor(((3,2),(3,4)))
# y=torch.tensor(((1,2),(2,4)))
# print(x)
# print(y)
# print(x[:,:]*y)

# print(1e6)
# ks = [3, 4, 6, 3, 4, 5, 2, 1, 3, 3, 4, 1]
# ds = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
# es = [2, 4, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# cunet_ks = [1, 2, 3, 4, 5, 6, 7, 8]
# cunet_ds = [4, 4, 4, 4, 4, 4, 4, 4]
# cunet_es = [2, 3, 4, 5, 6, 7, 8, 9]

# str = '(netconf)'
# ofa_settings = {'ks': ks, 'ds': ds, 'es': es}
# cuent_settings = {'cunet_ks': cunet_ks, 'cunet_ds': cunet_ds, 'cuent_es': cunet_es}
# ofa_settings.update(cuent_settings)
# subsettings=ofa_settings
# for key, val in subsettings.items():
#
#     str = str + ', ' + key + ':{'
#     for ksval in val:
#         str += '{}'.format(ksval)
#     str += "}"
# # print(' {}'.format(str))
# # print(subsettings)
# # print(len(subsettings))
# dict={}
# dict_fad={}
# dict_cuentt={}
# dict['1.24']=subsettings
# # print(dict)
# for key,value in zip(dict.keys(),dict.values()):
#     for key,value in zip(value.keys(),value.values()):
#         print(key)
#         print(value)
        # count=0
        # if count<3:
        #     dict_fad[key]=value
        # else:
        #     dict_cuentt[key]=value
        # count += 1




# for i , name in enumerate(subsettings):
#     print(subsettings[name])

# set=[1,2,3]
# setting=[set for _ in range(5)]
# d=[]
# for i in setting:
#     k=random.choice(i)
#     d.append(k)
# print(d)

# k=torch.randn(2)
# print(k)
# time.sleep(3)
# print(type(k)==torch.Tensor)
# k=[1,2,3,4,5]
# a=random.choice(k)
# print(a)
# b=random.choice(k)
# print(b)
net=torchvision.models.resnet18()
print(net.__class__.__name__)
