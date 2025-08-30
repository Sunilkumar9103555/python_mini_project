import qrcode
#Taking upi id 
upi_id=input("Enter the UPI Id=")
#upi://pay?pa=u.....(pa means paramater the take input from the user)
#Defineing the url based on the upi id and the payment app 
#you can modify these urls based on the payment apps you want to support 
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytem_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create Qr codes for the each paytem app
phonepe_qr=qrcode.make(phonepe_url)
paytem_qr=qrcode.make(paytem_url)
google_pay_qr=qrcode.make(google_pay_url)

#save thew qr code to image file 
phonepe_qr.save('phone_qr.png')
paytem_qr.save('paytem_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the qr codes (you may need to install pil/pillow library)
phonepe_qr.show()
paytem_qr.get_image()
google_pay_qr.get_image()




