from PIL import Image

# Opening Image
img = Image.open('image2.png')
pixels = img.load()
width, height = img.size

bytesArray = ""

messageLength = pixels[width - 1, height - 1][2]

lengthCounter = 0
for j in range(height):
    for i in range(width):
        for k in range(3):
            bytesArray = bytesArray + "{0: b}".format(pixels[i, j][k])[-2:]
            lengthCounter += 1

binMessage = bytesArray[0:messageLength]

binary_int = int(binMessage, 2)
byte_number = binary_int.bit_length() + 7 // 8

binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()

print(ascii_text)
