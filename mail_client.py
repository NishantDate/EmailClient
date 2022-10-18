from socket import *
msg = "SUBJECT: Neccessary Security Steps Taken :) \r \n \n\n  "
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "imap.nyu.edu"
serverport = 25
# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)
print(f"Attempting to connect to mailserver {mailserver} at port {serverport} ... ")
clientSocket.connect((mailserver, serverport))

recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
	print ("220 reply not received from server.")


heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
 print ("250 reply not received from server.")

# Send MAIL FROM command and print server response.
mailCommand = 'MAIL FROM: <asm717@nyu.edu>\r\n'
clientSocket.send(mailCommand)

recv1 = clientSocket.recv(1024)
print(recv1)

# Send RCPT TO command and print server response.

RCTPCommand = 'RCPT TO: <nishantdate@gmail.com>\r\n'
clientSocket.send(RCTPCommand)
recv1 = clientSocket.recv(1024)
print(recv1)

# Send DATA command and print server response.

clientSocket.send('DATA\r\n')

recv1 = clientSocket.recv(1024)
print(recv1)


# Send message data.
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)

# Send QUIT command and get server response.
clientSocket.send('QUIT')

recv1 = clientSocket.recv(1024)



