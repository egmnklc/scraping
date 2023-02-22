# -*- coding: utf-8 -*-
import scrapy

# ? robots.txt includes the restrictions for spider crawling
# ? Spiders cannot run javascript


# ?  fetch("https://www.worldometers.info/world-population/population-by-country/"): Plain html response
# ?  response.body: Plain html content body
# ?  view(response): View targeted site, not so reliable to give it a look.
# ?  title = response.xpath("//h1"): Select title by xpath, case sensitive.
# ?  title.get(): Return data as text.
# ?  title_css: response.css("h1::text"): Select title by CSS selector, convert data to text.
# ?  title_css.get(): Return title text
#!  css selector may cause some performance issues on big data
# ?  countries = response.xpath("//td/a/text()").getall(): Returns all country names under a td in an array.
# ?  countries_css = response.css("td a::text").getall(): Returns all country names under a td in an array using CSS Selector.
# ?
# ?
# ?


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # ! Don't include https:// here, it doesn't work.
    allowed_domains = ['www.worldometers.info/']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

    # * If you want to return the scraped data as a dict:
        yield {
            'title': title,
            'countries': countries,
        }
