import csv

csv_file = 'wallets_and_proxies.csv'

wallets_and_proxies = [
    {"address": "testnet_btc_address_1", "proxy": "http://username:password@proxy_ip_1:port"},
    {"address": "testnet_btc_address_2", "proxy": "http://username:password@proxy_ip_2:port"},
]

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["address", "proxy"])
    writer.writeheader()
    for wallet in wallets_and_proxies:
        writer.writerow(wallet)

print(f"CSV文件 '{csv_file}' 创建并填充完毕。")
