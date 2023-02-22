import os
import requests
from bs4 import BeautifulSoup
import chardet

url_template = "https://example.com/course/material/book-{}/pdf_content"

# Loop through a range of course IDs
for course_id in range(430, 436):
    url = url_template.format(course_id)
    response = requests.get(url, headers={'Accept-Encoding': 'identity'}, timeout=5)
    encoding = chardet.detect(response.content)['encoding']
    response.encoding = encoding

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with a PDF file link
    pdf_links = soup.find_all('a', href=lambda href: href and href.endswith('.pdf'))

    # Download each PDF file to a folder named after the course ID
    folder_name = f"Course {course_id}"
    os.makedirs(folder_name, exist_ok=True)
    for pdf_link in pdf_links:
        pdf_url = pdf_link['href']
        pdf_filename = os.path.basename(pdf_url)
        pdf_path = os.path.join(folder_name, pdf_filename)

        with open(pdf_path, 'wb') as f:
            pdf_response = requests.get(pdf_url)
            f.write(pdf_response.content)
