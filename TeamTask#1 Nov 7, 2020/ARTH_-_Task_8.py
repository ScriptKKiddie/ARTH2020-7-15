from os import system
from os import remove 
from shutil import which
from time import sleep
import getpass
import json
import subprocess
import os

#system("while sleep 1;do tput sc;tput cup 0 $(($(tput cols)-28));echo -e \"\e[1;32m`date +%d\" \"%b\", \"%Y\" \"%a\" \"%r`\e[39m\";tput rc;done &")

f = open('livedate', 'w')
f.write("while sleep 1;do tput sc;tput cup 0 $(($(tput cols)-28));echo -e \"\e[1;32m`date +%d\" \"%b\", \"%Y\" \"%a\" \"%r`\e[39m\";tput rc;done &")  

f.close() 



system("bash livedate")

def normal_colours():
	system("tput bold")
	system("tput setaf 7")
	system("tput setab 16")
	
global in1
in1 = 0

normal_colours()
system("clear")

def menu():
	global in1
	if(in1==0):

		in1 = 1
	else:
		a = input("\n\tpress enter to view menu.....  ")

	system("clear")
	system("tput setaf 12")
	print("""
	 *******************""", end = "")
	system("tput setaf 11") 
	print(""" Welcome, this project is a joint collaboration of Sanket Shobit Shubham and Mangal """, end = "")
	system("tput setaf 12")
	print("""*********************""")
	normal_colours()
 
	print("""

	Enter your choice :
	\t1.  Open project developer's LinkedIn profile :D
	\t2.  Open google.com
	\t3.  Speak whatever I will type
	\t4.  Check if this computer is connected to internet or not
	\t5.  Show calander of previous, current and next month
	\t6.  Open new terminal
	\t7.  Who is the current user ?
	\t8.  View all the current running process
	\t9.  Create user by entering unique username and password
	\t10. Delete existing user
	\t11. File handling(.txt file)
	\t12. SHOW ME DOCKER OPTIONS PLEASE!!!
        \t13. AUTOMATE AWS CLI FOR ME PLEASE!!!
	\t14. AUTOMATE HADOOP
	\t15. PARTITION AUTOMATION
	\t16. EXIT\nEnter your choice : """, end = "")
	if(in1 == 1):
		system("espeak-ng -s 80 \"Hi welcome \"")
		in1 = 2
	try:
		ch = int(input())
	except:
		ch=100

	return ch


def menu2():
	system("clear")
	print("""\n\n\n\n
		1. Insert into file
		2. Read file
		3. Delete file if exists
		4. Copy existing file to another new file
		5. Read 2 files (it will print 2 files together)
		6. EXIT
	
	Enter your choice : """, end = "")
	try:		
		ch1=int(input())	
	except:
		ch1=100
	return ch1


def menu3():
	system("clear")
	print("""\n\n\n\n
		1. Start Docker
		2. List Docker Images
		3. List Docker Containers
		4. Search Docker Image
		5. Pull Image
		6. Launch Container
		7. Inspect docker Container
		8. Execute command in the running container
		9. Stop Docker Container
                10. Stop Docker
		11. EXIT
	
	Enter your choice : """, end = "")
	try:		
		ch2=int(input())	
	except:
		ch2=100
	return ch2

def menu4():
	system("clear")
	print("""\n\n\n\n
		1. Download and install awscli2 on base Linux RHEL8
		2. aws configure
		3. List/Describe AWS volumes
		4. Creation of Key-Pair
		5. Deletion Of Key-Pair
		6. Creation of Security Group and define its rules
		7. Launch ec2 Instance
		8. Creating EBS Volume 
		9. Attach EBS Volume to EC2 Instance
		10. EXIT
	
	Enter your choice : """, end = "")
	try:		
		ch3=int(input())	
	except:
		ch3=100
	return ch3

def partition():
	system("clear")
	system("tput setaf 3")
	print("\t\t\tWelcome to PARTITION PROGRAM")
	system("tput setaf 7")
	print("\t\t\t---------------------------")


	r = input("Where to run this menu program?(local/remote) : ")
	print(r)
	t = 1
	while t == 1:
		system("clear")
		system("tput setaf 3")
		print("\t\t\tWelcome to PARTITION PROGRAM")
		system("tput setaf 7")
		print("\t\t\t---------------------------")
		print("""
			Press 1: To Create Partition
    		Press 2: To Format partition
			Press 3: To Mount Partition
    		Press 4: To Delete Partition
    		Press 5: Go to main Menu 
    		""")
		optionChoice = input("Enter Your Choice : ")
		#print(optionChosen)
		if r =="local":
			if int(optionChoice) == 1 :
				print("All Available BLOCK DEVICES are Listed Below : ")
				os.system("lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT")
				while True:
					blockName = input("Select the BLOCK DEVICE to create PARTITION : ")
					blockNameCheck = subprocess.getstatusoutput("lsblk /dev/{0} ".format(blockName))
					if int(blockNameCheck[0]) == 0 :
						print("Specified Block Device {0} is successfully recognized....".format(blockName))
						break
					elif int(blockNameCheck[0]) == 32 :
						print("Failed to Recognize Specified Device {0}....".format(blockName))
				while True:
					partitionType = input("Type of partition (primary p /extended e ) : ")
					if partitionType == "p":
						print("Creating Primary Partition.....")
						break
					elif partitionType == "e":
						print("Creating Extended Partition.....")
						break
					else:
						print("Incorrect choice.....\nTry Again")
				while True:
					partitionNumber = input("Enter Partition Number(1-4) : ")
					if int(partitionNumber) >= 1 and int(partitionNumber) <= 4 :
						print("Creating Partition Number {0}....".format(partitionNumber))
						break
					else:
						print("Incorrect Choice...Try Again")

				firstSector = input("Enter the First Sector: ")
				partitionSize = input("Enter the Partition Size {Units: K,M,G,T,P} :")
				partitionCreation = subprocess.getstatusoutput("(echo o ; echo n ; echo {0} ; echo {1} ; echo {2} ; echo +{3} ; echo w ) | fdisk /dev/{4} ".format(partitionType,partitionNumber,firstSector,partitionSize,blockName))
				if int(partitionCreation[0]) == 0:
					print("Partition Successfully Created......")
					input("Press ENTER to CONTINUE ........")
				else:
					print("Partition can't be created.....")
			elif int(optionChoice) == 2 :
				print("All available Block Devices and their Partitions are Listed Below :")
				system("lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT")
				while True:
					partitionName = input("Enter the PARTITION NAME to Format it:")
					partitionNameCheck = subprocess.getstatusoutput("lsblk {0} ".format(partitionName))
					if int(partitionNameCheck[0]) == 0 :
						print("Specified partition {0} Successfully Recognized....".format(partitionName))
						formatType = input("Enter the Format FileSystem Type( ext2 / ext3 / ext4 ) : ")
						alertMessage = input("Do you want to Format Partition {0} with {1} FileSystem ([Y]es / [N]o):".format(partitionName,formatType))
						if alertMessage == "Y" or alertMessage == "yes" or alertMessage == "Yes" or alertMessage == "YES" :
							subprocess.getstatusoutput("mkfs.{0} /dev/{1} ".format(formatType,partitionName))
							print("Finally partition {0} is Formatted with {1}".format(partitionName,formatType))
							break
						else:
							print("Abort")
							break
					else :
						print("Failed to Recognize Specified partition {0}....".format(partitionName))
			elif int(optionChoice) == 3 :
				print("All Available Block Devices and its Partitions are : ")
				os.system("lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINT")
				while True:
							partitionName = input("Enter the PARTITION NAME to mount it:")
							partitionNameCheck = subprocess.getstatusoutput("lsblk /dev/{0}".format(partitionName))
							if int(partitionNameCheck[0]) == 0 :
								print("Specified partition successfully recognized....")
								break
							elif int(partitionNameCheck[0]) == 32:
								print("Failed to Recognize Specified partition....")
				while True:
							mountPoint = input("Enter the MountPoint Path: ")
							mountPointCheck = subprocess.getstatusoutput("ls -all {0} ".format(mountPoint))
							if int(mountPointCheck[0]) == 0 :
								subprocess.getstatusoutput("mount /dev/{0} {1}".format(partitionName,mountPoint))
								print("/dev/{0} is Successfully Mounted to {1}".format(partitionName,mountPoint))
								input("Press ENTER to CONTINUE")
								break
							else:
								print("Specified MountPoint do not exist\n")
								createMountPoint = input("Do you like to create specified Mountpoint([Y]es/[N]o): ")
								if createMountPoint == "y":
									subprocess.getstatusoutput("mkdir {0}".format(mountPoint))
									subprocess.getoutput("mount /dev/{0} {1}".format(partitionName,mountPoint))
									print("/dev/{0} is Successfully Mounted to {1}".format(partitionName,mountPoint))
									input("Press ENTER to CONTINUE")
									break
								else:
									print("Specify Correct MountPoint.....")


			elif int(optionChoice) == 4:
				print("All available block devices and its partitions are:")
				os.system("lsblk -o NAME,SIZE,MOUNTPOINT")
				while True:
					partitionName = input("Enter the partition name to be deleted:")
					partitionNameCheck = subprocess.getstatusoutput("lsblk /dev/{0}".format(partitionName))
					if int(partitionNameCheck[0]) == 0 :
						print("Specified device successfully recognized....")
						subprocess.getstatusoutput("umount {0}".format(partitionName))
						subprocess.getstatusoutput("echo d ; echo {0} ; echo w | fdisk /dev/{0}".format(partitionName))
						print("{0} partition is Successfully Deleted".format(partitionName))
						input("Press ENTER to CONTINUE")
						break
					elif int(partitionNameCheck[0]) == 32:
						print("Failed to Recognize Specified Partition..try again....")
			elif int(optionChoice) == 5 :
            			t = 2


			else:
            			print("Not Supported")


def hadoop():
	init_1 = 1
	while init_1 == 1:
                
		system("clear")
		print("Configured for Local Machine")
		print("\t\tSelect Operation to do\n")
		print("\t\t1. Hadoop Operations")		
		print("\t\t2. Go to Main Menu")			


		local_input = int(input("Choose one: "))
		if local_input == 2:
			init_1 = 2            
		elif local_input == 1:
			hadoop_init = 1
			while hadoop_init == 1:
				system("clear")
				print("\t\tHadoop Operations Selected\n")
                                        
				print("\t\t1. Install Hadoop")
				print("\t\t2. Configure as Datanode or Namenode")
				print("\t\t3. Start Hadoop (Datanode/Namenode)")
				print("\t\t4. Stop Hadoop (Datanode/Namenode)")
				print("\t\t5. Check Hadoop Report")
				print("\t\t6. Return to Menu")
				hadoop_input = int(input("Choose one of them: "))
                                        
				if hadoop_input == 1:
                                        
					#Check whether it is already installed or not
					install_check_hadoop = which("hadoop")
					install_check_java = which("java")
                                                
					java_filename = 'jdk-8u171-linux-x64.rpm'
					hadoop_filename = 'hadoop-1.2.1-1.x86_64.rpm'
                                                
					if install_check_java is not None:
						print("Java Hotspot (TM) Version is already installed")

					else:
						print("Not exist, Installation required")
                                                        
						sleep(1)

						path = input("Choose path for Java Hotspot (TM) Version RPM file: i.e (/): ")
                                            
						print("Installing Java Hotspot (TM) Version")
						system("rpm -ivh "+path+java_filename)

						print("Successfully Installed")
                                                        
						system("clear")

					if install_check_hadoop is not None:
						print("Hadoop is already installed")
					else:
						print("Not exist, Installation required")
                                                        
						sleep(1)
                                                        
						path = input("Choose path for Hadoop RPM file: i.e (/): ")
                                                                                                
						sleep(1)
						print("Installing Hadoop")
						system("rpm -ivh "+path+hadoop_filename+" --force")
                                                        
						print("Successfully installed")
                                                        
					system("clear")
                                                        
					hadoop_init == 1
                                                    
                                        
				elif hadoop_input == 2:
                                            
					system("clear")
					print("\t\tConfiguration of Hadoop\n")
                                                    
					asNode = input("Datanode (d) or Namenode (n): d/n: ")
                                                
					if asNode == 'd':
                                                    
                                                        
						asNode_folder = input("Enter Desired directory name (must be unique): ")
						system("mkdir /root/"+asNode_folder+"")
                                                        
						asNode_folder_prep = "/"+asNode_folder
                                                        
						asNode_ip = input("Enter Namenode IP Address: ")
                                                        
						fileDatanode = open("/etc/hadoop/hdfs-site.xml","w") 
						fData = ["<configuration> \n","<property> \n","<name>dfs.data.dir</name> \n","<value>",asNode_folder_prep,"</value> \n","</property> \n","</configuration>\n"]  
                             
						fileDatanode.writelines(fData) 
						fileDatanode.close() 
                                                    
						fileCore = open("/etc/hadoop/core-site.xml","w")
						fCore = ["<configuration> \n","<property> \n","<name>fs.default.name</name> \n","<value>hdfs://",asNode_ip,":9001</value> \n","</property> \n","</configuration>\n"]
                                                        
						fileCore.writelines(fCore)
						fileCore.close()
                                                        
						system("clear")
                                                        
						hadoop_init == 1
                                                        
						print("Successfully configured")
						sleep(1)
                                                    
					elif asNode == 'n':
                                                
						asNode_folder = input("Enter Desired directory name (must be unique): ")
						system("mkdir /root/"+asNode_folder+"")
                                                        
						asNode_folder_prep = "/"+asNode_folder
						#asNode_ip = input("Enter Namenode IP Address: ")
                                                        
						fileNamenode = open("/etc/hadoop/hdfs-site.xml","w") 
						fName = ["<configuration> \n","<property> \n","<name>dfs.name.dir</name> \n","<value>",asNode_folder,"</value> \n","</property> \n","</configuration>\n"]  
                             
						fileNamenode.writelines(fName) 
						fileNamenode.close() 
                                                    
						fileCore = open("/etc/hadoop/core-site.xml","w")
						fCore = ["<configuration> \n","<property> \n","<name>fs.default.name</name> \n","<value>hdfs://0.0.0.0:9001</value> \n","</property> \n","</configuration>\n"]
                                                        
						fileCore.writelines(fCore)
						fileCore.close()
                                                        
						system("hadoop namenode -format")
                                                        
					system("clear")
                                                        
					hadoop_init == 1
                                                        
					print("Successfully configured")
					sleep(1)
                                                    
				elif hadoop_input == 3:
                                          
					system("clear")
                                                
					node_service = input("Starting Datanode(d) or Namenode(n): (d/n): ")
                                                
					if node_service == 'd':
						system("hadoop-daemon.sh start datanode")
						break
                                                        
					elif node_service == 'n':
						system("hadoop-daemon.sh start namenode")
						break
                                                        
					else:
						print("Invalid Option")
                                                        
                                                           
                                                
					hadoop_init == 1
					system("clear")
                                                
                                                
                                            
                                        
                                            
				elif hadoop_input == 4:
                     	                       
					service_init = 1
					while service_init == 1:
                                                
						system("clear")
                                                    
						node_service = input("Stopping Datanode(d) or Namenode(n): (d/n): ")
                                                    
						if node_service == 'd':
							system("hadoop-daemon.sh stop datanode")
							break
                                                                
						elif node_service == 'n':
							system("hadoop-daemon.sh stop namenode")
							break
                                                            
						else:
							print("Invalid Option")
                                                                
							service_init = 1
					hadoop_init == 1                
					system("clear")    
                                                
                                                
				elif hadoop_input == 5:
                                            
					system("clear")
                                                
					print("Checking report")
					sleep(1)
                                                
					system("hadoop dfsadmin -report")
					hadoop_init == 1
					system("clear")  

				elif hadoop_input == 6:
					hadoop_init = 2     
                                        
				else:
					print("Invalid Option, Try Again!")
					init_1 = 1


ch = menu()
system("clear")
print("\n\n")
while ch!=16:
	system("clear")
	if ch == 1:
		from webbrowser import open_new_tab
		open_new_tab("https://www.linkedin.com/in/sanket-bari-061951b9/")
	elif ch == 2:
		from webbrowser import open_new_tab
		open_new_tab("https://www.google.com")
	elif ch == 3:
		print("Enter string you want machine to speak : ", end = "")
		v1 = input()
		v2 = "\""+v1+"\""
		system("espeak-ng  "+v2)
	elif ch == 4:
		import urllib.request
		try :
		    print("\n\tWait few seconds....")
		    stri = "https://www.google.co.in"
		    data = urllib.request.urlopen(stri)
		    print("\n\tConnected")
		except:
		    print ("\n\tNot Connected") 
	elif ch == 5:
		print("\n\t\t")
		system("cal -3")
		print("\n\n")
	elif ch == 6:
		system("gnome-terminal")
		system("clear")
	elif ch == 7:
		print("\n\n\t\tCurrent user is : ",end  = "")
		system("whoami")
	elif ch == 8:
		system("ps -aux")
	elif ch == 9:
		try:
			print("\n\nEnter username : ",end = "" )
			nm = input()
			system("useradd "+nm)
			print("\n\n")
			system("passwd "+nm)
			print("\n\nAccount created successfully....")
		except:
			pass
	elif ch == 10:
		try:
			print("\n\n\tEnter username you want to delete : ", end = "")
			nm1 = input()
			system("userdel --remove "+nm1)
			print("\n\n")
		except:
			pass

	elif ch == 11:
		ch1 = menu2()
		while ch1 != 6:
			if(ch1 == 100):
				print("\n\n\t\tIncorrect choice... try again...")
				sleep(1)
				
				
			
			elif(ch1 == 1):
				system("clear")
				print("\n\n\n\tEnter file name in which you want to insert data\n\n\t\teg. file1\n\n Enter file name : ",end = "")
				filenm = input()
				if(filenm != ""):
					system("gedit "+ filenm + ".txt")
			elif(ch1 == 2):
				system("clear")
				print("\n\n\n\tEnter file name which you want to edit\n\n\t\teg. file1\n\n Enter file name : ",end = "")
				filenm = input()
				if(filenm != ""):
					system("cat "+ filenm + ".txt")
				print("\n\n\tPress enter key to continue... ")
				c = input()
			elif(ch1 == 3):
				system("clear")
				print("\n\n\n\tEnter file name which you want to delete : ",end = "")
				filenm = input()
				if(filenm != ""):
					system("rm "+ filenm + ".txt")
				print("\n\n\tPress enter key to continue... ")
				c = input()
			elif(ch1 == 4):
				system("clear")
				print("\n\n\n\tEnter existing file name : ",end = "")
				aaa = input()
				if(aaa!= ""):
					print("\n\tEnter file name in which you want to copy : ", end = "")
					bbb = input()
					if(bbb!=""):
						system("cat < "+ aaa + ".txt"+" > "+bbb+".txt")
	
			elif(ch1 == 5):
				system("clear")
				
				print("\n\n\n\tFollowing operaton will happen\n\n\t\tf1 + f2 will be printed\n\n\tEnter first file name : ",end = "")
				aaa = input()
				if(aaa!= ""):
					print("\n\tEnter second file name : ", end = "")
					bbb = input()
					if(bbb != ""):
						system("cat  "+ aaa + ".txt"+" "+bbb+".txt")	
				print("\n\n\tPress enter key to continue... ")
				c = input()
			ch1 = menu2()
	elif ch == 12:
		ch2 = menu3()
		while(ch2!=11):
			if(ch2 == 100):
				print("\n\n\t\tIncorrect choice... try again...")
				sleep(1)

			elif(ch2 == 1):
				system("clear")
				x = system("systemctl start docker")
				if(x == 0):
					print("Docker started successfully")
					
					sleep(5)
					system("clear")
					print("\n\n\tPress enter key to continue... ")
					c = input()

			elif(ch2 == 2):
				system("clear")
				x = system("docker images")
				print("\n\n\tPress enter key to continue... ")
				c = input()

			elif(ch2 == 3):
				system("clear")
				system("docker ps")
				print("\n\n\tPress enter key to continue... ")
				c = input()

			elif(ch2 == 4):
				system("clear")
				x = input("Enter the name of image to be searched...")
				print(x)
				y = "docker search " + x
				system(y)
				print("\n\n\tPress enter key to continue... ")
				c = input()

			elif(ch2 == 5):
				system("clear")
				x = input("Enter name of the image to be pulled from docker repo,,,")
				y = "docker pull" + x
				system(y)
				print("\n\n\tPress enter key to continue... ")
				c = input()

			elif(ch2 == 6):
				system("clear")
				x = input("Enter the image name... ")
				y = input("Enter the name you want to give to the container...")
				z = "docker container run -td --name" + " " + y + " " + x
				system(z)
				
				print("\n\n\tPress enter key to continue... ")
				c = input()

			elif(ch2 == 7):
				system("clear")
				x = input("Enter the container name to be inspected... ")
				y = "docker inspect " + x
				system(y)
				
				sleep(5)
				print("\n\n\tPress enter key to continue... ")
				
			elif(ch2 == 8):
				system("clear")
				x = input("Enter the container name in which You want to execute the command.../t")
				y = input("Enter the command to be executed...")
				z = "docker container exec " + x + " "+ y
				system(z)
				
				sleep(5)
				print("\n\n\tPress enter key to continue... ")
			
			elif(ch2 == 9):
				system("clear")
				x = input("Enter container name to be stopped....")
				y = "docker stop " + x
				system(y)
				print("\n\n\tPress enter key to continue... ")	

			elif(ch2 == 10):
				system("clear")
				x = system("systemctl stop docker")
				if x == 0:
					print("Docker stopped successfully...")
					
					sleep(5)			
			ch2 = menu3()						
	
	elif ch == 13:
		ch3 = menu4()
		while ch3!=10:
			if(ch3 == 100):
				print("\n\n\t\tIncorrect choice... try again...")
				
				sleep(1)

			elif(ch3 == 1):
				system("clear")
				print("You must check internet connectivity before continuing....")
				system("clear")
				
				sleep(5)
				print("Enter Y if internet connectivity is there ...Otherwise enter N")
				x = input()
				system("clear")
				if(x == 'Y'):
					system("clear")
					system('curl "{}" -o "{}"'.format('https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip','awscliv2.zip'))
					system("clear")
					sleep(2)
					system("unzip awscliv2.zip")
					system("clear")
					system("sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")
					system("clear")
					r = system("aws --version")
					print(r)
					sleep(5)
					if(r == 0):
						print("awscli2 installed Successfully...ready to use...")
						sleep(10)
					print("\n\n\tPress enter key to continue... ")
			elif ch3 == 2:
				system("clear")
				print("Please provide Your aws_access_key_id eg. AKIARXBXJXQWESDER....")
				y = input()
				system("clear")
				system("aws configure set aws_access_key_id {}".format(y))
	
				print("Please provide your aws_secret_access_key eg. M8OFqsoshfyrvSdehn")
				y = input()
				system("aws configure set aws_secret_access_key {}".format(y))

				print("Please provide your region eg. ap-south-1")
				y = input()
				system("aws configure set region {}".format(y))
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 3:
				system("clear")
				
				system("aws ec2 describe-volumes > aws.txt")
				sleep(2)
				system("cat aws.txt")
				sleep(7)
				system("clear")
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 4:
				system("clear")
				
				print("Enter key name to create:-",end='')
				y=input()
				system("aws ec2 create-key-pair --key-name {}".format(y))
				sleep(2)
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 5:
				system("clear")
				
				print("Enter key name to be deleted:-",end='')
				y = input()
				system("aws ec2 delete-key-pair --key-name {}".format(y))
				sleep(3)
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 6:
				system("clear")
				
				print("Enter security group name:--",end='')
				y = input()
				print("Enter VPC Id:-",end='')
				x = input()
				system('aws ec2 create-security-group --group-name {} --description "Security group created" --vpc-id {}'.format(y,x))
				sleep(2)				
				system("clear")
				print("For Security group rules...")
				print("Enter Security Group Id:-",end='')
				x = input()
				print("Enter IP Protocol eg. tcp,dhcp etc:-",end='')
				ip = input()
				print("Enter Port No:-",end='')
				port = input()
				print("Input Ip Ranges :-",end='')
				ip_range_cidr = input()				
				system("aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions  			IpProtocol={},FromPort={},ToPort={},IpRange=[{}]".format(x,ip,port,port,ip_range_cidr))
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 7:
				system("clear")
				
				print("Enter AMI Id:--",end='')
				AMI = input()
				print("Enter Instance type:--",end='')
				Itype = input()
				print("Enter Number of instances to launch:- ",end='')
				No_In = input()
				print("Enter Subnet id:- ",end='')
				Sub_id = input()
				print("Enter security group Id:--",end='')
				sg_id = input()
				print("Enter key to attach to ec2 instance:-",end='')
				key = input()
				system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(AMI,Itype,No_In,Sub_id,sg_id,key))
				print("\n\n\tPress enter key to continue... ")			
			elif ch3 == 8:
				system("clear")
				print("Enter Avaibility zone to create ebs volume:- ",end='')
				x = input()
				print("Enter size for ebs volume:--",end='')
				y = input()
				system("aws ec2 create-volume --availability-zone {} --size {}".format(x,y))
				print("\n\n\tPress enter key to continue... ")
			elif ch3 == 9:
				system("clear")
				print("Enter EBS volume id to attach to ec2 instance:--",end='')
				x = input()
				print("Enter ec2 instance id --",end='')
				y = input()
				system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(x,y))
				print("\n\n\tPress enter key to continue... ")				
			ch3 = menu4()	

	elif ch == 14:
		system("clear")
		hadoop()

	elif ch == 15:
		system("clear")
		partition()
		
	else:
		print("\n\n\tIncorrect choice... ")	

		
	ch = menu()

system("tput setaf 11") 
print("\n\t----- Thank You -----\n\n")
normal_colours()
system("espeak-ng  \"thaank you!\"")
system("killall bash livedate") 
remove("livedate")
system("clear")
