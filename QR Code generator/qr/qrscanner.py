import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


myqr1=qrcode.make('https://chatgpt.com/')
myqr2=qrcode.make('https://www.w3schools.com/python/default.asp')
myqr3=qrcode.make('https://www.youtube.com/')
myqr4=qrcode.make('https://www.indiabix.com/')
myqr5=qrcode.make('https://www.youtube.com/@freecodecamp')


myqr1.save("myqr1.png",scale=6)
myqr2.save("myqr2.png",scale=8)
myqr3.save("myqr3.png",scale=10)
myqr4.save("myqr4.png",scale=12)
myqr5.save("myqr5.png",scale=9)


a=decode(Image.open('myqr1.png'))
print(a[0].data.decode('ascii'))
b=decode(Image.open('myqr2.png'))
print(b[0].data.decode('ascii'))
c=decode(Image.open('myqr3.png'))
print(c[0].data.decode('ascii'))



