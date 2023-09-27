import httpx

url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true"

try:
    response = httpx.get(url)
    response.raise_for_status()  # Memeriksa apakah respons adalah 2xx (sukses)
    
    with open("proxy.txt", 'w') as file:  # Mengganti nama file menjadi "proxies.txt"
        file.write(response.text)  # Menyimpan respons ke dalam file
except httpx.HTTPError as e:
    print(f"Terjadi kesalahan HTTP: {e}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")