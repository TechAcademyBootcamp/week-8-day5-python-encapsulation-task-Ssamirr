class Author():

  def __init__(self,name,email,gender):
    self.__name = name
    self.__email = email
    self.__gender = gender
  
  @property
  def name(self):
    return self.__name

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self,newEmail):
    self.__email = newEmail
  
  @property
  def gender(self):
    return self.__gender
  
  def toString(self):
    return f"Author[name={self.__name},email={self.__email},gender={self.__gender}]"

author = Author("Tan Ah Teck","ahTeck@somewhere.com","m")

class Book(Author):

  def __init__(self,name_book,author,price,qty):
    self.__bookName = name_book
    self.__price = price
    self.__qty = qty

  @property
  def name(self):
    return self.__bookName

  @property
  def author(self):
    return author.name

  @property
  def Price(self):
    return self.__price
  
  @Price.setter
  def Price(self,newPrice):
    self.__price = newPrice

  @property
  def Qty(self):
    return self.__qty

  @Qty.setter
  def Qty(self,newQty):
    self.__qty = newQty

  def toString(self):
    return f"Book[name={self.__bookName},Author[name={author.name},email={author.email},gender={author.gender},price={self.__price},qty={self.__qty}]"

book = Book("Tan",author,2.5,3)
print(book.toString())