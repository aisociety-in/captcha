#generate image captcha
from captcha.image import ImageCaptcha
image = ImageCaptcha()

image_data = image.generate('AI SOCIETY')
image.write('AI SOCIETY', 'captcha.png')

#generate audio captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
audio_data = audio.generate('45678')
audio.write('45678', 'audio.wav')