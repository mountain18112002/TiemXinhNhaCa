from PIL import Image

# Open the image
img = Image.open('02.jpg')

# Define the new size (width, height)
# Define the coordinates for cropping (left, upper, right, lower)
crop_box = (0, 0, img.width, 1920)

# Crop the image
cropped_img = img.crop(crop_box)

# Save the cropped image
cropped_img.save('02.jpg')
