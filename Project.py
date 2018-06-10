#!/usr/bin/python2

import time
import os
import webbrowser
import urllib

option='''
Press 1 : To display current date and time
Press 2 : To create a file
Press 3 : To create a directory
Press 4 : To search on google
Press 5 : To logout your system
Press 6 : To shutdown your os
Press 7 : To check internet connection in your pc
Press 8 : To login whatsapp on browser
Press 9 : To check all connected IP in your network
Press 0 : To exit
'''

choice=0
while choice!='0':
	print option
	os.system('echo "enter your choice '+os.getlogin()+' " | festival --tts')  
	choice=raw_input("Enter Your Choice "+os.getlogin()+" : ")
	if   choice=='1':
		date_time=time.ctime().split()[1:4]
		print "Date :",date_time[1]+date_time[0],"& Time :",date_time[2]
	elif choice=='2':
		file_name=raw_input("Enter the file name : ")
		file_path=raw_input("Enter the destination where you want to create the file or just enter for create in current location : ")
		os.system('touch '+file_path+file_name)
		print "File created"
                os.system('echo "file created" | festival --tts')
		time.sleep(1)
	elif choice=='3':
		folder_name=raw_input("Enter the folder name : ")
		folder_path=raw_input("Enter the destination where you want to create the folder or just enter for create in current location : ")
		os.system('mkdir -p '+folder_path+folder_name)
		print "Folder created"
                os.system('echo "folder created" | festival --tts')
		time.sleep(1)
	elif choice=='4':
		search=raw_input("Enter for search : ")
		webbrowser.open_new_tab('https://google.com/search?q='+search)
	elif choice=='5':
		print "Logoff Your System"
		time.sleep(2)
		current_username=os.getlogin()
		os.system('pkill -KILL -u '+current_username)
	elif choice=='6':
		print 'Good Bye '+os.getlogin()
		os.system('echo Good Bye '+os.getlogin()+' | festival --tts')
		time.sleep(1)
		print 'Shutdown.......'
		os.system('echo shutdownnnnnnnnnnnnn | festival --tts')
		time.sleep(2)
		os.system('poweroff')
	elif choice=='7':
		print "Checking Internet Connection....."
		try    :
    			url = "https://www.google.co.in"
    			data = urllib.urlopen(url)
    			print "Connected"
		except :
  			print "Not connected"
	elif choice=='8':
		print 8
	elif choice=='9':
		createfile=os.system('w | tail -2 >>ip.txt')
		f=open('ip.txt','r')
		messege=f.read()
		ip=messege.split()
		i=0
		ip_variable_range=len(ip)
		print "Connected IPs in your PC....."
		os.system('echo connected ip in your pc | festival --tts')
		while i < ip_variable_range:
			print ip[i+2]
			i=i+8
		delfile=os.system('rm -f ip.txt')
	elif choice=='0':
		print "Thanks For Using"
		os.system('echo "thanks for using" | festival --tts')
		print "Bye........"
		os.system('echo "byeeeeeeeeeeeeeeeeee" | festival --tts')
	else		:
		print "Wrong Choice"


