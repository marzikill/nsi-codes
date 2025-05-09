import requests, os
code = 'uhr7-cn2v'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/main.py')
with open('main.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/3.pyxres')
with open('3.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "main.py"')
