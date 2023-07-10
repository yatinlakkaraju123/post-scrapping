import scrapy


class PostslinksaSpider(scrapy.Spider):
    name = "postslinksa"
    download_delay = 2

    headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding" : "gzip, deflate, sdch, br",
    "accept-language" : "en-US,en;q=0.8,ms;q=0.6",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

    def start_requests(self):


        linkedin_post_url = 'https://www.linkedin.com/directory/posts/a-1?trk=posts_directory_page_num_nav'
        yield scrapy.Request(url=(linkedin_post_url), callback=self.parse_post, meta={'posts': linkedin_post_url}) 
    def parse_post(self,response):
        item = {}
        posts = response.css('li.listings__entry')
        for post in posts:
            yield{
                'url':post.css('a.listings__entry-link').attrib['href']
            }
