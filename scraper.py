import requests
import re

def get_tv3_link():
    url = "https://www.kds.tw/tv/malaysia-tv-channels-online/tv3-sd/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://www.kds.tw/" # Tambah ini supaya server tak block
    }
    
    print(f"Sedang mencari link dari: {url}")
    
    try:
        # Gunakan session supaya cookies disimpan (lebih nampak macam manusia buka)
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        
        # Regex yang lebih fleksibel untuk cari .m3u8
        match = re.search(r'(https?://[^\s"\']*?\.m3u8\?[^\s"\']*)', response.text)
        
        if match:
            found_link = match.group(1)
            # Kadangkala ada backslash (\/) dalam kod web, kita bersihkan
            clean_link = found_link.replace('\\/', '/')
            print(f"✅ BERJAYA: {clean_link}")
            return clean_link
        else:
            print("❌ GAGAL: Link m3u8 tidak dijumpai dalam kod web.")
            return None
    except Exception as e:
        print(f"⚠️ ERROR: {e}")
        return None

def main():
    link = get_tv3_link()
    if link:
        content = f"#EXTM3U\n#EXT-X-INDEPENDENT-SEGMENTS\n\n#EXTINF:-1, TV3 MALAYSIA\n{link}\n"
        with open("playlist.m3u8", "w") as f:
            f.write(content)
        print("Done! Fail 'playlist.m3u8' dikemaskini.")

if __name__ == "__main__":
    main()
    
