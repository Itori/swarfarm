import io
from glob import iglob

from PIL import Image
from bitstring import Bits, BitStream, ReadError

from .game_data import JokerContainerFile


# Functions to work with static files
def crop_images():
    # If the image is 102x102, we need to crop out the 1px white border.
    for im_path in iglob('herders/static/herders/images/monsters/*.png'):
        im = Image.open(im_path)

        if im.size == (102, 102):
            print(f'Cropping {im_path}')
            crop = im.crop((1, 1, 101, 101))
            im.close()
            crop.save(im_path)


com2us_decrypt_values = [
    0x2f, 0x7c, 0x47, 0x55, 0x32, 0x77, 0x9f, 0xfb, 0x5b, 0x86, 0xfe, 0xb6, 0x3e, 0x06, 0xf4, 0xc4,
    0x2e, 0x08, 0x49, 0x11, 0x0e, 0xce, 0x84, 0xd3, 0x7b, 0x18, 0xa6, 0x5c, 0x71, 0x56, 0xe2, 0x3b,
    0xfd, 0xb3, 0x2b, 0x97, 0x9d, 0xfc, 0xca, 0xba, 0x8e, 0x7e, 0x6f, 0x0f, 0xe8, 0xbb, 0xc7, 0xc2,
    0xd9, 0xa4, 0xd2, 0xe0, 0xa5, 0x95, 0xee, 0xab, 0xf3, 0xe4, 0xcb, 0x63, 0x25, 0x70, 0x4e, 0x8d,
    0x21, 0x37, 0x9a, 0xb0, 0xbc, 0xc6, 0x48, 0x3f, 0x23, 0x80, 0x20, 0x01, 0xd7, 0xf9, 0x5e, 0xec,
    0x16, 0xd6, 0xd4, 0x1f, 0x51, 0x42, 0x6c, 0x10, 0x14, 0xb7, 0xcc, 0x82, 0x7f, 0x13, 0x02, 0x00,
    0x72, 0xed, 0x90, 0x57, 0xc1, 0x2c, 0x5d, 0x28, 0x81, 0x1d, 0x38, 0x1a, 0xac, 0xad, 0x35, 0x78,
    0xdc, 0x68, 0xb9, 0x8b, 0x6a, 0xe1, 0xc3, 0xe3, 0xdb, 0x6d, 0x04, 0x27, 0x9c, 0x64, 0x5a, 0x8f,
    0x83, 0x0c, 0xd8, 0xa8, 0x1c, 0x89, 0xd5, 0x43, 0x74, 0x73, 0x4d, 0xae, 0xea, 0x31, 0x6e, 0x1e,
    0x91, 0x1b, 0x59, 0xc9, 0xbd, 0xf7, 0x07, 0xe7, 0x8a, 0x05, 0x8c, 0x4c, 0xbe, 0xc5, 0xdf, 0xe5,
    0xf5, 0x2d, 0x4b, 0x76, 0x66, 0xf2, 0x50, 0xd0, 0xb4, 0x85, 0xef, 0xb5, 0x3c, 0x7d, 0x3d, 0xe6,
    0x9b, 0x03, 0x0d, 0x61, 0x33, 0xf1, 0x92, 0x53, 0xff, 0x96, 0x09, 0x67, 0x69, 0x44, 0xa3, 0x4a,
    0xaf, 0x41, 0xda, 0x54, 0x46, 0xd1, 0xfa, 0xcd, 0x24, 0xaa, 0x88, 0xa7, 0x19, 0xde, 0x40, 0xeb,
    0x94, 0x5f, 0x45, 0x65, 0xf0, 0xb8, 0x34, 0xdd, 0x0b, 0xb1, 0x29, 0xe9, 0x2a, 0x75, 0x87, 0x39,
    0xcf, 0x79, 0x93, 0xa1, 0xb2, 0x30, 0x15, 0x7a, 0x52, 0x12, 0x62, 0x36, 0xbf, 0x22, 0x4f, 0xc0,
    0xa2, 0x17, 0xc8, 0x99, 0x3a, 0x60, 0xa9, 0xa0, 0x58, 0xf6, 0x0a, 0x9e, 0xf8, 0x6b, 0x26, 0x98
]


def decrypt_images(**kwargs):
    path = kwargs.pop('path', 'herders/static/herders/images')
    for im_path in iglob(f'{path}/**/*.png', recursive=True):
        encrypted = BitStream(filename=im_path)

        # Check if it is 'encrypted'. 8th byte is 0x0B instead of the correct signature 0x0A
        encrypted.pos = 0x07 * 8
        signature = encrypted.peek('uint:8')
        if signature == 0x0B:
            print(f'Decrypting {im_path}')
            # Correct the PNG signature
            encrypted.overwrite('0x0A', encrypted.pos)

            # Replace bits with magic decrypted values
            try:
                while True:
                    pos = encrypted.pos
                    val = encrypted.peek('uint:8')
                    encrypted.overwrite(Bits(uint=com2us_decrypt_values[val], length=8), pos)
            except ReadError:
                # EOF
                pass

            # Write it back to the file
            with open(im_path, 'wb') as f:
                encrypted.tofile(f)

            continue

        # Check for weird jpeg format with extra header junk. Convert to png.
        encrypted.pos = 0
        if encrypted.peek('bytes:5') == b'Joker':
            print(f'Converting Joker container JPEG to PNG {im_path}')
            with open(im_path, 'rb') as f:
                bts = f.read()
                first_img = bts.find(b'JFIF')
                second_img = bts.rfind(b'JFIF')
                imgs = []
                if second_img > -1 and first_img != second_img:
                    imgs = [bts[:second_img], bts[second_img:]]
                    # Add Joker & header to immitate new file
                    imgs[1] = imgs[0][imgs[0].find(b'Joker'):first_img] + imgs[1]
                    imgs = [JokerContainerFile(img, read=False) for img in imgs]
                else:
                    img = JokerContainerFile(bts, read=False)

            # Open it as a jpg and resave to disk
            try:
                if len(imgs) > 1:
                    new_imfile = Image.open(io.BytesIO(imgs[0].data.tobytes()))
                    new_mask = Image.open(io.BytesIO(imgs[1].data.tobytes())).convert('L')
                    new_imfile.putalpha(new_mask)
                else:
                    new_imfile = Image.open(io.BytesIO(img.data.tobytes()))
                new_imfile.save(im_path)
            except IOError:
                print(f'Unable to open {im_path}')
