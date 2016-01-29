import festival
from pydub import AudioSegment
import lingualeo
import urllib


festival = festival.Festival()
account = raw_input('leo account: ')
password = raw_input('password: ')
balalaykin = lingualeo.Lingualeo(account, password)
balalaykin.auth()
dictionaryGroup = input('dictionary group: ')
url = "http://lingualeo.com/userdict/json"
dictionary = balalaykin.getContent(url, '')
for section in dictionary['userdict3']:
    for word in section['words']:
        if word.get('groups'):
            for group in word['groups']:
                if group == dictionaryGroup:
                    print word['word_value']
                    preWord = word['word_value'].replace("'","").replace(' ', '_')
                    enWord = preWord + "-en"
                    ruWord = preWord + "-ru"
                    enruWord = preWord + "-enru"
                    ruenWord = preWord + "-ruen"
                    festival.ruPhraseToFile(word['user_translates'][0]['translate_value'], '/tmp/leo/' + ruWord + '.mp3')
                    urllib.URLopener().retrieve(word['sound_url'], '/tmp/leo/'+enWord+'.mp3')
                    ruAudio = AudioSegment.from_mp3('/tmp/leo/'+ruWord+'.mp3')
                    enAudio = AudioSegment.from_mp3('/tmp/leo/'+enWord+'.mp3')
                    enruAudio = enAudio + ruAudio
                    enruAudio.export('/tmp/leo/final/'+enruWord+'.mp3', format="mp3")
                    ruenAudio = ruAudio + enAudio
                    ruenAudio.export('/tmp/leo/final/'+ruenWord+'.mp3', format="mp3")













#public class APIConstants {
