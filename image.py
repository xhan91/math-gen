from PIL import Image, ImageDraw, ImageFont
from random import random

def generateImg(num1, num2, imgNum):
    # Set up the variables for the image
    image_width = 2550
    image_height = 1100
    bg_color = (255, 255, 255)
    font_size = 60
    font_color = (0, 0, 0)

    # Set up the variables for the addition calculation

    # Load the apple image
    apple_image = Image.open("apple.jpeg")
    apple_size = image_width // (4 * 3)
    apple_height = int(apple_size * 0.8)
    apple_image = apple_image.resize((apple_size, apple_height))

    # Load the font
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", font_size)

    # Create the image
    image = Image.new("RGB", (image_width, image_height), bg_color)

    # Draw the apples
    apple_padding = 0
    total_apples_width = (num1 + num2) * (apple_size + apple_padding) - apple_padding
    apples_x = (image_width - total_apples_width) // 2
    apples_y = (image_height - apple_height) // 2
    # Draw left
    for i in range(num1):
        image.paste(apple_image, (apples_x + i % 3 * (apple_size + apple_padding), apples_y + ((i // 3) - 1) * apple_height))
    # Draw right
    for i in range(num2):
        image.paste(apple_image, (apples_x + (3 + (i % 3)) * (apple_size + apple_padding) + 100, apples_y + ((i // 3) - 1) * apple_height))

    # Draw the plus and equals signs
    plus_sign_x = apples_x + 3 * (apple_size + apple_padding) + 35
    plus_sign_y = (image_height - font_size) // 2
    equals_sign_x = apples_x + total_apples_width + font_size * 2
    equals_sign_y = plus_sign_y
    plus_draw = ImageDraw.Draw(image)
    plus_draw.text((plus_sign_x, plus_sign_y), "+", font=font, fill=font_color)
    plus_draw.text((equals_sign_x, equals_sign_y), "=", font=font, fill=font_color)
    image.save(f"img/addition{imgNum}.png")

c = 0
for i in 9:


