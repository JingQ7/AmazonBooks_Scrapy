# pyAmazon_Scrap

Ability to scraping Amazon Bestseller Book's Details with Scrapy Framework.


### Set up
Create a virtual environment: <br>
<code>python3 -m pip install --user virtualenv </code> <br>
<code>python3 -m venv venv </code> <br>
<code>source venv/bin/activate </code> <br>

Install Scrapy Framework: <br>
<code>pip install Scrapy </code><br>

Install other dependencies from requirement.txt file

### Run & Save data
<code>scrapy crawl booksScrap -o amazon_data.json</code>
