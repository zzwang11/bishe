# class c:
#     def __init__(self,aa):
#         self.aa = aa
#
#     def d(self):
#         if self.aa:
#             print(123)
#         else:
#             print(456)
#
#
#
# m = c()
# m.d()

# def a(*aa):
#     if aa == ('aaaaaa',):
#         print(222)
#     print(aa)
#     print(*aa)
#
# a('aaaaaa')

import configparser


def read(*a):
    c = configparser.ConfigParser()
    c.read('e://bishe//config.ini')
    b = c.get(*a)
    print(b)
    print(type(b))

read('test_config','ip')