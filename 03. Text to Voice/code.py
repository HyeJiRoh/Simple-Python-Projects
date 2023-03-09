from gtts import gTTS
from playsound import playsound

file_path = '입력된 소개.txt'

with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text = read_file, lang = 'ko')

tts.save(r"test.mp3")
playsound("test.mp3")

# playsound의 원활한 사용을 위해 아래의 명령어를 터미널에 입력 후, 사용해야 한다.
# pip3 install PyObjC