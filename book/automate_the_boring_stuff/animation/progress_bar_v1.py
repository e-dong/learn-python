import time
import sys

progress = ""
max = 51

for i in range(max): 
  sys.stdout.write('\033[2k')
  part = i + 1
  progress += "="
  remaining_space = max - part
  time.sleep(0.1)
  perc_str = "{:.2f}".format(round((part/max) * 100, 2))
  frac_str = f"({str(part)}/{max})"
  bar_str = "[" + progress + ">" +  f"{remaining_space * ' '}]"
 
  print("\r", "{0:>6} {1}{2}".format(perc_str, frac_str, bar_str), end="")

