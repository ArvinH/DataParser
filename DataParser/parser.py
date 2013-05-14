import sys
import urllib.request
import json

class Parser:
    def __init__(self, url, datasrc):
        self.url = url
        self.datasrc = datasrc
    def parse(self):
        req_url = self.url
        print(req_url)
        response = urllib.request.urlopen(req_url)
        str_response = response.read().decode('utf-8')
        print(str_response)
        obj = json.loads(str_response)
        print(json.dumps(obj,sort_keys=True, indent=4, separators=(',', ': ')))
        


def main():
    queryText = '孔廟'
    p = Parser('http://query.yahooapis.com/v1/public/yql?q=select%20id%2Ctitle%2Clocation.latitude%2Clocation.longitude%2Cdates.taken%2Cfarm%2Cserver%2Csecret%20from%20flickr.photos.info%20where%20photo_id%20in%20(select%20id%20from%20flickr.photos.search(0)%20where%20text%3D%22%E5%AD%94%E5%BB%9F%22%20and%20has_geo%3D1%20and%20lat%3D22.993299484253%20and%20lon%3D120.20359802246%20and%20content_type%3D1%20and%20radius%3D20%20and%20api_key%3D%2263d0f7b2e9592d8f5ad413cc5c60e551%22%20limit%20100%20)%20and%20api_key%3D%2263d0f7b2e9592d8f5ad413cc5c60e551%22&format=json&callback=','flickr_data')
    #p = Parser('http://query.yahooapis.com/v1/public/yql?q=select id,title,location.latitude,location.longitude,dates.taken,farm,server,secret from flickr.photos.info where photo_id in ( select id from flickr.photos.search(0) where text="'+queryText+'" and has_geo=1 and lat=22.993299484253 and lon=120.20359802246 and content_type=1 and radius=20 and api_key="63d0f7b2e9592d8f5ad413cc5c60e551" limit 100 ) and api_key="63d0f7b2e9592d8f5ad413cc5c60e551" and format=json','opengov_data')
    ###p = Parser('http://query.yahooapis.com/v1/public/yql?q=select%20id%2Ctitle%2Clocation.latitude%2Clocation.longitude%2Cdates.taken%2Cfarm%2Cserver%2Csecret%20from%20flickr.photos.info%20where%20photo_id%20in%20(select%20id%20from%20flickr.photos.search(0)%20where%20text%3D%22'+queryText+'%22%20and%20has_geo%3D1%20and%20lat%3D22.993299484253%20and%20lon%3D120.20359802246%20and%20content_type%3D1%20and%20radius%3D20%20and%20api_key%3D%2263d0f7b2e9592d8f5ad413cc5c60e551%22%20limit%20100%20)%20and%20api_key%3D%2263d0f7b2e9592d8f5ad413cc5c60e551%22&format=json','opengov_data')
    p.parse()



if __name__ == '__main__':
    main()
