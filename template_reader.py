from exceptions import JsonIOException
import json
from template import MailTemplate

class MailTemplateReader:
  def read(self, filePath: str) -> MailTemplate:
    pass
  pass

class JsonMailTemplateReader(MailTemplateReader):
  def read(self, filePath: str):
    with open(filePath, 'r') as file:
      source = json.load(file)
      source_2_dict = dict(source)
      subject= source_2_dict.get("subject")
      sender= source_2_dict.get("from")
      mime_type=source_2_dict.get("mimeType")
      body=source_2_dict.get("body")
      if subject is None or sender is None or mime_type is None or body is None:
        raise JsonIOException(type= 'in', message= "template have not enough fields")
      template =  MailTemplate(subject = subject, sender= sender, mime_type=mime_type, body=body)
      return template