In this module, I will present one of the most complete Crawlers (data sweeping tool).

Scrapy is a complete framework for fetching data, processing, extracting, and exporting to different formats and databases.

What can be extracted from a website:
Text, Images, Videos, Emails, Phones,Addresses, Links,
Basically anything that is available within the HTML code of that page

You can select the data you want to extract(normally using XPATH or CSS selectors).

What you will need to install
#####################
# pip3 install scrapy
# Use this website as an example: https://quotes.toscrape.com
# Type on terminal: scrapy startproject name_of_project
# Example: scrapy startproject website_scraper
# Create a spider (a .py file inside /website_scraper/spiders)
scrapy crawl botname
scrapy crawl botname -O dados.csv (to create a csv file with the info)
#####################

in the file items.py we can clean and process the data that we want before save it to a JSON file for example

# avoid get blocked by user agent
# pip3 install scrapy-fake-useragent
# pip3 install scrapeops-scrapy-proxy-sdk 

Use the pipelines.py files to define and export to SQL

in the file settings.py we can configure or setting as an user agent to not be identified as a bot by websites.

to create a database SQL. Use on terminal"scrapy crawl nameofthebot"


