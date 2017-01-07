import requests
import json, re

class DownloadYoutubeChannelList:
    
    apikey = ''

    def __init__(self, key):
        self.key = key
    
    def config(self, order, part, channelId, maxResults):
        self.order = order
        self.part = part
        self.channelId = channelId
        self.maxResults = str(maxResults)
        
    def generate_request(self):
        self.url = 'https://www.googleapis.com/youtube/v3/search'
        self.url += '?order=' + self.order + '&part=' + self.part + '&channelId=' + self.channelId + '&maxResults=' + self.maxResults
        self.url += '&key=' + self.key
        #print (self.url)
        
    def request_data(self):
        self.videos = {}
        data = requests.get(self.url).json()
        for item in data['items']:
            if item['id']['kind'] == "youtube#video":
                videoId = item['id']['videoId']
                title = item['snippet']['title']
                self.videos[videoId] = title
                
    def display(self):
        for id,title in self.videos.items():
            print (id, title)

    def generate_vedio_list(self, filename):
        file = open(filename, 'w')
        for id,title in self.videos.items():
            file.write('https://www.youtube.com/watch?v=' + id + '\n')
        file.close()

if __name__ == '__main__':
    d = DownloadYoutubeChannelList('your Youtube API key')
    d.config('viewCount', 'snippet', 'UC6IMF6xi_MZ3jA1wRlPQDLA', 50)
    d.generate_request()
    d.request_data()
    d.display()
    d.generate_vedio_list('videolist.txt')
