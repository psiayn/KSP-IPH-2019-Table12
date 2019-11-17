import scrapy

class FacebookSearcher(scrapy.Spider):
    name = "facebook_searcher"
    start_urls = ["http://mobile.facebook.com"]
    custom_settings = {"ROBOTSTXT_OBEY": False}

    def __init__(self, search_query):
        self.search_query = search_query
        self.base_url = "http://mobile.facebook.com"

    def parse(self, response):
        print(response.url)
        # email_field = response.xpath('//input[@id="m_login_email"]')
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'momo@chinese.shezuan', 'pass': 'dongonzalo'}, ##replace with your own facebook details
            callback=self.after_login
        )

    def after_login(self, response):
        print(response.url)
        cancel_path = response.xpath('//a[contains(@href, "/login/save-device/cancel/")]/@href').extract()
        if cancel_path:
            cancel_path = cancel_path[0]
            return response.follow(cancel_path, callback=self.after_cancel)
        else:
            return self.after_cancel(response)

    def after_cancel(self, response):
        print(response.url)
        return scrapy.FormRequest.from_response(
            response,
            formdata = {"query": self.search_query},
            callback = self.save_search
        )

    def save_search(self, response):
        print(response.url)
        with open("search_result_{}.html".format(self.search_query), "wt", encoding="utf-8") as f:
            f.write(response.text)
        links = response.xpath('//td[@class="s ch"]/a/@href').extract()
        # links = [i.split("?")[0] for i in links]
        with open("search_result_{}.txt".format(self.search_query), "wt", encoding="utf-8") as f:
            for link in links:
                print(self.base_url + link, file=f)
        return {"links": links}
