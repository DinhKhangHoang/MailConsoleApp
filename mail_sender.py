from typing import List
from mail import Mail
import json

class MailSender:
  def __init__(self, config: dict):
    self.config = config

  def send(self, mails: List[Mail]) -> List[str]:
    pass
  
  def checkConfig(self) -> bool:
    pass
  
class JsonMailSender(MailSender):
  def send(self, mails: List[Mail]) -> List[str]:
    if self.checkConfig() is False:
      raise Exception("sender", "wrong config")
    success_receiver = []
    try:
      for mail in mails:
        with open(self.config.get("output_path") + '/' + mail.customer.email + '.json', 'w') as fh:
          json.dump(mail.encode(), fh, indent=4)
          success_receiver.append(mail.customer.email)
      return success_receiver
    except Exception:
      return success_receiver

  def checkConfig(self) -> bool:
    output_path = self.config.get("output_path")
    if not output_path or type(output_path) is not str:
      print('output_path is empty')
      return False
    return True