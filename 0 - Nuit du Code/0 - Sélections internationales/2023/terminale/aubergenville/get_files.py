import requests, os
code = '42be-sek3'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/2_edit.pyxres')
with open('2_edit.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/main.py')
with open('main.py', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "2_edit.pyxres"')
