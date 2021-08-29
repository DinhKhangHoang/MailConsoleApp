from datetime import datetime

class SpoofDateTime(datetime):
  def __new__(cls, *args, **kwargs):
    return datetime.__new__(datetime, *args, **kwargs)