import requests
import re

def test_single_channel():
    # URL sumber TV3
    url = "https://www.kds.tw/tv/malaysia-tv-channels-online/tv3-sd/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"Sedang menyemak: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Mencari link m3u8 yang mempunyai token (id= atau seumpamanya)
        match = re.search(r'(https?://[^\s"\']*?\.m3u8\?[^\s"\']*)', response.text)
        
        if match:
            link_baru = match.group(1)
            print("\n✅ BERJAYA JUMPA LINK!")
            print(f"Link: {link_baru}")
            
            # Bina fail m3u8 untuk testing
            with open("tv3_test.m3u8", "w") as f:
                f.write(f"#EXTM3U\n#EXTINF:-1,TV3 TEST\n{link_baru}")
            print("\nFail 'tv3_test.m3u8' telah dicipta. Cuba buka dalam VLC.")
        else:
            print("\n❌ GAGAL: Link m3u8 tidak dijumpai. Kod web mungkin berubah.")
            
    except Exception as e:
        print(f"\n⚠️ ERROR: Masalah teknikal - {e}")

if __name__ == "__main__":
    test_single_channel()

