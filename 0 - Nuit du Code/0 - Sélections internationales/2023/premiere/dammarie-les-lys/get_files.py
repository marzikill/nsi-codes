import requests, os
code = '27cx-9vs2'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/theme.pyxres')
with open('theme.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/v2.py')
with open('v2.py', 'wb') as file:
    file.write(pyxres.content)
# print(py.content.decode())
os.system('pyxel run "v2.py"')
