#!/usr/bin/env python
import socket
import threading
import getpass

def recieve_message_thread():
    while True:
        message_recieved = client_socket.recv(1024)
        if message_recieved == 'exit' or message_recieved == '':
            print 'User disconnected'
            client_socket.close()
            break
        
        else:
            print message_recieved
        
    return


if __name__ == '__main__':
     Username = raw_input('Username: ')
     client_socket = socket.socket()
     client_socket.connect(('localhost', 9005))
     client_socket.send(Username)
     recieve_message_thread = threading.Thread(target = recieve_message_thread)
     recieve_message_thread.daemon = True
     recieve_message_thread.start()
     while True:
          Message_to_send = raw_input()
          if (Message_to_send.lower() == 'exit'):
               client_socket.send('exit')
               sever_socket.close()
               exit()
     
          else:
               Response = Username + ':' + Message_to_send
               client_socket.send(Response)
