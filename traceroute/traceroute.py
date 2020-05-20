# -*- coding: utf-8 -*-
import socket
import requests
import traceback

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)

def traceroute(ip, port):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 1
    while True:
        udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)

        # trimite un mesaj UDP catre un tuplu (IP, port)
        udp_send_sock.sendto(b'salut', (ip, port))

        # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
        # in cazul nostru nu verificăm tipul de mesaj ICMP
        # puteti verifica daca primul byte are valoarea Type == 11
        # https://tools.ietf.org/html/rfc792#page-5
        # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header
        addr = 'done!'
        # noinspection PyInterpreter
        try:
            data, addr = icmp_recv_socket.recvfrom(63535)
            fake_HTTP_header = {
                'referer': 'https://ip-api.com/',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
            }
            raspuns = requests.get('http://ip-api.com/json/' + addr[0], headers=fake_HTTP_header)
            data = raspuns.json()
            city = data['city']
            region = data['region']
            country = data['country']
            print(addr[0])
            print("City: " + city)
            print("Region: " + region)
            print("Country: " + country)
            print()
        except Exception as e:
            print("Socket timeout ", str(e))
            print(traceback.format_exc())
            print()
        if addr[0] == ip:
            print(addr[0])
            print("YESS")
            break
        TTL += 1

traceroute('36.110.213.10', 33434)
print("Done first traceroute")
traceroute('130.102.184.3', 33434)
print("Done second traceroute")
traceroute('196.21.45.86', 33434)
print("Done third traceroute")