from PIL import Image

# Opening and reading text file
f = open('message.txt', 'r')
message = f.read()
f.close()

# Converting text to binary
messageBit = ''.join(format(ord(i), 'b').zfill(8) for i in message)
print(messageBit)

# Opening Image
img = Image.open('image.png')
pixels = img.load()
width, height = img.size

crop_index = 0

for j in range(height):
    for i in range(width):
        if not messageBit[crop_index: crop_index + 2] or not messageBit[crop_index + 2: crop_index + 4] or not messageBit[crop_index + 4: crop_index + 6]:
            break
        else:
            # Splitting first bits of messageBit
            bitsRed = messageBit[crop_index: crop_index + 2]
            bitsGreen = messageBit[crop_index + 2: crop_index + 4]
            bitsBlue = messageBit[crop_index + 4: crop_index + 6]

            # Converting the pixel's RGB value into binary, removing last two bits and joining new bits from messageBits
            red = int("{0: b}".format(pixels[i, j][0])[:-2] + bitsRed, 2)
            green = int("{0: b}".format(pixels[i, j][1])[:-2] + bitsGreen, 2)
            blue = int("{0: b}".format(pixels[i, j][2])[:-2] + bitsBlue, 2)

            pixels[i, j] = (red, green, blue)
            crop_index += 6

    if not messageBit[crop_index: crop_index + 2] or not messageBit[crop_index + 2: crop_index + 4] or not messageBit[crop_index + 4: crop_index + 6]:
        break

messageSize = len(messageBit)
messageBits = '{0:08b}'.format(messageSize)
pixels[width - 1, height - 1] = ((pixels[width - 1, height - 1 ][0], pixels[width - 1, height - 1][1], messageSize))

img.save("image2.png")
