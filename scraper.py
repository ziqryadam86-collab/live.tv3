import requests
import re

def get_tv3_link():
    # URL sumber tunggal untuk TV3
    url = "https://www.kds.tw/tv/malaysia-tv-channels-online/tv3-sd/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"Sedang mencari link terbaru dari: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Mencari link m3u8 yang mempunyai token/ID selepas tanda soal (?)
        match = re.search(r'(https?://[^\s"\']*?\.m3u8\?[^\s"\']*)', response.text)
        
        if match:
            found_link = match.group(1)
            print(f"Berjaya jumpa link: {found_link}")
            return found_link
        else:
            print("Gagal: Link m3u8 tidak dijumpai dalam kod web.")
            return None
    except Exception as e:
        print(f"Error sambungan: {e}")
        return None

def main():
    link = get_tv3_link()
    
    if link:
        # Membina isi fail playlist.m3u8
        content = "#EXTM3U\n"
        content += "#EXT-X-INDEPENDENT-SEGMENTS\n\n"
        content += "#EXTINF:-1, TV3 MALAYSIA\n"
        content += f"{link}\n"
        
        # Menulis fail ke dalam repository
        with open("playlist.m3u8", "w") as f:
            f.write(content)
        print("Fail 'playlist.m3u8' telah dikemaskini secara automatik.")
    else:
        print("Tiada perubahan dibuat kerana link tidak ditemui.")

if __name__ == "__main__":
    main()
    
