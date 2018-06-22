#!/usr/bin/python2

import time
import os
import webbrowser
import urllib
import commands
from selenium import webdriver

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
        #get user choice 
	choice=raw_input("Enter Your Choice "+os.getlogin()+" : ")
	if   choice=='1':
		#get current date & time in list format
		date_time=time.ctime().split()[1:4]
		print "Date :",date_time[1]+date_time[0],"& Time :",date_time[2]
	elif choice=='2':
		#get file name
		file_name=raw_input("Enter the file name : ")
		#get file path
		file_path=raw_input("Enter the destination where you want to create the file or just enter for create in current location : ")
		#create file with the path given by the user
		os.system('touch '+file_path+file_name)
		print "File created"
                os.system('echo "file created" | festival --tts')
		#delay for 1 second
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
		#open default browser and search in google with the keywords given by the user
		webbrowser.open_new_tab('https://google.com/search?q='+search)
	elif choice=='5':
		print "Logoff Your System"
		time.sleep(2)
		#get current username by using python library function
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
			# open url and store output in data variable
    			data = urllib.urlopen(url)
    			print "Connected"
		except :
  			print "Not connected"
	elif choice=='8':
		

		driver = webdriver.Chrome('/usr/local/bin/chromedriver')
		driver.get('https://web.whatsapp.com/')

		name = input('Enter the name of user or group : ')
		msg = input('Enter your message : ')
		count = int(input('Enter the count : '))

		input('Enter anything after scanning QR code')

		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()

		msg_box = driver.find_element_by_class_name('_2S1VP')

		for i in range(count):
 		   msg_box.send_keys(msg)
  		   button = driver.find_element_by_class_name('_2lkdt')
		   button.click()
	elif choice=='9	':
                #count the number of line in w command and store in variable w_output_line
		w_output_line=commands.getstatusoutput('w | wc -l')
		w_output_line=str(int(w_output_line[1])-3)
		#store the output of the command in ip.txt file
		createfile=os.system("w | tail -"+w_output_line+" >>ip.txt")
		#open and put the data of ip.txt in f variable
		f=open('ip.txt','r')
		#read the f variable data which is previous extracted by the ip.txt file
		messege=f.read()
		#change the data of output to list format
		ip=messege.split()
		i=0
		#check the length of the variable ip and store it into ip_variable
		ip_variable_range=len(ip)
		if ip:
      	   	      print "Connected IPs to your PC....."
       	       	      while i  < ip_variable_range:
			     #print the ip variable data
		             print ip[i+2]
		             i=i+8
   		else :
	       	      print "No IP is connected to your PC......"
		#del the file ip.txt which is created previously for storing some output
		delfile=os.system('rm -f ip.txt')
	
	elif choice=='0':
		print "Thanks For Using"
		os.system('echo "thanks for using" | festival --tts')
		print "Bye........"
		os.system('echo "byeeeeeeeeeeeeeeeeee" | festival --tts')
	else		:
		print "Wrong Choice"


