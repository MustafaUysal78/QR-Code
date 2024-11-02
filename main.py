import pyqrcode

url = input("Enter url: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', 8)