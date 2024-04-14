from PIL import Image


# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width):
      width, height = image.size
      ratio = height/width
      new_height = int(new_width * ratio)
      resized_image = image.resize((new_width, new_height))
      return(resized_image)

def pixels_to_ascii(image, new_width):
    # resize image first
    resized_image = resize_image(image, new_width)
    # convert to grayscale 
    grayscale_image = resized_image.convert("L")
    pixels = grayscale_image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters
       





def main(new_width):
    path = input("Enter a valid pathname to an image:\n")

    try: 
            image = Image.open(path)
    except:
            print(f"{path} is not a valid pathname to an image.")
            return

    new_image_data = pixels_to_ascii(image, new_width)

    #format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    print(ascii_image)

main(new_width=50)