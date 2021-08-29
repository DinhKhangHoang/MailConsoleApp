class MailTemplate:
  def __init__(self, subject: str, sender: str, body: str, mime_type: str):
    self.subject = subject
    self.sender = sender
    self.body = body
    self.mime_type = mime_type
      
  def __eq__(self, o: object):
    return self.subject == o.subject \
      and self.sender == o.sender \
      and self.body == o.body \
      and self.mime_type == o.mime_type
      