from customer import WrongCustomer
from typing import List, Tuple
from mail import JsonMail, Mail
from customer_reader import CustomerReader
from template_reader import MailTemplateReader

class MailCreator:
  def __init__(self, mail_template_reader: MailTemplateReader, customer_reader: CustomerReader):
    self.mail_template_reader = mail_template_reader
    self.customer_reader = customer_reader
  
  def create_mails(self, template_mail_path: str, customer_path: str) -> Tuple[List[Mail], List[WrongCustomer]]:
    pass

class JsonMailCreator(MailCreator):

  def create_mails(self, template_mail_path: str, customer_path: str) -> Tuple[List[Mail], List[WrongCustomer]]:
    (customers, wrong_customers) = self.customer_reader.read(customer_path)
    template = self.mail_template_reader.read(template_mail_path)
    mails = list(map(lambda receiver: JsonMail(template= template, customer=receiver), customers))
    return (mails, wrong_customers)
    