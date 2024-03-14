import re
import time as t
#file name to read {emails, urls, phone numbers}

filename = "SOURCE FILE YOU WANT TO EXTRACT FROM.txt :


with open(filename, "r") as f:
	text = f.read()
#print(text) #to check the file{if u want uncommon it
	
#------------------------------
#url.. 
	
urls = re.findall(r"(www.\S+.com)",text)

#emails... 

mail=re.findall(r"([a-z0-9]+@gmail\.com)",text)

#10 dig it phone number

ind_phone=re.findall(r"(\+\d\d)?(\s)?(\d)(10)",text)
 

#target file location

filetarget="TARGET FILE PATH YOU WANT TO CREATE.txt"


#file name to write {emails, urls, phone numbers}

f=open(filetarget, "a")
	
def write_mail(mail):
	f. write("the mails are :\n")
	f.write("\n".join(mail))
	print(" the mails are : \n",mail)

def write_urls(urls):
	f. write('the urls are :\n')
	f. write("\n".join(urls))
	print(" the urls are :\n",urls)
def write_ph(ind_phone):
	f. write("the phone numbers are :\n")
	f.write("\n".join(ind_phone))
	print(" the phone numbers are :\n",ind_phone)

	
# iniate the program
def __init__():	
	print("what do you what to extract from your text file :")
	print("1 .to get URL (1) ")
	print("2 .to get mails (2) ")
	print("3 . to get phone number(3) ")
	type=int(input(" enter the type : ")) 
	if (type==1):
		write_mail(mail)
	elif (type==2):
		write_urls(urls)
	elif (type==3):
		write_ph(ind_phone)
	t. sleep(1)
	
	#call the function again... 
	
	again=(input(" Do you want to any other type (y/n):"))
	if (again==('y')):
		__init__()
	else:
		print("thank you !")		
			
__init__()
