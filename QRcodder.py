# pip install pyqrcode
# pip install pyfiglet
import pyfiglet
import pyqrcode 
from pyqrcode import QRCode 

text = pyfiglet.figlet_format("QRcodder", font="isometric1")
print(text)

selectURL = input("pleas enter the url: ")
  
# String which represent the QR code 
s = selectURL
  
# Generate QR code 
url = pyqrcode.create(s) 
 
url.svg("QRcodder.svg", scale = 8)
print("Your URL is https://"+selectURL);
print("Pleas check the ' QRcodder.svg ' file")
