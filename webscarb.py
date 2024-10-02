import os
import requests
from bs4 import BeautifulSoup
import json
import csv

def extract_headlines(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Unable to access website. Status code: {response.status_code}")
            return []

        # Parse the HTML content of the website
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all headline elements (adjust based on HTML structure of the website)
        headlines = soup.find_all(['h1', 'h2', 'h3' , 'h4' ,'h5','h6'])

        # Extract headline text and corresponding link (if available)
        headline_data = []
        for headline in headlines:
            link_tag = headline.find('a')
            if link_tag and 'href' in link_tag.attrs:
                headline_text = headline.get_text(strip=True)
                headline_link = link_tag['href']
                headline_data.append({
                    'headline': headline_text,
                    'link': headline_link
                })

        return headline_data

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_as_json(data, file_name='headlines.json'):
    # Get the Downloads directory path
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_path, file_name)

    # Save the data in JSON format to the Downloads folder
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return file_path

def save_as_csv(data, file_name='headlines.csv'):
    # Get the Downloads directory path
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_path, file_name)

    # Save the data in CSV format to the Downloads folder
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['headline', 'link'])
        writer.writeheader()
        writer.writerows(data)

    return file_path

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    headlines = extract_headlines(website_url)

    if headlines:
        output_format = input("Enter the output format (json/csv): ").strip().lower()

        if output_format == 'json':
            file_path = save_as_json(headlines)
            print(f"Headlines saved in Downloads as {file_path}")
        elif output_format == 'csv':
            file_path = save_as_csv(headlines)
            print(f"Headlines saved in Downloads as {file_path}")
        else:
            print("Invalid format. Please choose 'json' or 'csv'.")
    else:
        print("No headlines found or an error occurred.")
