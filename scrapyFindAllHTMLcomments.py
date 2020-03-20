import scrapy, re

class QuotesSpider(scrapy.Spider):

    name = 'quotesComments'

    start_urls = ["https://en.wikipedia.org/wiki/Main_Page"]   #< lets try English wikipedia


    def parse(self, response):
        wholeBody = response.xpath("//body").get()   #not used but could be handy
        head = response.xpath("//head").get()      #not used but could be handy
        allHtml = response.xpath("//html").get()      # here we get the entire html code
        commentsWholeBody = re.findall("<!--.*-->", allHtml)      #here we take out the comments

        cleanComments = []    #when we get rid off the comment mark up

        for i in commentsWholeBody:
            firstHalf = re.sub("<!--","",i)
            cleanComments.append(re.sub("-->","",firstHalf))

        yield {'comments': cleanComments}