import csv
import time
import requests
from bs4 import BeautifulSoup

# 定义目标URL
faucet_url = "https://coinfaucet.eu/en/btc-testnet/"

# 读取CSV文件
wallets_and_proxies = []
with open('wallets_and_proxies.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        wallets_and_proxies.append({"address": row['address'], "proxy": row['proxy']})

for wallet in wallets_and_proxies:
    btc_address = wallet["address"]
    proxy = wallet["proxy"]

    # 设置HTTP代理
    proxies = {
        "http": proxy,
        "https": proxy,
    }

    # 创建会话对象
    session = requests.Session()

    try:
        # 获取faucet页面
        response = session.get(faucet_url, proxies=proxies)
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.content, 'html.parser')

        # 构建表单数据，不需要提取隐藏表单令牌
        data = {
            'address': btc_address,
            'submit_form': '97a736dabd1a937975269c86344860f231c1bfa2'  
        }

        # 提交表单
        response = session.post(faucet_url, data=data, proxies=proxies)
        response.raise_for_status()  # 检查请求是否成功

        if response.status_code == 200:
            print(f"成功领取测试币! 地址: {btc_address}")
        else:
            print(f"领取失败，地址: {btc_address}，状态码: {response.status_code}")
            print("响应内容:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"请求失败，地址: {btc_address}，错误信息: {e}")

    # 休眠8秒
    time.sleep(8)
