from PIL import Image
from save_instruments import save_edited_image,  add_to_edited_table

def watermark_photo(input_image_path, output_image_path, watermark_image_path, position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to your image
    if (base_image.size > watermark.size):
        base_image.paste(watermark, position)
        #base_image.show()
        save_edited_image(base_image, output_image_path)
	add_to_edited_table(output_image_path)
    else:
        print('the size of the watermark is larger than the original photo')