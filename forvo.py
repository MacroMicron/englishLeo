import urllib2
import xml.etree.ElementTree as ET

class Forvo:
    def __init__(key):
        self.key = key

    def getWordPronunciation(self, word):
      	url = 'http://apifree.forvo.com/key/'
      	#response = urllib2.urlopen('http://apifree.forvo.com/key/2d1025563fc6455fe9d5a3ac9c560256/formal/xml/action/word-pronunciations/word/forvo/language/en')
      	#root = ET.fromstring(response.read())
      	#root
      	#root.tag
      	#root.attrib
      	#root[0][10].text
