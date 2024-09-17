import torch
import cv2
import pytesseract
import matplotlib.pyplot as plt

# Set the path to Tesseract executable (required for Windows)
# Example: pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Uncomment the line below and replace with the correct path if necessary
# pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract'

# Load the pre-trained YOLOv5 model from Ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' for a smaller, faster model

# Function to detect objects (products) in the ad image
def detect_objects(image_path):
    # Perform object detection using YOLOv5
    results = model(image_path)
    
    # Convert results to pandas DataFrame format
    detected_objects = results.pandas().xyxy[0]  # Extract bounding box, class, confidence
    return detected_objects

# Function to extract text (brand name or product name) using OCR
def extract_text(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray_img)
    return text

# Function to classify ad and extract brand names and products
def classify_ad(image_path):
    print("Processing Ad Image: ", image_path)

    # Step 1: Detect objects (products) in the image
    detected_objects = detect_objects(image_path)
    print("Detected Products:")
    print(detected_objects[['name', 'confidence']])
    
    # Step 2: Extract text (brand names) using OCR
    extracted_text = extract_text(image_path)
    print("\nExtracted Text (Potential Brand/Product Names):")
    print(extracted_text)

  
    plt.imshow(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB))
    plt.title("Ad Image with Detected Products")
    plt.show()


image_path = 'input.jpeg'  
classify_ad(image_path)
