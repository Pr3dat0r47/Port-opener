import socket
from threading import Thread

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def openport(port):
	try:
			# First we need to create a socket obect
		sock = socket.socket()

		# We then get the local hosts name
		host = socket.gethostname()

		# Next we need to bind the port and reserve it on the system
		sock.bind((host, port))

		# We will now listen for any connection with a max of 5 
		sock.listen(5)

		# We now run the while loop to consistantly check for connections and send back a response
		while True:

			# Establish a connection with the client
			client, address = sock.accept()

			print('Connection From {0}'.format(address))
			# We now send data over to the client
			client.send('Recieved a connection! Closing!')

			# We now close the connection
			client.close()
	except Exception as e:
		raise e
	

def main():
	#start port index
	print('Enter range of ports you want to start')
	port1 = input('enter First port: ')
	port1 = int(port1)
	#last port index
	port2 = input('enter Last port: ')
	port2 = int(port2)
	#array to hold all the working trheads
	threads = []
	for i in range(port1,port2+1):
	    t = Thread(target=openport, args=(i,))
	    threads.append(t)
	    t.start()

	numberof_ports = port2 - port1
	print('You have {0} ports Opened from {1} - {2} '.format(numberof_ports,port1,port2))

	




# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()