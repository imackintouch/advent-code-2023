#!/usr/local/bin/python3.12
import sys
import click
import re

def decode_calibration(code: str) -> int:
  m = re.findall(r"\d", code)
  return int(m[0] + m[len(m)-1])

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
