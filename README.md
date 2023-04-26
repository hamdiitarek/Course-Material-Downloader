

# Course Material Downloader

This Python script downloads all PDF files from a range of courses offered by example.com. 

## Dependencies

- Python 3.5+
- requests
- BeautifulSoup
- chardet

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/hamdiitarek/Course-Material-Downloader
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the script:

   ```
   python course_material_downloader.py
   ```

   This will download all PDF files from the courses specified in the `range()` function in the script.

## Configuration

You can configure the script by editing the following variables:

- `url_template`: the URL template for the course material pages. The `{}` placeholder will be replaced with the course ID.
- `range()`: the range of course IDs to download. The script will download all PDF files for each course in the range.
- `timeout`: the number of seconds to wait for a response from the server before timing out.
- `headers`: the headers to send with the requests. By default, the script sets the `Accept-Encoding` header to `identity` to prevent the server from compressing the response.
- `folder_name`: the name of the folder to save the PDF files in. By default, the script names the folder after the course ID. If the folder already exists, the script will not create a new folder.
- `pdf_link`: the HTML tag to look for when searching for PDF links. By default, the script searches for `<a>` tags with a `.pdf` file extension.

## License

This code is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
