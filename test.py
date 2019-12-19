import hashlib
import binascii
from bitcoin.rpc import RawProxy

def Interfeisas():
	print("""Pasirinkite norima uzduoti: 
1 - Tranzakcijos mokestis
2 - Ar hashas teisingas
3 - Nutraukti sesija""")
	task = input(">")
	convert = int(task)
	return convert

def Mokestis():

	p = RawProxy()
	#txid = input("Iveskite transakcija ")
	txid = '0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2'
	print(txid)
	raw_tx = p.getrawtransaction(txid)
	decoded_tx = p.decoderawtransaction(raw_tx)

	sumIn = 0
	sumOut = 0
	for output in decoded_tx['vin']:
	    vinTxId = output['txid']
	    raw_vintx = p.getrawtransaction(vinTxId)
	    decoded_vintx = p.decoderawtransaction(raw_vintx)
	    vin_vout = output['vout']
	    for out in decoded_vintx['vout']:
	        if(out['n'] == vin_vout):
	            sumIn+=out['value']
	        
	for output in decoded_tx['vout']:
	    sumOut+=output['value']

	tx_fee = sumIn - sumOut
	print("Transakcijos: ", txid)
	print("mokestis: ", tx_fee, "BTC")


def swap(c):
    c = list(c)
    x = 0
    while(x< len(c)-1):
        if(x != len(c)-1):
           c[x], c[x+1] = c[x+1], c[x]
           x += 2
    return ''.join(c)


def Patikra():



# Mainas
while True:
	task = Interfeisas()
	if task in range(1, 4):
		if task == 1:
			Mokestis()
			continue
		if task == 2:
			Patikra()
			continue
		if task == 3:
			break
	else:
		print("Blogai pasirinkote, bandykite dar karta\n")

