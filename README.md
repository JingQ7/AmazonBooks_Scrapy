# pyAmazon_Scrap

Ability to scraping Amazon Bestseller Book's Details with Scrapy Framework.


### Set up
Create a virtual environment: <br>
python3 -m pip install --user virtualenv <br>
python3 -m venv venv <br>
source venv/bin/activate <br>

Install Scrapy Framework: <br>
pip install Scrapy <br>

Install other dependencies from requirement.txt file

### Run & Save data
scrapy crawl booksScrap -o amazon_data.json
