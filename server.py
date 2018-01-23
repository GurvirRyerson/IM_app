#!/usr/bin/env python
import threading
import datetime
import socket
username_dictionary = {}
connection_list = []

def send_to_all_clients(message, client_sending):
    print "made it to send_to_all_clients function"
    num = 0
    for client in connection_list:
        if (client != client_sending):
            print message
            client.sendall(message)
        
    return


def communication_thread(connection_object, address):
    Username = connection_object.recv(1024)
    username_dictionary[address] = str(address[0])
    username_dictionary[Username] = Username
    #to_send = 'Ip address:' + username_dictionary[Username] + ' Username:' + username_dictionary[addr]
    print "Succes up to while loop in thread"
    while True:
        message_in = connection_object.recv(1024)
        print "success in recieving a message"
        if message_in.lower() == 'exit' or not message_in:
            if connection_object in connection_list:
                connection_list.remove(connection_object)
                print "Sucess in ending the thread"
                
            break

        else:
            current_datetime = str(datetime.datetime.now())
            message_out = ' '+ current_datetime  + ': ' + message_in
            send_to_all_clients(message_out, connection_object)
            
    connection_object.close()
    print "Thread closed"
    return
    


if __name__ == '__main__':
    #socket.setdefaulttimeout(15)
    #Used to get ip address of machine, gethostbyname is giving me 127.0.1.1
    #print "what"
    #ip_address_socket = socket.socket()
    #ip_address_socket.connect(('google.com', 80))
    #host = ip_address_socket.getsockname()[0]
    #print host
    #ip_address_socket.close()
    
    server_socket = socket.socket()
    server_socket.bind(('localhost', 9005))
    server_socket.listen(5)
    num = 1
    
    #Currently just chills waiting on another connection in the while loop
    #Not sure if i want it to close the server when there are no new connections after a while or what
    #Currently thinking of leaving it open to new connections
    while True:
        c, addr = server_socket.accept()
        connection_list.append(c)
        communication_thread_object = threading.Thread(target = communication_thread, kwargs ={'connection_object': c, 'address': addr})
        communication_thread_object.start()
        #to_send = 'Ip address:' + username_dictionary[Username] + ' Username:' + username_dictionary[addr]
        #print to_send

    server_socket.close()
    
