import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = [' https://maoyan.com/films?showType=3']
    start_urls = ['http:// https://maoyan.com/films?showType=3/']

    # def parse(self, response):
        # pass
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(
            url = url, 
            callback= self.parse,
            dont_filter = True,
            headers = {
                'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                'Cookie' : '__mta=150239753.1595246592119.1595637408584.1595803814641.12; uuid_n_v=v1; uuid=F9B75DF0CA8011EAB2AE8B45D9A9C865119372F35227413E9C64975C445D4CF0; mojo-uuid=7f4c703124a36d6b48e207b39862b4ec; _lxsdk_cuid=1736c1b3e26c8-088cabfab03c83-15366650-13c680-1736c1b3e26c8; _lxsdk=F9B75DF0CA8011EAB2AE8B45D9A9C865119372F35227413E9C64975C445D4CF0; _csrf=4107fea4b0dae19dcfafa5b4de7b027c5395789b195dae3802d1b38a661db34d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595331874,1595542409,1595637405,1595802080; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595812035; __mta=150239753.1595246592119.1595803814641.1595812035987.13; mojo-session-id={"id":"13f5e886525ceca83099134505aeab52","time":1595814984081}; mojo-trace-id=1; _lxsdk_s=1738dfc3984-205-701-1be%7C%7C2'
            })
    
    def parse (self,response):
        print(response.url)
        print(response.text)
        movies = Selector(response = response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            moviename = movie.xpath('./div[@class="movie-hover-title"]/span/text()[1]').extract_first()
            movietype = movie.xpath('./div[@class="movie-hover-title"]/text()').extract()[-3].strip()
            showtime = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].strip()
            item = MaoyanmovieItem()
            item['moviename'] = moviename
            item['movietype'] = movietype
            item['showtime'] = showtime
            print('-----------')
            print(moviename)
            print(movietype)
            print(showtime)
            # print('-----------')
            # print(moviename.extract())
            # print(moviename.extract_first())
            # print(moviename.extract_first().strip())
            # print('-----------')
            # print(movietype.extract())
            # print(movietype.extract_first())
            # print(movietype.extract_first().strip())
            # print('-----------')
            # print(showtime.extract())
            # print(showtime.extract_first())
            # print(showtime.extract_first().strip())
            yield item


