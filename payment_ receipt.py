from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from datetime import datetime,date

Customer_name=input("Enter customer name: ")
List_of_Items = {"Milk":40,"Juice":100,"Chips":30,"Biscuits":20,"Cold Drinks":60,"Chocolates":25}
print("Items Available are :")
for item,price in List_of_Items.items():
    print(f"{item}: ₹{price} ")
Bought_Items={}
while True:
    Choice=input("Enter item name to be bought OR No to complete order : ")
    if Choice=="No" or Choice=="no":
        break
    if Choice in List_of_Items:
        Bought_Items[Choice]=List_of_Items[Choice]
    else:
        print("This Item not available")

#PDF Creation will begin here
file="store_payment_receipt.pdf"  
now=datetime.now()              
date_today=date.today()
time=now.strftime("%H:%M:%S")
r=canvas.Canvas(file, pagesize=letter)
company_logo_path = "logo.jpg"
r.drawImage(company_logo_path, 50, 600, width=150, height=150)
r.drawString(250, 750, "SK STORE")
r.drawString(250, 730, "Ahemdabad,Gujarat,India")
r.drawString(250, 710, "Phone: 123-456-7890")
r.drawString(250, 690, f"Date: {date_today}")
r.drawString(250, 670, f"Time: {time}")
r.drawString(250, 650, f"Customer Name: {Customer_name}")
r.drawString(5, 630,"-"*150)

r.drawString(250, 610, "PAYMENT RECEIPT")
r.drawString(250, 610, "_________________")
y=590
for item,price in Bought_Items.items():
    r.drawString(100,y,f"{item}: Rs. {price}")
    y-=20
Total=sum(Bought_Items.values())
r.drawString(100,y-20,"*"*50)
r.drawString(100,y-40,f"Total Amount : Rs. {Total}")

#QR code will be created below
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
qr.add_data=(f"Payment Receipt for {Customer_name}\nItems: {Bought_Items.items()}")
qr.make(fit=True)
qr_img=qr.make_image(fill_color="black", back_color="white")
qr_img_path="qr_code.png"
qr_img.save(qr_img_path)
r.drawImage(qr_img_path, 250, 400, width=100, height=100)


r.drawString(50, 350, "Thank you for shopping with us!")
r.save()
print(f"PDF of Payment Receipt is : {file}")