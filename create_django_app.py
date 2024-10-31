# -*- coding: utf-8 -*-
import os
import subprocess
import sys

# Create new folder myapp
os.makedirs("myapp", exist_ok=True)

# Create  "myapp/.venv"
subprocess.run([sys.executable, "-m", "venv", "myapp/.venv"])

