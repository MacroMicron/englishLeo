# -*- coding: utf-8 -*- 
from subprocess import call

class Festival:
    def sayPhrase(self, phrase, language):
      phrase = "'" + phrase + "'"
      call("echo " + phrase + " | " + "festival --tts --language " + language, shell=True)

    def ruPhraseToFile(self, phrase, path):
      phrase = "'" + phrase + "'"
      call("echo " + phrase + " | " + " text2wave -eval '(voice_msu_ru_nsh_clunits)' | lame - " + path + " 2> /dev/null", shell=True)

# Usage example
#festival = Festival()
#festival.ruPhraseToFile("уходить, уезжать; убегать, улетать", "/tmp/uletet.mp3")
