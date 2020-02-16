import socket
from threading import Thread
# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def portchecker(port):
		# First we need to create a socket obect
	sock = socket.socket()
	# We then get the local hosts name. This would be the remote servers IP if we were not on the local host already
	host = socket.gethostname()
	# We now set the port we will be using
	
	# Now we issue a connection to the server

	
	result = sock.connect_ex((host, port))

	# Now we recieve the data sent to use
	if(result == 0):
		print('Port {0} is opened \n'.format(port))
		
		# Close the socked connection
	sock.close()




def main():
		print('Enter range of ports you want to scan')
		port1 = input('enter First port: ')
		port1 = int(port1)
		#last port index
		port2 = input('enter Last port: ')
		port2 = int(port2)
		#array to hold all the working trheads
		threads = []
		for i in range(port1,port2+1):
		    t = Thread(target=portchecker, args=(i,))
		    threads.append(t)
		    t.start()

		



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()
