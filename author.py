class Author():

  def __init__(self,name,email,gender):
    self.__name = name
    self.__email = email
    self.__gender = gender
  
  @property
  def name(self):
    return self.__name

  @property
  def Email(self):
    return self.__email

  @Email.setter
  def Email(newEmail):
    self.__email = newEmail
    return f"New email-{self.__email}"
  
  @property
  def gender(self):
    return self.__gender
  
  def toString(self):
    return f"Author[name={self.__name},email={self.__email},gender={self.__gender}]"
  
author = Author("Tan Ah Teck","ahTeck@somewhere.com","m")
print(author.toString())