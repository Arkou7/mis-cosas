import os

import requests

url = "https://github.com/Hamy-os/computer-outro/raw/main/outro.mp3"

response = requests.get(url)
opc = open("outro.mp3","wb")



count = 0

while (count < 100000):    

    count = count + 1

    print("troleado puto")
