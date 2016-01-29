import urllib, urllib2, json
from cookielib import CookieJar

class Lingualeo:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cj = CookieJar()

    def auth(self):
        url = "http://api.lingualeo.com/api/login"
        values = {
            "email" : self.email,
            "password" : self.password
        }

        return self.getContent(url, values)

    def addWord(self, word, tword):
        url = "http://api.lingualeo.com/addword"
        values = {
            "word" : word,
            "tword" : tword
        }
        self.getContent(url, values)

    def getTranslates(self, word):
        url = "http://api.lingualeo.com/gettranslates?word=" + word

        try:
            result = self.getContent(url, {})
            translate = result["translate"][0]
            return {
                "is_exist" : translate["is_user"],
                "word" : word,
                "tword" : translate["value"].encode("utf-8")
            }
        except Exception as e:
            return False

    def getContent(self, url, values):
        data = urllib.urlencode(values)

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        req = opener.open(url, data)

        return json.loads(req.read())

    def getDictionaryGroups(self):
      	url = "http://lingualeo.com/userdict3/getWordSets"
      	groups = self.getContent(url, '')
      	if groups.get('result'):
      	    for group in groups['result']:
            		print group['name'],'(',group['id'],')'

    def getWordsFromDictionary(self, dictionaryGroup):
      	url = "http://lingualeo.com/userdict/json"
      	dictionary = self.getContent(url, '')
      	for section in dictionary['userdict3']:
      	    for word in section['words']:
            		if word.get('groups'):
            		    for group in word['groups']:
                  			if group == dictionaryGroup:
                  			    print word['word_value'], word['user_translates'][0]['translate_value'], word['sound_url']

    def getWords(self):
      	url = "http://lingualeo.com/userdict/json"
      	dictionary = self.getContent(url, '')
      	for section in dictionary['userdict3']:
      	    for word in section['words']:
            		print word['word_value'], word['sound_url']



#    public static final String AUTH_ADDRESS = "http://api.lingualeo.com/api/login"; // POST
#    public static final String ADD_WORD = "http://lingualeo.com/userdict3/addWord"; // POST
#    public static final String GET_TRANSLATION = "http://lingualeo.com/userdict3/getTranslations"; //GET
#    public static final String CREATE_DICTIONARY = "http://lingualeo.com/userdict3/createWordSet"; //POST
#    public static final String GET_DICTIONARIES = "http://lingualeo.com/ru/userdict3/getWordSets"; //GET
#    public static final String GET_WORDS_FROM_DICTIONARY = "http://lingualeo.com/userdict/json"; // POST
#    public static final String DELETE_DICTIONARY = "http://lingualeo.com/userdict3/deleteWordSet"; // POST
#    public static final String DELETE_WORD_FROM_DICTIONARY = "http://lingualeo.com/ru/userdict3/deleteWords"; //POST
#}
# found here: https://github.com/VladimirApolaiko/Leo-web-clien
