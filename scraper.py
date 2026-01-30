import requests

def get_live():
    # Link stream TV3
    url = "https://tonton-live-001.akamaized.net/content/bundle/B-TV3/manifest.m3u8"
    
    content = "#EXTM3U\n"
    content += "#EXTINF:-1 tvg-id='TV3' tvg-logo='https://upload.wikimedia.org/wikipedia/commons/6/62/TV3_logo_2014.png',TV3\n"
    content += url
    
    with open("playlist.m3u8", "w") as f:
        f.write(content)
    print("Fail playlist.m3u8 berjaya dihasilkan!")

if __name__ == "__main__":
    get_live()
    
