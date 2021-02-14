from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    mserver = (mailserver,port)

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mserver)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print("Message after connection request:" + recv)
    #if recv[:3] != '220':
     #   print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'EHLO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print("Message for HELO command:"+ recv1)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM: <so2170@nyu.edu> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    #print ("After Mail from command:" + recv2)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO: <saritha0203@yahoo.com> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    #print("After RCPT from command:" + recv3)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = "DATA \r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    #print("After DATA from command:" + recv4)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')
    # Fill in end
    # Fill in end

    # Send message data.
    # Fill in start
    subject= "Subject: SMTP mail client testing \r\n"
    clientSocket.send(subject.encode())
    message = "SMTP mail client body \r\n"
    clientSocket.send(message.encode())
    recv5 = clientSocket.recv(1024)
    #print("After message data from command:" + recv5)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send("\r\n.\r\n".encode())
    recv6 = clientSocket.recv(1024)
    #print("After single period from command:" + recv6)
    #if recv1[:3] != '250':
     #   print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    clientSocket.send("Quit\r\n".encode())
    recv7 = clientSocket.recv(1024)
    #print("After Quit command:" + recv7)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
