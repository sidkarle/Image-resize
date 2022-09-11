from PIL import Image

image = Image.open(r"C:\Users\SIDDHESH\Pictures\786001a1-da1b-4ca0-ae8f-98584b806233.jpg")

print(f"current size : {image.size}")

resized_image = image.resize((500, 500))

resized_image.save('siddhesh-photo.jpeg')
