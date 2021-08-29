class CsvIOException(Exception):
  def __init__(self, type: int, message: str) -> None:
    self.msg = message
    self.type = type

class JsonIOException(Exception):
  def __init__(self, type: str, message: str) -> None:
    self.msg = message
    self.type = type