from gtts import gTTS
text="hello prince hoe are you are you are well or not"
language="en"
obj=gTTS(text=text,lang=language,slow=False)
obj.save("sound.mp3")