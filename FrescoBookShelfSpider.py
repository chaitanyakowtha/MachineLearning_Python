# -*- coding: utf-8 -*-
import scrapy
import re

class FrescobookshelfspiderSpider(scrapy.Spider):
    name = 'FrescoBookShelfSpider'
    allowed_domains = ['fbookshelf.herokuapp.com']
    start_urls = ['https://fbookshelf.herokuapp.com/']

    def parse(self, response):
        #Extracting the content using xpath selectors
                response.selector.remove_namespaces()
		divs = response.xpath('//div[@class="col-md-8"]')
		for div in divs:
			Title = div.xpath('.//h3/text()').extract()
			Author = div.xpath('.//p[@class = "author"]/text()').extract()
			Genre = div.xpath('.//p[@class = "genre"]/text()').extract()
			NumberOfPages = div.xpath('.//p[@class = "pages"]/text()').extract()
			StarRating = div.xpath('.//p[@class = "rating"]/text()').extract()
			NumberOfReviews = div.xpath('.//p[@class = "#reviews"]/text()').extract()
			ShortDescription = div.xpath('.//p[@class = "description"]/text()').extract()
			ISBNNumber = div.xpath('.//p[@class = "isbn"]/text()').extract()
			NumberOfVotes = div.xpath('.//p[@class = "votes"]/text()').extract()
			#CommentsClass = [re.sub(re.compile('[^c\d+]'),'',str(x)) for x in [re.findall(r'c\d+',p.get()) for p in div.xpath('p')]]
			#Above code snippet gives some null elements also in list, whereas below code eliminates the nulls too
			#CommentsClass = [temp for temp in [re.sub(re.compile('[^c\d+]'),'',str(x)) for x in [re.findall(r'c\d+',p.get()) for p in div.xpath('p')]] if len(temp)>0]
			#Comments = div.xpath('.//p[contains(@class,CommentsClass)]/text()').extract()
			scraped_info = {'Title':Title,'Author':Author,'Genre':Genre,'NumberOfPages':NumberOfPages,
                                        'StarRating':StarRating,'NumberOfReviews':NumberOfReviews,'ShortDescription':ShortDescription,
                                        'ISBNNumber': ISBNNumber, 'NumberOfVotes': NumberOfVotes}
                        #,'Comments': Comments
			yield scraped_info
        

#response.xpath('//div[@class="col-md-8"]/h3/text()').extract_first() // Title
#response.xpath('//div[@class="col-md-8"]/p[@class = "author"]/text()').extract_first() // Author
#response.xpath('//div[@class="col-md-8"]/p[@class = "genre"]/text()').extract_first() // Genre
#response.xpath('//div[@class="col-md-8"]/p[@class in re.match(r'c[1-1000]')]/text()').extract_first()
