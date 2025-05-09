import requests, os
code = 'mfj3-lfx8'
site = 'https://www.nuitducode.net'
url = site + '/storage/fichiers_pyxel/' + code
py = requests.get(url + '/5.pyxres')
with open('5.pyxres', 'wb') as file:
    file.write(py.content)
pyxres = requests.get(url + '/projet_NDC.py')
with open('projet_NDC.py', 'wb') as file:
    file.write(pyxres.content)
print(py.content.decode())
os.system('pyxel run "5.pyxres"')
