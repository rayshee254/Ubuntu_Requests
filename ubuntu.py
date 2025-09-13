import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher!")

    # Get multiple URLs from user
    urls = input("Please enter the image URLs: ").split(',')
    urls = [url.strip() for url in urls]  # Clean whitespace

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Check important HTTP headers
            if 'Content-Type' not in response.headers or 'image' not in response.headers['Content-Type']:
                print(f"✗ Invalid content type for URL! {url}")
                continue
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:
                filename = "downloaded_image.jpg"
            
            # Check for duplicate files
            filepath = os.path.join("Fetched_Images", filename)
            if os.path.exists(filepath):
                print(f"✗ File already exists: {filename}. Skipping download.")
                continue

            # Saving the image
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for URL {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for URL {url}: {e}")

if __name__ == "__main__":
    main()
