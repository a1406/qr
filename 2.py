from PIL import Image
import zbarlight
file_path = 'my.png'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()
codes = zbarlight.scan_codes('qrcode', image)
codes2 = str(codes[0], encoding="utf-8")
print('QR codes: %s' % codes2)

with open('result', 'wb') as f:
    f.write(codes[0])

