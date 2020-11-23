from PIL import Image
from main import save_edited_image

def watermark_photo(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to your image
    if (base_image.size > watermark.size):
        base_image.paste(watermark, position)
        #base_image.show()
        #base_image.save(output_image_path)
        save_edited_image(base_image, 'newimage.jpg')
    else:
        print('the size of the watermark is larger than the original photo')


if __name__ == '__main__':
    img = 'ty.png'
    watermark_photo(img, 'marked.jpg', 'sample.jpg', position=(1, 1))