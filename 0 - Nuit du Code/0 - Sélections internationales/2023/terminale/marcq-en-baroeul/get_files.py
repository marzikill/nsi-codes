import requests, os
code = '2wnp-jx7m'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/my_resource.pyxres')
with open('my_resource.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/ndc.py')
with open('ndc.py', 'wb') as file:
    file.write(pyxres.content)
# print(py.content.decode())
os.system('pyxel run "ndc.py"')
