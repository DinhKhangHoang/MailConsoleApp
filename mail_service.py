from mail_sender import MailSender
from mail_creator import MailCreator

class MailService:
  def __init__(self, mail_creator: MailCreator, mail_sender: MailSender):
    self.mail_creator = mail_creator
    self.mail_sender = mail_sender
  pass

  def send(self, template_mail_path: str, customer_path: str, error_path: str):
    (mails, wrong_customers) = self.mail_creator.create_mails(template_mail_path, customer_path)
  
    success_receivers = self.mail_sender.send(mails)
    if len(success_receivers) > 0:
      print("Sent successfully to\n" + "\n".join(success_receivers))
    else:
      print("No mails have been sent!")
    
    if len(wrong_customers) > 0:
      self.mail_creator.customer_reader.writeWrongCustomers(error_path, wrong_customers)
    pass
