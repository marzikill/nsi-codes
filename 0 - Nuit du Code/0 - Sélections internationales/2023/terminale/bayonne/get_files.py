import requests, os
code = 'g7jx-u3c8'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/5.pyxres')
with open('5.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "5.pyxres"')
