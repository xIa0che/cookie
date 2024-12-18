from DrissionPage import Chromium, ChromiumOptions
import requests
import socket

def get_machine_id():
    return socket.gethostname()

def get_xiaohongshu_cookies():
    co = ChromiumOptions()
    # 创建 Chromium 实例
    page = Chromium(addr_or_opts=co)
    
    # 获取所有 cookie，注意这里需要调用 cookies() 方法
    all_cookies = page.cookies()
    
    # 筛选小红书域名的 cookie 并转换为字符串格式
    xhs_cookies = [f"{cookie['name']}={cookie['value']}" 
                   for cookie in all_cookies 
                   if '.xiaohongshu.com' in cookie.get('domain', '')]
    
    # 将所有 cookie 合并为一个字符串
    cookie_string = '; '.join(xhs_cookies)

    return cookie_string

def send_cookies(server_url, cookies):
    data = {
        "machine_id": get_machine_id(),
        "cookies": cookies
    }
    
    try:
        response = requests.post(
            f"{server_url}/upload_cookie",
            json=data,
            timeout=5
        )
        
        if response.status_code == 200:
            print("Cookie 上传成功！")
        else:
            print(f"上传失败: {response.text}")
            
    except Exception as e:
        print(f"发送失败: {str(e)}")

if __name__ == '__main__':
    # 服务器地址，需要根据实际情况修改
    SERVER_URL = "http://127.0.0.1:5000"
    
    # 获取并发送 cookie
    cookies = get_xiaohongshu_cookies()
    send_cookies(SERVER_URL, cookies)