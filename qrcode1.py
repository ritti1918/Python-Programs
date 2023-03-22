import qrcode  
data='Hello! Welcome to the World of Python😂'
img=qrcode.make(data)
img.save('qrcode1.png')