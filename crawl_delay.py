class CrawlDelay(object):
    def __init__(self,delay=1.0):
        self.last_parse_time = datetime.utcnow()
        self.delay = delay

    def update(self):
        self.last_parse_time = datetime.utcnow()

    def throttle(self):
        sleep_time = self.delay-(datetime.utcnow() - self.last_parse_time).total_seconds()
        if sleep_time > 0.0:
            sleep(sleep_time)
        self.update()

# Default to crawl-delay: 1.0
crawl_delay = CrawlDelay(delay=1.0)

def page_from_url(url,cd=crawl_delay):
    cd.throttle()
    response = ur.urlopen(url)
    return response.read()
    
if __name__ == "__main__":
    url = "http://www.google.com"
    for i in range(10):
        print i
        page_from_url(url)
