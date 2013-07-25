import browser
import explain

explains = explain.explains

for meme, (text, images) in explains.items():
    print meme, text, images
