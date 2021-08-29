from template import MailTemplate
from template_reader import JsonMailTemplateReader
from customer import Customer, WrongCustomer
from exceptions import CsvIOException, JsonIOException
from customer_reader import CsvCustomerReader
import unittest

class Test(unittest.TestCase):

  '''#**************************
  ## TEST CUSTOMER READER
  #**************************'''
  def test_customer_reader_wrong_path_file(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    with self.assertRaises(FileNotFoundError) as ex:
      (customers, wrong_customers) = customer_reader.read("./customers/empty.csv")
    self.assertEqual(ex.exception.filename, "./customers/empty.csv")

  def test_customer_reader_empty_csv(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    with self.assertRaises(CsvIOException) as ex:
      (customers, wrong_customers) = customer_reader.read("./testcases/customers/empty.csv")
    self.assertEqual(ex.exception.type, 1)
    
  def test_customer_reader_headers_notenough(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    with self.assertRaises(CsvIOException) as ex:
      (customers, wrong_customers) = customer_reader.read("./testcases/customers/headers_not_enough.csv")
    self.assertEqual(ex.exception.type, 2)

  def test_customer_reader_headers_wrongname_1_line(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    with self.assertRaises(CsvIOException) as ex:
      (customers, wrong_customers) = customer_reader.read("./testcases/customers/headers_wrong_name.csv")
    self.assertEqual(ex.exception.type, 2)

  def test_customer_reader_headers_wrongname_3_line(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    with self.assertRaises(CsvIOException) as ex:
      (customers, wrong_customers) = customer_reader.read("./testcases/customers/headers_wrong_name_3_line.csv")
    self.assertEqual(ex.exception.type, 2)
  
  def test_customer_reader_right_headers_3_line(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    expect = ([Customer(title= "Mr", first_name="Khang", last_name="Hoang", email="khang.hoang@example.com"), \
      Customer(title= "Mrs", first_name="Jung", last_name="Lee", email="jung.lee@example.com")], [])
    (customers, wrong_customers) = customer_reader.read("./testcases/customers/right_header_3_line.csv")
    self.assertListEqual(customers, expect[0])
    self.assertListEqual(wrong_customers, expect[1])

  def test_customer_reader_1_customer_not_email(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    expect = ([Customer(title= "Mrs", first_name="Jung", last_name="Lee", email="jung.lee@example.com")], \
      [WrongCustomer(info=["Mr","Khang","Hoang",""])])
    (customers, wrong_customers) = customer_reader.read("./testcases/customers/not_email_in_1line.csv")
    self.assertListEqual(customers, expect[0])
    self.assertListEqual(wrong_customers, expect[1])

  def test_customer_reader_1_customer_not_email_1_not_first_name(self):
    customer_reader = CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"])
    expect = ([Customer(title= "Mrs", first_name="", last_name="Lee", email="jung.lee@example.com")], \
      [WrongCustomer(info=["Mr","","Hoang",""])])
    (customers, wrong_customers) = customer_reader.read("./testcases/customers/not_email_not_first_name_1line.csv")
    self.assertListEqual(customers, expect[0])
    self.assertListEqual(wrong_customers, expect[1])

  '''#******************
  ##TEST MAIL TEMPLATE READER
  #******************'''
  def test_template_reader_wrong_path_file(self):
    template_reader = JsonMailTemplateReader()
    with self.assertRaises(FileNotFoundError) as ex:
      template = template_reader.read("./template/not_enough_field.json")
    self.assertEqual(ex.exception.filename, "./template/not_enough_field.json")

  def test_template_reader_not_enough_field(self):
    template_reader = JsonMailTemplateReader()
    with self.assertRaises(JsonIOException) as ex:
      template = template_reader.read("./testcases/template/not_enough_field.json")
    self.assertEqual(ex.exception.type, "in")
    
  def test_template_reader_empty_json(self):
    template_reader = JsonMailTemplateReader()
    with self.assertRaises(JsonIOException) as ex:
      template = template_reader.read("./testcases/template/empty.json")
    self.assertEqual(ex.exception.type, "in")

  def test_template_reader_with_field_of_empty_string(self):
    template_reader = JsonMailTemplateReader()
    expect = MailTemplate(subject="Hello from the other side...", sender="The Dev Team<dev@google.com>", body= "", mime_type="text/plain")
    template = template_reader.read("./testcases/template/empty_string_fields.json")
    self.assertEqual(template, expect)

  def test_template_reader_full_field_and_no_empty(self):
    template_reader = JsonMailTemplateReader()
    expect = MailTemplate(subject="Sprint notes", \
      sender="The Dev Team<dev@google.com>", \
      body= "Hi {{TITLE}} {{FIRST_NAME}} {{LAST_NAME}}, \nToday we send you our sprint notes... Sincerely,\n The Marketing Team", \
      mime_type="text/plain")
    template = template_reader.read("./testcases/template/full_field_and_no_empty.json")
    self.assertEqual(template, expect)

  '''#*******************
  ## TEST MAIL CLASS
  #*******************'''

if __name__ == "__main__":
    unittest.main()