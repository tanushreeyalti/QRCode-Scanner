import qrcode

features = qrcode.QRCode(version=1,box_size=70,border=3)

features.add_data('https://www.youtube.com/c/ACMStudentChapterVideos')
features.make(fit=True)
generate_image = features.make_image(fill_color="blue",back_color="white")
generate_image.save('image4.png')
