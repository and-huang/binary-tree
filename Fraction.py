from Binary_Search_Tree import Binary_Search_Tree

class Fraction:

  def __init__(self, numerator, denominator):
    # In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)


  def __lt__(self, other):
    num1 = self.__n * other.__d
    num2 = other.__n * self.__d
    return num1 < num2
    

  def __gt__(self, other):
    num1 = self.__n * other.__d
    num2 = other.__n * self.__d
    return num1 > num2


  def __eq__(self, other):
    num1 = self.__n * other.__d
    num2 = other.__n * self.__d
    return num1 == num2 


  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  # testTree = Binary_Search_Tree()
  # a = Fraction(4, 5)
  # b = Fraction(4, 10)
  # c = Fraction(4, 11)
  # d = Fraction(9, 10)
  # e = Fraction(112, 190)
  # f = Fraction(40, 210)
  # g = Fraction(67, 101)
  # h = Fraction(49, 51)
  # fractionList = []
  # fractionList.extend((a,b,c,d,e,f,g,h))
  # for i in fractionList:
  #   testTree.insert_element(i)
  # print("This is the original array: \n", fractionList)
  # print("This is the in-order traversal: \n", testTree.to_list())
  pass

