# BS4 HTML and XML Parsing: News Headlines Scraper

### Overview
This Python project utilizes the `BeautifulSoup` library to scrape the latest news headlines and their corresponding links from a news website. The headlines are then saved in an organized format such as JSON or CSV. The script is designed to handle potential issues like missing or malformed HTML elements gracefully, ensuring robust data extraction.

### Features
- **Scrape headlines** from any specified news website.
- **Output data** in JSON or CSV format.
- **Handle HTML parsing errors** and missing elements gracefully.
- **Menu-driven interface** for user input on website URL and output format.

### Problem Statement
Develop a Python script that scrapes a news website to extract the latest headlines and their corresponding links. The script should output the results in an organized format (e.g., a JSON or CSV file) and handle potential issues like missing or malformed HTML elements gracefully.

### Requirements

- Python 3.x
- `requests` module (Install using `pip install requests`)
- `BeautifulSoup` module (Install using `pip install beautifulsoup4`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sshafiqa/BS4-HTML-and-XML-Parsing.git
   ```

2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the program:**
   ```bash
   python webscrab.py
   ```

### Workflow
1. **User Input**: The user provides the URL of the news website they want to scrape.
2. **Headline Extraction**: The script sends a request to the website, parses the HTML, and extracts all headlines (tagged as `h1`, `h2`, `h3`, etc.) along with their corresponding links.
3. **Choose Output Format**: The user is prompted to choose whether to save the output in **JSON** or **CSV** format.
4. **Save to File**: The scraped data is saved to the **Downloads** folder in the selected format, and the file path is displayed.

### Code Walkthrough

1. **Headline Extraction (`extract_headlines`)**:
   The function `extract_headlines()` sends a GET request to the website, parses the HTML using BeautifulSoup, and looks for headline tags (`h1`, `h2`, `h3`, etc.). For each headline, it extracts the text and its corresponding link, if available.

2. **Saving Data**:
   - **save_as_json()**: Saves the scraped headlines as a JSON file.
   - **save_as_csv()**: Saves the scraped headlines as a CSV file.

3. **Error Handling**:
   The script handles errors like:
   - Connection issues (handled via `requests` exceptions).
   - Malformed or missing HTML elements.


### How to Use

1. **Run the script**: After running the program, it will prompt you to input a news website URL. For example:
   ```
   Enter the website URL: https://www.foxnews.com/
   ```

2. **Choose Output Format**: Select whether you'd like the data saved in JSON or CSV format:
   ```
   Enter the output format (json/csv): json
   ```

3. **Check your Downloads folder**: The output file will be saved in your Downloads directory, and the path will be displayed in the console.

### Sample Output

#### 1. Extracting Headlines

When you run the program and provide a valid news website URL (e.g., [Fox News](https://www.foxnews.com/)), the script extracts the headlines and asks you to choose between saving them as a JSON or CSV file.

#### Example Interaction:

```
Enter the website URL: https://www.foxnews.com/
Fetching headlines...

Enter the output format (json/csv): json
Headlines saved in Downloads as /Users/yourname/Downloads/headlines.json
```

### Notes
- The script is optimized for scraping headlines from news websites that use HTML heading tags (`h1` to `h6`) for headlines. You may need to modify the `extract_headlines()` function if a website uses a different structure.
- Ensure the website you are scraping is public and legally accessible.
- The default file name for JSON output is `headlines.json`, and for CSV, it is `headlines.csv`.
