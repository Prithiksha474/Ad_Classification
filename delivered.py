from PIL import Image
import imagehash

# Function to compute the hash of an image
def compute_image_hash(image_path):
    img = Image.open(image_path)
    img_hash = imagehash.phash(img)  # Perceptual Hashing (pHash)
    return img_hash

# Function to compare the original ad with the publisher's version
def verify_ad_delivery(original_ad_path, publisher_ad_path, threshold=5):
    # Compute the hash of both the original ad and the publisher's ad
    original_ad_hash = compute_image_hash(original_ad_path)
    publisher_ad_hash = compute_image_hash(publisher_ad_path)

    # Calculate the Hamming distance between the two hashes
    hash_difference = original_ad_hash - publisher_ad_hash
    print(f"Hamming distance between original and publisher ad: {hash_difference}")

    # Check if the difference is within the threshold
    if hash_difference <= threshold:
        print("The ad has likely reached the publisher.")
        return True
    else:
        print("The ad did not reach the publisher or has been significantly altered.")
        return False

# Example usage: provide the paths to the original ad and the publisher's ad
original_ad_path = 'path_to_original_ad.jpg'  # Replace with the actual path to the original ad
publisher_ad_path = 'path_to_publisher_ad.jpg'  # Replace with the actual path to the ad from the publisher's platform

# Verify whether the ad has reached the publisher
verify_ad_delivery(original_ad_path, publisher_ad_path)
