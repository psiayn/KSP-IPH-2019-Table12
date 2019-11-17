import scrapy
from urllib.request import urlretrieve

class FacebookScraper(scrapy.Spider):
    name = "facebook_scraper"
    base_url = "http://mobile.facebook.com/"
    start_urls = []
    custom_settings = {"ROBOTSTXT_OBEY": False}

    def __init__(self, profile_id):
        FacebookScraper.start_urls = [profile_id.replace("www", "mobile")]
        self.profile_id = profile_id.split("/")[-1].replace("?", ".")
        self.about_scraped = False
        self.timeline_scraped = False
        self.num_timeline_pics = 0

    def parse(self, response):
        print(response.url)
        with open("scrape_result_{}.html".format(self.profile_id), "wt", encoding="utf-8") as f:
            f.write(response.text)

        try:
            login = scrapy.FormRequest.from_response(
                    response,
                    formdata={'email': 'hello_there@chinese.shezuan', 'pass': 'dongonzaloagain'},
                    callback=self.after_login
                )
            return login
        except:
            login = response.xpath('//a[text() = "Log In"]/@href').extract()
            if login:
                return response.follow(login[0], callback=self.login)
        # data_type = response.xpath('//span[@class="co cj"]/text()').extract()
        # data_links = response.xpath('//span[@class="co cj"]/a/@href').extract()
        # # data = response.xpath('//span[@class="co cj"]/a/text()').extract()
        # studies = response.xpath('//span[contains(text(), "Stu")]')
        # studies_type = studies.xpath('/text()').extract()
        # studies_link = studies.xpath('a/@href').extract()
        # studies_data = studies.xpath('a/text()').extract()
        # print(studies_type, studies_data, studies_link)

    def login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'hello_there@chinese.shezuan', 'pass': 'dongonzaloagain'},
            callback=self.after_login
        )

    def scrape_info(self, response):
        # studies = response.xpath('//span[contains(text(), "Stu")]')
        # studies_type = studies.xpath('text()').extract()
        # studies_link = studies.xpath('a/@href').extract()
        # studies_data = studies.xpath('a/text()').extract()
        # print(studies_type, studies_data, studies_link)

        # location = response.xpath('//span[contains(text(), "Live")]')
        # location_type = location.xpath('text()').extract()
        # location_link = location.xpath('a/@href').extract()
        # location_data = location.xpath('a/text()').extract()
        # print(location_type, location_data, location_link)

        # work = response.xpath('//span[contains(text(), "Work")]')
        # work_type = work.xpath('text()').extract()
        # work_link = work.xpath('a/@href').extract()
        # work_data = work.xpath('a/text()').extract()
        # print(work_type, work_data, work_link)

        f = open("info_{}.txt".format(self.profile_id), "wt")
        works = response.xpath('//span[contains(text(), "Work")]/../../../../../../..//div/div/span/a')
        works_data = works.xpath('text()').extract()
        works_link = works.xpath('@href').extract()
        print("Work", works_data, works_link, file=f)

        education = response.xpath('//span[contains(text(), "Education")]/../../../../../../..//div/div/span/a')
        education_data = education.xpath("text()").extract()
        education_link = education.xpath("@href").extract()
        print("Education", education_data, education_link, file=f)

        places_types = response.xpath('//span[contains(text(), "Places")]/../../../../../../div[2]/div/div/table//div/span/text()').extract()
        places_names = response.xpath('//span[contains(text(), "Places")]/../../../../../../div[2]/div/div/table//div/a/text()').extract()
        for place_type, place_name in zip(places_types, places_names):
            print("Place: '{}'-'{}'".format(place_type, place_name), file=f)

        contactinfo_type =  response.xpath('//div[@id="contact-info"]/div/div[2]//span/text()').extract()
        contactinfo_data = response.xpath('//div[@id="contact-info"]/div/div[2]//tr/td[2]/div/text()').extract()
        for contact_type, contact_data in zip(contactinfo_type, contactinfo_data):
            print("Contact:", contact_type, contact_data, file=f)

        basicinfo_type = response.xpath('//div[@id="basic-info"]/div/div[2]//span/text()').extract()
        basicinfo_data = response.xpath('//div[@id="basic-info"]/div/div[2]//tr/td[2]/div/text()').extract()
        for basic_type, basic_data in zip(basicinfo_type, basicinfo_data):
            print("Basic Info:", basic_type, basic_data, file=f)

        family_links = response.xpath('//div[@id="family"]/div/div[2]/div/a/@href').extract()
        family_names = response.xpath('//div[@id="family"]/div/div[2]/div//h3/a/text()').extract()
        family_imgs = response.xpath('//div[@id="family"]/div/div[2]/div/a/img/@src').extract()
        family_relations = response.xpath('//div[@id="family"]/div/div[2]/div/div/h3[2]/text()').extract()
        for name,link,relation in zip(family_names,family_links,family_relations):
            print("Family: '{}'-'{}'-'{}'".format(name, relation, link), file=f)

        # events = response.xpath('//div[@id="year-overviews"]/div/div[2]/div//a')
        # events_names = events.xpath('text()').extract()
        # events_links = events.xpath('@href').extract()
        # for name,link in zip(events_names, events_links):
        #     print("Event: {}".format(name), file=f)
        events = response.xpath('//div[@id="year-overviews"]/div/div[2]/div/div/div')
        events_names = []
        events_links = []
        for i in events:
            event_names = i.xpath('.//a/text()').extract()
            events_names.append(event_names)
            event_links = i.xpath('.//a/@href').extract()
            events_links.append(event_links)
            print("Events for {}: ".format(i.xpath('div[1]/text()').extract_first()), file=f)
            for name, link in zip(event_names, event_links):
                print("\t '{}'".format(name), file=f)
        f.close()

    def after_login(self, response):
        with open("scrape_result_{}_2.html".format(self.profile_id), "wt", encoding="utf-8") as f:
            f.write(response.text)
        # self.scrape_info(response)
        about_link = response.xpath('//a[text()="About"]/@href')
        if about_link:
            yield response.follow(about_link.extract()[0], callback=self.about)
        # else:
        timeline_link = response.xpath('//a[text()="Timeline"]/@href').extract_first()
        if timeline_link:
            yield response.follow(timeline_link, callback=self.timeline, dont_filter = True)

    def about(self, response):
        self.about_scraped = True
        print("*********SCRAPING ABOUT***********")
        self.scrape_info(response)
        # if not self.timeline_scraped:
            # yield response.follow(response.xpath('//a[text()="Timeline"]/@href').extract_first(), callback=self.timeline)
        # else:
        name = response.xpath('//div[@id="objects_container"]//strong/text()').extract_first()
        img = response.xpath('//img[@alt="{}"]/../@href'.format(name)).extract_first()
        yield response.follow(img, callback=self.profpic)

    def timeline(self, response):
        self.timeline_scraped = True
        print("*********SCRAPING TIMELINE***********")
        # timeline_imgs = response.xpath('//div[@id="timelineBody"]//img[@width>30 and @height>30]/@src').extract()
        timeline_links = response.xpath('//div[@id="timelineBody"]//img[@width>30 and @height>30]/../@href').extract()
        # self.timeline_pic(response, timeline_links)
        for i in timeline_links:
            # self.num_timeline_pics += 1
            yield response.follow(i, callback=self.goto_fullsize)
        # count = 0
        # for i in timeline_links:
        #     urlretrieve(i, "timeline_img_{}_{}.jpg".format(self.profile_id, count))
        #     count += 1
        about_link = response.xpath('//a[text()="About"]/@href')
        if about_link and not self.about_scraped:
            yield response.follow(about_link.extract()[0], callback=self.about)
        name = response.xpath('//div[@id="objects_container"]//strong/text()').extract_first()
        img = response.xpath('//img[@alt="{}"]/../@href'.format(name)).extract_first()
        if not img:
            img = response.xpath('//img[@alt="{}"]/../../../@href'.format(name)).extract_first()
        yield response.follow(img, callback=self.profpic)

    def profpic(self, response):
        print("******SCRAPING PROFPIC******")
        # prof_pic = response.xpath('//div[@id="objects_container"]//img/@src').extract_first()
        view_full = response.xpath('//a[text() = "View full size"]/@href').extract_first()
        if not view_full:
            return None
        return response.follow(view_full, callback=self.fullsize_profpic, dont_filter = True)

    def fullsize_profpic(self, response):
        with open("profpic_{}.jpg".format(self.profile_id), "wb") as f:
            f.write(response.body)

    def timeline_pic(self, response, links):
        # prof_pic = response.xpath('//div[@id="objects_container"]//img/@src').extract_first()
        for i in links:
            print("*****SCRAPING TIMELINE PIC {}******".format(self.num_timeline_pics))
            # view_full = response.xpath('//a[text() = "View full size"]/@href').extract_first()
            # return response.follow(view_full, callback=self.fullsize_timeline_pic)
            # self.goto_fullsize(response, i)
            yield response.follow(i, callback=self.fullsize_timeline_pi, dont_filter = Truec)

    def goto_fullsize(self, response):
        print("*****GETTING FULLSIZE {}******".format(self.num_timeline_pics))
        view_full = response.xpath('//a[text() = "View full size"]/@href').extract_first()
        self.num_timeline_pics += 1
        return response.follow(view_full, callback=self.fullsize_timeline_pic, meta={'count': self.num_timeline_pics}, dont_filter = True)

    def fullsize_timeline_pic(self, response):
        count = response.meta.get('count')
        print("*****SAVING FULLSIZE {}******".format(count))
        with open("timeline_pic_{}_{}.jpg".format(self.profile_id, count), "wb") as f:
            f.write(response.body)
        # self.num_timeline_pics += 1

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
        links = [i.split("?")[0] for i in links]
        print(links)
        return response.text
