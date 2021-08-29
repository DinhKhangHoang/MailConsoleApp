from template import MailTemplate
from customer import Customer
import datetime
class Mail:
  def __init__(self, template: MailTemplate, customer: Customer):
    self.template = template
    self.customer = customer
    pass

  def encode(self):
    pass

class JsonMail(Mail):
  def encode(self):
    body = self.template.body.replace("{{TITLE}}", self.customer.title) \
    .replace("{{FIRST_NAME}}", self.customer.first_name) \
    .replace("{{LAST_NAME}}", self.customer.last_name) \
    .replace('{{TODAY}}', datetime.datetime.now().strftime("%d %b %Y"))

    json = {
      "from": self.template.sender,
      "subject": self.template.subject,
      "mimeType": self.template.mime_type,
      "to": self.customer.email,
      "body": body
    }
    return json
