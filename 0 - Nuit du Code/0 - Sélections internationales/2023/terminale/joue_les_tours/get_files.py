import requests, os
code = 'x3c6-wkem'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/NDC.py')
with open('NDC.py', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/theme.pyxres')
with open('theme.pyxres', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "NDC.py"')
