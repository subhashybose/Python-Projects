print ("Python: Create You Own QR Code")

import qrcode

img = qrcode.make("https://github.com/subhashybose")
img.save("E:\\Subhash\\GitHub_Repository\\Python-Projects\\Python_Misc\\my_github_qrcode.png")
