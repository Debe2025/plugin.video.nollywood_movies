import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import urllib.parse
import requests  # For HTTP if needed

# Addon handle
_handle = int(sys.argv[1])

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def get_nollywood_movies(category='latest'):
    # Example: Fetch from YouTube API or scrape (use yt-dlp or YouTube Data API v3 for real impl)
    # For demo, hardcode sample items
    items = [
        {'label': 'Living In Bondage (2019)', 'thumb': 'https://example.com/poster1.jpg', 'url': 'https://www.youtube.com/watch?v=VIDEO_ID1'},
        {'label': 'Lionheart (2018)', 'thumb': 'https://example.com/poster2.jpg', 'url': 'https://www.youtube.com/watch?v=VIDEO_ID2'},
        # Add more via API: https://developers.google.com/youtube/v3/docs/search/list
    ]
    listing = []
    for item in items:
        list_item = xbmcgui.ListItem(label=item['label'])
        list_item.setArt({'thumb': item['thumb']})
        list_item.setProperty('IsPlayable', 'true')
        url = build_url({'mode': 'play', 'video_url': item['url']})
        listing.append((url, list_item, False))
    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.endOfDirectory(_handle)

def play_video(video_url):
    list_item = xbmcgui.ListItem(path=video_url)
    xbmcplugin.setResolvedUrl(_handle, True, list_item)

def router(paramstring):
    params = dict(urllib.parse.parse_qsl(paramstring))
    if params:
        mode = params.get('mode')
        if mode == 'play':
            play_video(params['video_url'])
        # Add more modes: search, etc.
    else:
        # Main menu
        url = build_url({'mode': 'list', 'category': 'latest'})
        li = xbmcgui.ListItem('Latest Nollywood Movies')
        xbmcplugin.addDirectoryItem(_handle, url, li, True)
        # Add other categories: Action, Romance, etc.
    xbmcplugin.endOfDirectory(_handle)

if __name__ == '__main__':
    router(sys.argv[2][1:])
