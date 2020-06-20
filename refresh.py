import json
import pandas as pd
import requests

# proxies
proxy_new = "https://free-proxy-list.net/"
proxy_anon = "https://free-proxy-list.net/anonymous-proxy.html"
proxy_uk = "https://free-proxy-list.net/uk-proxy.html"
proxy_ssl = "https://www.sslproxies.org/"
proxy_us = "https://www.us-proxy.org/"
proxy_list = []

# user agents
ua_url = "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/"
ua_list = []

def parse_ua(url):
    for i in range(1, 100):
        try:
            ua_list.extend(pd.read_html(f"{url}{i}")[0]['User agent'].dropna().to_numpy())
        except:
            return ua_list

def parse_proxy(url):
    proxy_table = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)[0].dropna().to_json(orient='records', double_precision=0)
    proxy_table = json.loads(proxy_table)
    [p.pop("Last Checked", None) for p in proxy_table]
    proxy_list.extend(proxy_table)
    proxies = [f"{p['IP Address']}:{p['Port']}" for p in proxy_table]
    return proxies

with open("anon.py", 'w') as f:
    # dump user agents
    f.write(f"ua_list = {parse_ua(ua_url)}\n")
    # dump proxies
    f.write(f"proxy_new = {parse_proxy(proxy_new)}\n")
    f.write(f"proxy_anon = {parse_proxy(proxy_anon)}\n")
    f.write(f"proxy_ssl = {parse_proxy(proxy_ssl)}\n")
    f.write(f"proxy_uk = {parse_proxy(proxy_uk)}\n")
    f.write(f"proxy_us = {parse_proxy(proxy_us)}\n")
    f.write(f"proxy_all = {proxy_list}\n")

