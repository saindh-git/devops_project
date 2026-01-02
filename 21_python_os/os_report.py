import os
import sys

print(f"---estate os intelligence report---")
current_location = os.getcwd()
print(f"current estate location:{current_location}")
files=os.listdir('.')
print(f"files found in this romm{files}")
print(f"operating system platform:{sys.platform}")
