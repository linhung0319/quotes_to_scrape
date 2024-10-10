import base64
import scrapy
from scrapy_splash import SplashRequest

from quotes_to_scrape.items import QuotesItem

# lua_script = """
# function main(splash, args)
#     assert(splash:go(args.url))

#     while not splash:select('div.quote') do
#         splash:wait(0.1)
#         print('waiting...')
#     end
#     return {html=splash:html()}
# end
# """

# lua_script = """
# function main(splash, args)
#     local num_scrolls = 10
#     local scroll_delay = 1.0

#     local scroll_to = splash:jsfunc("window.scrollTo")
#     local get_body_height = splash:jsfunc(
#         "function() {return document.body.scrollHeight;}"
#     )
#     assert(splash:go(splash.args.url))
#     splash:wait(splash.args.wait)

#     for _ = 1, num_scrolls do
#         scroll_to(0, get_body_height())
#         splash:wait(scroll_delay)
#     end

#     return splash:html()
# end
# """

# lua_script = """
# function main(splash, args)
#     assert(splash:go(args.url))

#     local element = splash:select('body > div > nav > ul > li.next > a')
#     element:mouse_click()

#     splash:wait(splash.args.wait)
#     return splash:html()
# end
# """

javascript_script = """
element = document.querySelector('h1').innerHTML = 'The best quotes of all time!'
"""

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["http://quotes.toscrape.com/"]

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js'
        #url = 'https://quotes.toscrape.com/scroll'
        # yield SplashRequest(url=url, callback=self.parse, args={'wait': 0.5})
        
        # yield SplashRequest(
        #     url=url, 
        #     callback=self.parse,
        #     endpoint='execute', 
        #     args={'wait': 2, 'lua_source': lua_script, url: url})

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

    def parse(self, response):
        # quote_item = QuotesItem()
        # for quote in response.css('div.quote'):
        #     quote_item['text'] = quote.css('span.text::text').get()
        #     quote_item['author'] = quote.css('small.author::text').get()
        #     quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
        #     yield quote_item

        imgdata = base64.b64decode(response.data['png'])
        filename = 'some_image.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)
