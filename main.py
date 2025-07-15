import cv2

# get the image location
image_path = input("Enter the name of image e.g. (imgname.jpg) : ")

# read image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found. Please check the file path.")
    exit()

# get image dimensions
height, width = img.shape[:2]
print(f"Image Dimensions: {width} x {height}")

# convert to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert the grayscale image
inverted_img = 255 - grayscale_img

# blur the inverted image using Gaussian blur
blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)

# invert the blurred image
inverted_blurred = 255 - blurred_img

# create pencil sketch
pencil_sketch = cv2.divide(grayscale_img, inverted_blurred, scale=256.0)

# add text to the sketch
cv2.putText(pencil_sketch, "Engr. Zia Ur Rehman", (width - 300, height - 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# save the sketch image
new_img_name = image_path.rsplit('.', 1)[0] + "_sketch.jpg"
cv2.imwrite(new_img_name, pencil_sketch)

# show images in resizable windows
for window_name, display_img in [
    ("Input Image", img),
    ("Grayscale Image", grayscale_img),
    ("Inverted Image", inverted_img),
    ("Blurred Image", blurred_img),
    ("Inverted Blurred Image", inverted_blurred),
    ("Pencil Sketch", pencil_sketch)
]:
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, display_img)
    cv2.resizeWindow(window_name, 800, 600)  # Adjust window size as you like

cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Sketch saved as: {new_img_name}")
print("Code Completed!")
