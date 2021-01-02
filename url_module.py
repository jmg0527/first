def get_wep(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('주소를 입력해주세요.')
content = get_wep(url)
print(content)