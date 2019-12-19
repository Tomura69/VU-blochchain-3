import hashlib
import binascii
import codecs
import struct
from bitcoin.rpc import RawProxy

def Interfeisas():
	print("""Pasirinkite norima uzduoti: 
1 - Tranzakcijos mokestis
2 - Brangiausia tranzakcija
3 - Ar hashas teisingas
4 - Nutraukti sesija""")
	task = input(">")
	convert = int(task)
	return convert

def Mokestis():
	p = RawProxy()
	#txidd = input("Iveskite transakcija")
	#txid = str(txidd)
	txid = '0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2'
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


def Brangiausia():
	p = RawProxy()
	txid = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"
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


def SwapOrder(Line):
    ReverseInput = Line[::-1];
    Swapper = list(ReverseInput);
    Swapped = "";
    for i in range(0, len(Swapper), 2):
        Swapped = Swapped + (Swapper[i + 1] + Swapper[i]);
    return Swapped;

def Endian(Numb):
    Pack = struct.pack("<I",Numb);
    CodeUp = codecs.encode(Pack,'hex');
    Decode = CodeUp.decode();
    return Decode;

def Patikra():
	p = RawProxy()
	BHeight = 277316;
	BHash = p.getblockhash(BHeight);
	Block = p.getblock(BHash);
	BVer = Block['version'];
	BPrevHash = Block['previousblockhash'];
	BNonce = Block['nonce'];
	BTime = Block['time'];
	BMerkle = Block['merkleroot'];
	BBits = Block['bits'];
	BPrevHash = SwapOrder(BPrevHash);
	BMerkle = SwapOrder(BMerkle);
	BBits = SwapOrder(BBits);
	BNonce = Endian(BNonce);
	BTime = Endian(BTime);
	BVer = Endian(BVer);
	Hex = (BVer + BPrevHash + BMerkle + BTime + BBits + BNonce);
	HexBinary = codecs.decode(Hex, 'hex');
	Hash1 = hashlib.sha256(HexBinary).digest();
	Hash2 = hashlib.sha256(Hash1).digest();
	Hash3=codecs.encode(Hash2[::-1],'hex_codec')
	FinalHash = codecs.decode(Hash3);
	print("Block Hash", BHash);
	print("Verified Block Hash", FinalHash);


# Mainas
while True:
	task = Interfeisas()
	if task in range(1, 5):
		if task == 1:
			Mokestis()
			continue
		if task == 2:
			Brangiausia()
			continue
		if task == 3:
			Patikra()
			continue
		if task == 4:
			break
	else:
		print("Blogai pasirinkote, bandykite dar karta\n")