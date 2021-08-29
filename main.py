#!/usr/bin/python3
from mail_service import MailService
from mail_sender import JsonMailSender
from customer_reader import CsvCustomerReader
from template_reader import JsonMailTemplateReader
from mail_creator import JsonMailCreator
import os.path
import sys, getopt
from typing import List, Tuple

def validateArguments(argv: List[str]) -> Tuple[str, str, str, str]:
  template_file= ''
  customer_file= ''
  output_path= ''
  error= ''
  try:
    opts, args = getopt.getopt(argv,"ht:c:o:e:",["template=","customer=", "outputpath=", "error="])
  except getopt.GetoptError:
    print ('main.py -t <templatefile> -c <customersfile> -o <outputemail> -e <error>')
    sys.exit(2)
  
  for opt, arg in opts:
    if opt in ('-h', "--help"):
      print ('main.py -t <templatefile> -c <customersfile> -o <outputemail> -e <error>')
      sys.exit()
    elif opt in ("-t", "--template"):
      template_file = arg
    elif opt in ("-c", "--customer"):
      customer_file = arg
    elif opt in ("-o", "--outputpath"):
      output_path = arg
    elif opt in ("-e", "--error"):
      error = arg
  if not os.path.isfile(template_file):
    sys.exit('Cannot find file ' + template_file)
  if not os.path.isfile(customer_file):
    sys.exit('Cannot find file ' + customer_file)
  if not os.path.isdir(output_path):
    sys.exit('Cannot find directory ' + output_path)
  if not os.path.isfile(error):
    sys.exit('Cannot find file ' + error)
    
  return (template_file, customer_file, output_path, error)
  

def main(argv: List[str]):
  (template_file, customer_file, output_path, error) = validateArguments(argv)
  mail_creator = JsonMailCreator(JsonMailTemplateReader(), CsvCustomerReader(formats=["TITLE","FIRST_NAME","LAST_NAME","EMAIL"]))
  mail_sender = JsonMailSender({"output_path": output_path})
  mail_service = MailService(mail_creator, mail_sender)
  mail_service.send(template_file, customer_file, error)

if __name__ == "__main__":
   main(sys.argv[1:])