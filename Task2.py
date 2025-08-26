import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=5)

features.add_data('https://www.linkedin.com/in/sayali-more-968a0a33a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') 

generate_image = features.make_image(fill_color="white",back_color="Blue")

generate_image.save('Sayali_Linkedin_Page.png')

