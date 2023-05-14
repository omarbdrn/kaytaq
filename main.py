import requests
import json
import feedparser
from bs4 import BeautifulSoup

# Todo: Add InoReader instead of different RSS feeds

class KayTaq:
    def __init__(self):
        self.rss_feeds = {"SecLists FullDisclosure": {"url":"https://seclists.org/rss/fulldisclosure.rss", "parser": "SecLists"}, "SecLists Pentest": {"url":"https://seclists.org/rss/pen-test.rss", "parser": "SecLists"}, "Reddit": {"url":"https://www.reddit.com/r/netsec/.rss", "parser": "Reddit"}}
        self.entries = 0
        self.snippet_size = 4096
        self.blogBuilderAPI = "http://127.0.0.1:8000/api/models/run?service=blogs&blogType=unique&channel={channel}"
        self.currentFeed = 0

    def open_channel(self, channel):
        response = requests.get(self.blogBuilderAPI.format(channel=channel))
        if response.json()['success'] == True:
            return True
        else:
            raise Exception(response.json()['errors'])
    
    def send_to_channel(self, channel, chunk):
        response = requests.post(self.blogBuilderAPI.format(channel=channel), json={"query": chunk})
        if response.json()['success'] == True:
            return True
        else:
            raise Exception(response.json()['errors'])
    
    def get_final_blog(self, channel):
        response = requests.post(self.blogBuilderAPI.format(channel=channel), json={"status": "Finished"})
        if response.json()['success'] == True:
            return response.json()['blog']
        else:
            raise Exception(response.json()['errors'])

    def split_text(self, content, chunk_size):
        num_snippets = (len(content) + chunk_size - 1) // chunk_size 
        snippets = []
        for i in range(num_snippets):
            start = i * chunk_size
            end = start + chunk_size
            snippet = content[start:end]
            snippets.append(snippet)
        return snippets

    def parseFeeds(self):
        for feed_name, feed_info in self.rss_feeds.items():
            feed_url = feed_info["url"]
            feed_parser = feed_info["parser"]
            
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                blog_title = entry.title
                blog_link = entry.link
                soup = BeautifulSoup(entry.summary, 'html.parser')
                blog_summary = soup.get_text()
                self.parseFeed(blog_link, feed_parser)
                self.entries += 1
                exit()
    
    def parseFeed(self, url, feed_parser):
        # Open Channel to Model
        self.open_channel(self.currentFeed)

        # Get Feed Text
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if feed_parser == "Reddit":    
            # div = soup.find("div", {"data-post-click-location": "post-media-cta"})
            # if div != None:
            #     items = ''.join([line for line in div.get_text().split("\n") if line.strip != ''])
            #     if len(items) > 48:
            #         # If Greater than 48 Characters split context into multiple chunks
            #         for chunk in self.split_text(items, self.snippet_size):
            #             print(chunk)
            return 0
        elif feed_parser == "SecLists":
            data = soup.get_text()
            items = ' '.join([line for line in data.split("\n") if line.strip != ''])
            if len(items) > 48:
                for chunk in self.split_text(items, self.snippet_size):
                    self.send_to_channel(self.currentFeed, chunk)
        
        print(self.get_final_blog(self.currentFeed))
        self.currentFeed += 1

kt = KayTaq()
kt.parseFeeds()