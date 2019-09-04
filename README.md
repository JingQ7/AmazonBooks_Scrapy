# pyAmazon_Scrap

Ability to scraping Amazon Bestseller Book's Details with Scrapy Framework.


### Set up
Create a virtual environment:
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate

Install Scrapy Framework:
pip install Scrapy

Install other dependencies from requirement.txt file

### Run & Save data to amazon_data.json
scrapy crawl booksScrap -o amazon_data.json
