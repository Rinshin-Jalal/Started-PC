#!/usr/bin/python
from discord_webhook import DiscordWebhook, DiscordEmbed
import cv2
import datetime
import time


URL = ""
NOW = str(datetime.datetime.now())


def capture_image():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite(f".{NOW}.png", image)
    del(camera)


def message(url):
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title='Some Body opened your laptop',
                         description='somebody opened your laptop if it you check you laptop', color='03b2f8')
    with open(f".{NOW}.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='openedby.jpg')
    embed.set_image(url='attachment://openedby.jpg')
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()


while True:
    try:
        capture_image()
        message(URL)
        print("send image")
        break
    except:
        time.sleep(5)
        print("Network not connected")
        pass
