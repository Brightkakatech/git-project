import qrcode

def generate_qr_code(data, filename):
    # Create an instance of QRCode
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls error correction
        box_size=20,  # size of each box (or pixel)
        border=5,  # thickness of the border (default is 4)
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image from the QR code
    img = qr.make_image(fill='blue', back_color='white')

    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage:
data = "altlantisconstructum.com"  # Replace with your data or URL
filename = "qr_code_example.png"
generate_qr_code(data, filename)
