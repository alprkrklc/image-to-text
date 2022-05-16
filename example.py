import pytesseract
from PIL import Image

# You need to define `tesseract.exe` location first. (Just for Windows users.) 
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

IMAGE_PATH = 'test.jpg'
LANGUAGE = 'eng'

def main():
    # See available languages to work with.
    languages = pytesseract.get_languages()
    
    # Want to show you two different examples becuase sometimes results can be different in some images.
    
    # Using an image object. (You can also work with `cv2` and so on.)
    image = Image.open(IMAGE_PATH)
    text1 = pytesseract.image_to_string(image, lang=LANGUAGE)

    # Using image path only. Default language is `eng` so you don't need to pass it.
    text2 = pytesseract.image_to_string(IMAGE_PATH)

    seperator = '\n' + '-' * 20 + '\n\n'
    print(text1, text2, sep=seperator)

if __name__ == '__main__':
    main()
