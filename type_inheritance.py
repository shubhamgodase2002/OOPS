# types of inheritance

# 1 single label inheritance

class Phone:
  def __init__(self,price,brand,camera):
    print('Inside phoen constructor')
    self.__price=price
    self.brand=brand
    self.camera=camera

  def buy(self):
    print('Buying a phone')

  def return_phone(self):
    print('Returning a phone')

class SmartPhone(Phone):
  pass

SmartPhone(1000,'Apple','13px').buy()

# 2 example of multilevel heritance

class Product:
  def review(self):
    print('Product customeer review')  

class Phone(Product):
  def __init__(self,price,brand,camera):
    print('Inside phone constructor')

    self._price=price
    self.brand=brand
    self.camera=camera

  def buy(self):
    print('buying a phone ')

class SmartPhone(Phone):
    pass

s=SmartPhone(20000,'Apple',12)
p=Phone(1000,'Samsung',1)

s.buy()
s.review()
p.review()



# 2 example of hyrachical heritance


class Phone:
  def __init__(self,price,brand,camera):
    print('Inside phone constructor ')
    self.__price=price
    self.brand=brand
    self.camera=camera

  def buy(self):
   print('buying a phone')

  def return_phone(self):
    print('returiing the phone')

class SmartPhone(Phone):
  pass

class FeaturePhone(Phone):
  pass

SmartPhone(1000,'Apple','13px').buy()



# 3  example of multiple inheritance

class Phone:
  def __init__(self,price,brand,camera):
    print('Inside phone constructor')
    self.__price=price
    self.brand=brand
    self.camera=camera

  def buy(self):
    print('Buying a phone')

  def return_phone(self):
    print('returning a phone')


class Product:
  def review(self):
    print('Customer review')

class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000,'apple',12)

s.buy()
s.review()




# 4 MRO example  method resolution order 


class Phone:
  def __init__(self,price,brand,camera):
    print('Inside phone constructor')
    self.__price=price
    self.brand=brand
    self.camera=camera

  def buy(self):
    print('Buying a phone')

  def return_phone(self):
    print('returning a phone')


class Product:
  def buy(self):
    print('product by method')

class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000,'apple',12)
s.buy()




##  5 multi level inheritance


class A:

  def m1(self):
    return 20

class B(A):

  def m1(self):
    return 30

  def m2(self):
    return 40

class C(B):

  def m2(self):
    return 20

obj1=A()
obj2=B()
obj3=C()

print(obj1.m1() + obj3.m1() + obj3.m2())


##  5 multi level inheritance  2nd example this code error becaus eshow the recursive code  run 


class A:

  def m1(self):
    return 20

class B(A):

  def m1(self):
    val=super().m1()+30
    return val

  

class C(B):

  def m1(self):
    val=self.m1()+20
    return val


obj=C()

print(obj1.m1())
































      \
        
