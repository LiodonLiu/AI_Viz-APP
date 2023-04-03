from PIL import Image

def resize(filename):
    img = Image.open('./foundImages/' + filename + '.jpg')
    final_img = Image.new('RGB', (500, 500), color=(255, 255, 255))

    if filename == 'ice cream':
        size = 100
    elif filename == 'table':
        size = 200
    elif filename == 'tree':
        size = 300
    elif filename == 'door':
        size = 200
    elif filename == 'house':
        size = 500
    elif filename == 'cat':
        size = 100
    elif filename == 'tea':
        size = 50

    img = img.resize((size, size))
    final_img.paste(img, (250-size//2, 500-size))

    final_img.save('./foundImages/' + filename + '.jpg')