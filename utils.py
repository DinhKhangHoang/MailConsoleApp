from typing import List
import re

def isSameListByElement(a: List, b: List) -> bool:
  length = len(a)
  return len(a) == len(b) and len([i for i, j in zip(a, b) if i == j]) == length

regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def checkValidMail(mail: str) -> bool:
  if mail is None:
    return False
  return re.fullmatch(regex_email, mail)