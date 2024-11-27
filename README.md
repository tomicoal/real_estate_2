# Property Scraper
This project is a web scraper that extracts property listings from Rightmove. It allows users to search for properties to rent or buy based on their criteria and saves the results to a CSV file.
## Features 
  - Search for rental or purchase properties.
  - Customize search criteria (minimum bedrooms, maximum price/rent).
  - Extract property details such as address, type, number of rooms, bathrooms, price, and link.
  - Save the results to a CSV file for further analysis.
## Requirements
  - Python 3.x
  -  Selenium
  -  Pandas
 ## Setup 
 1. **Install required packages:** ```bash pip install selenium pandas ```
 2. **Download ChromeDriver:** - Ensure you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) installed and it matches your installed Chrome version. - Add ChromeDriver to your system PATH or specify its location in the script.
## Usage
1. **Run the script:** ```bash python property_scraper.py ```
2. **Input search criteria:** - Specify whether you're looking to "rent" or "buy". - Input minimum number of bedrooms and maximum price/rent.
3. **Wait for the script to complete:** - The script will scrape the specified properties and save the results to a CSV file.
