print ("Python: Create You Own QR Code")

import qrcode

img = qrcode.make("https://www.linkedin.com/in/subhash-yada-b239652a1/")
img.save("E:\\Subhash\\GitHub_Repository\\Python-Projects\\Python_Misc\\my_linkedin_qrcode.png")
