from exceptions import CsvIOException
from typing import List, Tuple
from customer import Customer, WrongCustomer
import csv
from utils import checkValidMail, isSameListByElement

class CustomerReader:
  def __init__(self, formats: List[str]) -> None:
    self.headers = formats

  def read(self, filePath: str) -> Tuple[List[Customer], List[WrongCustomer]]:
    pass
  
  def writeWrongCustomers(self, filePath: str, customers: List[WrongCustomer]):
    pass
  pass

class CsvCustomerReader(CustomerReader):
  def read(self, filePath: str) -> Tuple[List[Customer], List[WrongCustomer]]:
    rows = []
    source_headers = []
    with open(filePath, 'r') as csv_source:
      csvreader = csv.reader(csv_source)
      data_lst = list(csvreader)
      if len(data_lst) <= 0:
        raise CsvIOException(1, "customer_template empty file")
      source_headers = data_lst[0]
      if not isSameListByElement(source_headers, self.headers):
        raise CsvIOException(2, 'customer_template wrong headers')
      for row in data_lst[1:]:
        rows.append(row)
    
    customers = []
    wrong_customers = []

    for row in rows:
      if len(row) < len(self.headers) or not checkValidMail(row[3]):
        wrong_customers.append(WrongCustomer(row))
      else:
        customers.append(Customer(title=row[0], first_name=row[1], last_name=row[2], email=row[3]))
    return (customers, wrong_customers)

  def writeWrongCustomers(self, filePath: str, customers: List[WrongCustomer]):
    lst = list(map(lambda customer: customer.info, customers))
    with open(filePath, 'a', encoding="UTF8", newline='') as f:
      writer = csv.writer(f)
      writer.writerows(lst)
    print('Customers with wrong email were saved in ' + filePath)
