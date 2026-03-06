import requests
import re
import os

def show_logo():
    os.system('clear')
    try:
        # قراءة ملف الشعار الذي سميته أنت ".الشعار.txt"
        with open('.الشعار.txt', 'r', encoding='utf-8') as f:
            print("\033[1;32m" + f.read() + "\033[0m")
    except:
        print("\033[1;32m[ قناص الحور ]\033[0m")
    print("\033[1;33m" + "-" * 40 + "\033[0m")

def check_account(tiktok_user):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get(f"https://www.tiktok.com/@{tiktok_user}", headers=headers)
        match = re.search(r'instagram\.com/([a-zA-Z0-9._]+)', res.text)
        if match:
            insta_user = match.group(1)
            check_insta = requests.get(f"https://www.instagram.com/{insta_user}/")
            if check_insta.status_code == 404:
                return f"✅ صيد ثمين! @{insta_user} متاح!"
            return f"❌ @{insta_user} مأخوذ."
        return "⚠️ لا يوجد رابط انستقرام."
    except:
        return "🚫 فشل الاتصال."

if __name__ == "__main__":
    show_logo()
    while True:
        target = input("\n[?] أدخل يوزر تيك توك لفحصه: ")
        print(check_account(target))
