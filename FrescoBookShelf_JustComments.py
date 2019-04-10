# -*- coding: utf-8 -*-
import scrapy


class FrescoBookShelf_JustComments(scrapy.Spider):
    name = 'FrescoBookShelf_JustComments'
    allowed_domains = ['fbookshelf.herokuapp.com/']
    start_urls = ['https://fbookshelf.herokuapp.com//']

    def parse(self, response):
        #Extracting the content using xpath selectors
                response.selector.remove_namespaces()
		divs = response.xpath('//div[@class="col-md-8"]')
		for div in divs:
			#Title = div.xpath('.//h3/text()').extract()
			#Author = div.xpath('.//p[@class = "author"]/text()').extract()
			#Genre = div.xpath('.//p[@class = "genre"]/text()').extract()
			#NumberOfPages = div.xpath('.//p[@class = "pages"]/text()').extract()
			#StarRating = div.xpath('.//p[@class = "rating"]/text()').extract()
			#NumberOfReviews = div.xpath('.//p[@class = "#reviews"]/text()').extract()
			#ShortDescription = div.xpath('.//p[@class = "description"]/text()').extract()
			#ISBNNumber = div.xpath('.//p[@class = "isbn"]/text()').extract()
			#NumberOfVotes = div.xpath('.//p[@class = "votes"]/text()').extract()
                        #CommentsClass = 
                        #re.findall(r'c\d+',str(div.xpath('.//p[@class = "votes"]/text()').extract()))
			Comments = ["|".join(div.xpath('.//p[@class = x]/text()').extract()) for x in ['c1','c2','c3','c4','c5','c6','c7','c8']]
			scraped_info = {'Comments':Comments}
			yield scraped_info
