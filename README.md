# Scrapy with Splash Web Scraping Project

This project demonstrates the use of Scrapy and Splash for web scraping JavaScript-rendered content. It includes examples of different techniques for handling dynamic websites.

## Setup Instructions

### 1. Docker Setup for Splash

First, pull the Splash Docker image:
```bash
docker pull scrapinghub/splash
```

Run the Splash container:
```bash
docker run -p 8050:8050 scrapinghub/splash
```

Splash will now be available at `http://localhost:8050`.

### 2. Project Configuration

The project uses the following Splash-specific settings in `settings.py`:

```python
SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

## Features Demonstrated

This project showcases several key features of Scrapy and Splash:

1. **JavaScript Execution**: Modifying page content using JavaScript
   ```python
   javascript_script = """
   element = document.querySelector('h1').innerHTML = 'The best quotes of all time!'
   """
   ```

2. **Screenshot Capture**: Taking screenshots of rendered pages
   ```python
   yield SplashRequest(
       url,
       callback=self.parse,
       endpoint='render.json',
       args={
           'wait': 2,
           'js_source': javascript_script,
           'html': 1,
           'png': 1,
           'width': 1000,
       }
   )
   ```

3. **Commented Examples**: The code includes commented examples of:
   - Waiting for specific elements to load
   - Infinite scrolling simulation
   - Clicking elements using Lua scripts

## Spider Details

The main spider (`QuotesSpider`) demonstrates:
- Using SplashRequest to handle JavaScript-rendered content
- Processing and saving screenshots
- Parsing and extracting data from dynamic web pages

## Additional Notes

- The project is set up to scrape from "quotes.toscrape.com", a commonly used test site for web scraping
- Different techniques are provided (though commented out) for various scraping scenarios
- The code includes examples of both JavaScript and Lua scripts for different use cases

## Usage

To run the spider:
```bash
scrapy crawl quotes
```

This will execute the spider and save the screenshot as 'some_image.png'.

