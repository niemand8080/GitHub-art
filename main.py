import os
import subprocess as sp

def main():
  print("Cle")
  sp.run(['git', 'status'], text=True, capture_output=True)

if __name__ == "__main__":
  main()