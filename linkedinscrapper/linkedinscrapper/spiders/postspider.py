import scrapy


class PostspiderSpider(scrapy.Spider):
    name = "postspider"
    headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding" : "gzip, deflate, sdch, br",
    "accept-language" : "en-US,en;q=0.8,ms;q=0.6",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

    def start_requests(self):
        post_list = ['evanharvey_from-22-days-to-22-seconds-with-ai-activity-7079873808270012416-fayp?trk=posts_directory']
        for post in post_list:
            linkedin_post_url = f'https://www.linkedin.com/posts/{post}/' 
            yield scrapy.Request(url=linkedin_post_url, callback=self.parse_post, meta={'post': post, 'linkedin_url': linkedin_post_url}) 
    def parse_post(self,response):
        item = {}
        item['post'] = response.meta['post']
        item['url'] = response.meta['linkedin_url']
        """
        POSTS INFORMATION
        """  
        post = response.css('div  section.mb-3  article')
        
        item['person_name'] = post.css('div.flex.items-center.font-sans.mb-1 div div a::text').get().strip()
        item['post_content'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p::text').get().strip()
        '''
        item['hashtag1'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(1)::text').get().strip()
        item['hashtag2'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(2)::text').get().strip()
        item['hashtag3'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(3)::text').get().strip()
        item['hashtag4'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(4)::text').get().strip()
        item['hashtag5'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(5)::text').get().strip()'''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(1)::text').get() is not None:
            item['hashtag1'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(1)::text').get().strip()
        else:
            item['hashtag1'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(2)::text').get() is not None:
            item['hashtag2'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(2)::text').get().strip()
        else:
            item['hashtag2'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(3)::text').get() is not None:
            item['hashtag3'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(3)::text').get().strip()
        else:
            item['hashtag3'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(4)::text').get() is not None:
            item['hashtag4'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(4)::text').get().strip()
        else:
            item['hashtag4'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(5)::text').get() is not None:
            item['hashtag5'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(5)::text').get().strip()
        else:
            item['hashtag5'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(6)::text').get() is not None:
            item['hashtag6'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(6)::text').get().strip()
        else:
            item['hashtag6'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(7)::text').get() is not None:
            item['hashtag7'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(7)::text').get().strip()
        else:
            item['hashtag7'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(8)::text').get() is not None:
            item['hashtag8'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(8)::text').get().strip()
        else:
            item['hashtag8'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(9)::text').get() is not None:
            item['hashtag9'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(9)::text').get().strip()
        else:
            item['hashtag9'] = ''
        if post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(10)::text').get() is not None:
            item['hashtag10'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(10)::text').get().strip()
        else:
            item['hashtag10'] = ''
        #item['hashtag6'] = post.css('div.attributed-text-segment-list__container.relative.mt-1.mb-1\.5.babybear\:mt-0.babybear\:mb-0\.5 p a:nth-child(6)::text').get().strip()
        item['likes'] = post.css('div.flex.items-center.font-sans.text-sm.my-1.main-feed-activity-card__social-actions a span::text').get().strip()
        yield item
