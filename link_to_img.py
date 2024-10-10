import csv
import os
import requests

# Create a directory to store the images
os.makedirs('brawler_images', exist_ok=True)
os.makedirs('base_brawler_images', exist_ok=True)

# Read the CSV file
with open('cleaned_bs_pins_by_brawler.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    pin_id = 0
    prev_brawler = ""
    for row in csv_reader:
        brawler_name = row['brawler_link']
        image_link = row['pin_img-src']
        
        if prev_brawler != brawler_name:
            pin_id = 0

        # Download the image
        response = requests.get(image_link)
        if response.status_code == 200:
            # Generate a unique filename for the image
            if pin_id == 0:
                filename = f"{brawler_name}.png"
                filepath = os.path.join('base_brawler_images', filename)
            else:
                filename = f"{brawler_name}_{pin_id}.png"
                filepath = os.path.join('brawler_images', filename)

            # Save the image to a file
            with open(filepath, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Saved image: {filename}")
        else:
            print(f"Failed to download image for {brawler_name}")
        prev_brawler = brawler_name
        pin_id += 1

