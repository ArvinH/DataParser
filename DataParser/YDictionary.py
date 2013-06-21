import csv
import urllib.request
import json
from html.parser import HTMLParser
class MyHTMLParser (HTMLParser ):
    def __init__(self, strict) :
        HTMLParser.__init__ (self, strict )
        self.printed = False
   
    def handle_starttag(self, tag, attrs) :
        #print("Encountered a start tag:", tag)
        if(len (attrs ) > 0) :
            if(attrs [0 ][1 ] == 'pos_abbr' or attrs [0 ][1 ] == 'pos_desc' or attrs[ 0][ 1] == 'explanation' ):
                self.printed = True
                print("the attributes is :" , attrs )
            else:
                self.printed = False
    def handle_endtag(self, tag) :
        #print("Encountered an end tag :", tag)
        self.printed = False
    def handle_data(self, data) :
        if(self.printed ):
            print("Encountered some data  :" , data )
            self.printed = False
       
class Parser :
    def __init__(self, url) :
        self.url = url
    def parse(self) :
        req_url = self.url
        print(req_url )
        WORDS = []
        try:
           
            for word in urllib.request.urlopen (req_url , timeout = 100000 ).readlines ():
                WORDS.append (word.strip ().decode ('utf-8' ))
            WORDS = WORDS.__str__ ()
            parser = MyHTMLParser (strict =False)
            parser.feed (WORDS )
            #str_response = response.read().decode('utf-8')
            #obj = json.loads(str_response)
            #print(json.dumps(obj,sort_keys=True, indent=4, separators=(',', ': ')))
            #print(WORDS)
           
        except(Exception ):
            if isinstance (Exception ):
                print('http error: {0}' .format( Exception.code))
            else:
                print('misc error: ' + Exception.__str__())
          
def main ():
   
    p = Parser('http://tw.dictionary.search.yahoo.com/search?q=temporal')
    p.parse()



if __name__ == '__main__' :
    main()
