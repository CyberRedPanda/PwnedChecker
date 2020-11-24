# pwnedChecker
Simple script that leverages selenium to mass check emails on Have I Been Pwned's website without paying for the API

Use by adding a pwned.txt file full of emails you want to check.

Note: replace lines 6 and 8 with the following to run Chrome headless. You'll need to make sure your chromedriver is up to date:

## Run Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

## Use API

Note: You can also check emails directy from the API by using the cloudscraper module to bypass cloudflare protections:

Example:

```
import cloudscraper
import pprint

scraper = cloudscraper.create_scraper(interpreter='nodejs')
response = scraper.get("https://haveibeenpwned.com/unifiedsearch/<yourEmail>")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.text)
```
