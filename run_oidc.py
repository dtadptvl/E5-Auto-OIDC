import time
import random
import requests
from azure.identity import DefaultAzureCredential

def main():
    print("Đang xác thực thông qua OIDC...")
    # Tự động nhận diện chứng chỉ OIDC từ GitHub Actions
    credential = DefaultAzureCredential()
    token_obj = credential.get_token("https://graph.microsoft.com/.default")
    access_token = token_obj.token

    # Các endpoint dành cho Application Permissions
    endpoints = [
        "https://graph.microsoft.com/v1.0/users",
        "https://graph.microsoft.com/v1.0/sites/root",
        "https://graph.microsoft.com/v1.0/applications?$count=true"
    ]
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    random.shuffle(endpoints)

    for endpoint in endpoints:
        time.sleep(random.randint(2, 6))
        try:
            resp = requests.get(endpoint, headers=headers)
            if resp.status_code == 200:
                print(f"Thành công: {endpoint}")
            else:
                print(f"Lỗi {resp.status_code} tại {endpoint}: {resp.text}")
        except Exception as e:
            print(f"Ngoại lệ khi gọi {endpoint}: {e}")

if __name__ == "__main__":
    main()
