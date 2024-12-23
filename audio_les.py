from audioplayer import AudioPlayer

# pip install audioplayer

audio = AudioPlayer("zvuk-pobedyi-v-igrovom-urovne-30120.mp3")
print("start")
audio.play(block=True)
print("end")