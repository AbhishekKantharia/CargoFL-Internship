# Import qrcode module using the import keyword.
import qrcode
# Pass the version and box size as the arguments to the QRCode() function
# and store it in a variable.
our_QRcode = qrcode.QRCode(version=1, box_size=15)
# Add data to the above QRcode using the add_data() function by passing some
# random string as an argument.
our_QRcode.add_data('generating our own qr code')
# Get or build the QRcode using the make() function.
our_QRcode.make()
# Convert the QRcode into an image using the make_image() function by passing
# some random fill color and background colors as the arguments to it.
# store it in another variable.
rslt_imge = our_QRcode.make_image(fill_color="green", back_color="yellow")
# Save the above image with some random name using the save() function
rslt_imge.save('myqrcode_2.png')