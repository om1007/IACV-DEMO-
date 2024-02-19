import cv2
import matplotlib.pyplot as plt
import easyocr
from deep_translator import GoogleTranslator

# Read the image
img = cv2.imread(r"C:\Users\om\Desktop\CV\adh.png", cv2.IMREAD_COLOR)

# Specify desired target language (English)
target_language = "en"

# Create readers for supported languages
readers = {
    'hi': easyocr.Reader(['hi'], gpu=False),
    'mr': easyocr.Reader(['mr'], gpu=False),
    'ne': easyocr.Reader(['ne'], gpu=False),
    # ... add other language readers as needed
    'ko': easyocr.Reader(['ko'], gpu=False),
    'ja': easyocr.Reader(['ja'], gpu=False),
}

# Translate text and draw bounding boxes
translated_text = []
for language, reader in readers.items():
    text_ = reader.readtext(img)
    if text_:
        for t in text_:
            bbox, text, score = t

            # Translate only if not already in English
            if language != target_language:
                translated = GoogleTranslator(source=language, target=target_language).translate(text)
            else:
                translated = text  # No translation needed if already in English

            translated_text.append((bbox, translated, score))

# Draw bounding boxes and translated text
for bbox, text_to_display, score in translated_text:
    # ... (rest of the code for drawing rectangles and text remains the same)
     # Extract coordinates and ensure correct data types
    x1, y1 = int(bbox[0][0]), int(bbox[0][1])  # Top-left corner
    x2, y2 = int(bbox[2][0]), int(bbox[2][1])  # Bottom-right corner

    # Print coordinates for debugging (optional)
    #print("Coordinates:", x1, y1, x2, y2)

    text_origin =  (x1, y1)

    # Draw the rectangle with proper coordinates
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Add text above the rectangle
    cv2.putText(img, text_to_display,  text_origin, cv2.FONT_HERSHEY_COMPLEX,1.5 , (255, 0, 0), 3)

# Display the image with detected and translated text
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
