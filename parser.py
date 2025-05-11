import re
import requests
from kodi_six import xbmc, xbmcaddon

BASE_URL = "https://www.freeshot.live"

def get_categories():
    return [
        ('+18 Adult Live', '/live-tv/18-adult-live'),
        ('Sports', '/live-tv/sky-sports'),
        # Ajouter toutes les catégories du menu
    ]

def get_channels(category_url):
    html = requests.get(BASE_URL + category_url).text
    return re.findall(r'<a href="(/live-tv/[^"]+)"[^>]*>([^<]+)<', html)

def play_channel(channel_url):
    html = requests.get(BASE_URL + channel_url).text
    video_url = re.search(r'source src="([^"]+\.mp4)"', html).group(1)
    xbmc.Player().play(video_url)
