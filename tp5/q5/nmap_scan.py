import subprocess
import sys

ip = sys.argv[1]

result = subprocess.run(['nmap','-sS', '-sV', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
      
if result.returncode == 0:
    print(result.stdout)
else:
    print(f"ERROR: {result.stderr}")
