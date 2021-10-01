from gtts import gTTS

textt="Bhag yaha se saale"

gTTS(text=textt, lang="en", slow=False).save("op.mp3")