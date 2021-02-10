from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    im = im.convert('RGB')
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=10)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image
