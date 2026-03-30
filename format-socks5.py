import requests


def format_main():
    urls = [
        "https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/refs/heads/master/proxy.txt",
        "https://raw.githubusercontent.com/HankNovic/ProxyClean/refs/heads/main/good_socks.txt",
        "https://raw.githubusercontent.com/BlacKSnowDot0/Proxy-Pulse/refs/heads/main/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/socks5.txt",
        "https://raw.githubusercontent.com/SevenworksDev/proxy-list/refs/heads/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/refs/heads/main/socks5/socks5.txt",
    ]
    out = []
    for url in urls:
        try:
            resp = requests.get(url)
            items = resp.text.split("\n")
            for item in items:
                if len(item) > 10:
                    proxy = f"socks5://{item}"
                    proxy = proxy.replace("\n", "")
                    proxy = proxy.replace("\r", "")
                    proxy = proxy.replace("\t", "")
                    out.append(proxy)
        except Exception as e:
            print(f"❌ get {url} error: {e}")
            pass

    try:
        temp = list(set(out))
        out.clear()
        out = temp
    except Exception as e:
        print(f"❌ get {url} error: {e}")
        pass

    try:
        with open("format-socks5.txt", "w") as file:
            file.write("\n".join(out))
    except Exception as e:
        print(f"❌ get {url} error: {e}")
        pass

    return out


if __name__ == "__main__":
    try:
        format_main()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
