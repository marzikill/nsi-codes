import requests, os
code = 'vw6j-5lhg'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/xiaolongbao.py')
with open('xiaolongbao.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/xiaolongbao.pyxres')
with open('xiaolongbao.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "xiaolongbao.py"')
