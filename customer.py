from typing import List


class Customer:
  def __init__(self, title: str, first_name: str, last_name: str, email: str):
    self.title = title
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    pass
  
  def __eq__(self, o: object) -> bool:
    return self.email == o.email \
    and self.first_name == o.first_name \
    and self.last_name == o.last_name \
    and self.title == o.title

class WrongCustomer:
  def __init__(self, info: List[str]):
    self.info = info
  
  def __eq__(self, o: object) -> bool:
    return self.info == o.info