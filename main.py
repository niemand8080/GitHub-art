import asyncio
import os
import subprocess as sp
import sys
from dotenv import load_dotenv # type: ignore

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_EMAIL = os.getenv('GITHUB_EMAIL')

async def main():
  print(f"username: {GITHUB_USERNAME}\nemail   : {GITHUB_EMAIL}")
  sp.run(['git', 'config', 'user.name', GITHUB_USERNAME], text=True)
  sp.run(['git', 'config', 'user.email', GITHUB_EMAIL], text=True)

if __name__ == "__main__":
  # Get current email and username
  result_name = sp.run(['git', 'config', 'user.name'], text=True, capture_output=True)
  result_email = sp.run(['git', 'config', 'user.email'], text=True, capture_output=True)
  name = result_name.stdout.strip()
  email = result_email.stdout.strip()

  if GITHUB_EMAIL is None or GITHUB_USERNAME is None:
    sys.exit()
  
  asyncio.run(main())

  # set current email and username
  sp.run(['git', 'config', 'user.name', name], text=True)
  sp.run(['git', 'config', 'user.email', email], text=True)