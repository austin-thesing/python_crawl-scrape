class AppCrawler:

    def __init__(self, starting_url, depth)
        self.starting_url = starting_url
        self.depth = depth
        self.apps = []

    def crawl(self):
        return

    def get_app_from_link(self, link):
        return

class App:
    def __init__(self, name, developer, price, links)

        self.name = name
        self.developer = developer
        self.price = price
        self.links = links

    def __str__(self):
        return ("Name " + self.name.encode('UTF-8') +
        "\r\nDeveloper: " + self.developer.encode('UTF-8') +
        "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")

crawler = AppCrawler('https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8&utm_medium=referral&utm_source=pulsenews', 0)
crawler.crawl()

for app in self.apps:
    print app
