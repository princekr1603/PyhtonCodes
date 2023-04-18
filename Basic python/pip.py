import qrcode
import img
qr=qrcode.QRCode(version=15,box_size=10,border=5) #version upto 1 to 40
#version increases then complexity increases
data="""
name:prince kumar
age:20
D.O.P:16/03/2003
vill:eakemba gaya (Bihar)
12th marks:384 (BSEB),2022
10th marks:364 (CBSE),2018
"""
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("test.png")
