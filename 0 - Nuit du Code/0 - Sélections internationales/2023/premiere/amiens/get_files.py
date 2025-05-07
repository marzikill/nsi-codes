import requests, os
code = 'xf38-d53b'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/2.pyxres')
with open('2.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(pyxres.content)
# print(py.content.decode())
os.system('pyxel run "ndc.py"')
