#!/usr/local/bin/python3.12
import sys
import click
import regex as re

def decode_calibration(code: str) -> int:
  digits_as_text = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
  }

  #ToDo: For my own benefit, work out a positive lookahead expression that would work without overlapped=True
  digits_text_pattern = "|".join(digits_as_text.keys()) + r"|\d"
  m = re.findall(digits_text_pattern, code, overlapped=True)

  first, last = (m[0], m[len(m)-1])
  first = digits_as_text[first] if len(first) > 1 else first
  last = digits_as_text[last] if len(last) > 1 else last
  return int(first + last)

def calibrate(file_path: str) -> int:
  with open(file_path, "r") as f:
    coded_calibrations = f.readlines()

  calibration_sum = 0
  for coded_calibration in coded_calibrations:
    calibration = decode_calibration(coded_calibration)
    print(f"Calibration value for {coded_calibration.rstrip()} is: {calibration}" )
    calibration_sum += calibration

  print(f"Calibration sum of {file_path} is: {calibration_sum}")

  return calibration_sum

@click.command()
@click.option("-f", "--file", type=str, default="calibration-data.txt", help="path of calibrations file")
def main(file):
  calibrate(file)
  
if __name__ == '__main__':
  sys.exit(main())
