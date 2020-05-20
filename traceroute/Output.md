# Soluție

## 1. Traceroute

Am implementat soluția iar aici este output-ul:

### Ruta către IP1
```
Output-ul programului pentru ip-ul '36.110.213.10' al unui site din China cu extensia .cn


209.85.244.30
City: Newark
Region: NJ
Country: United States

172.253.64.170
City: Englewood
Region: CO
Country: United States

108.170.241.5
City: Ashburn
Region: VA
Country: United States

202.97.62.213
City: Beijing
Region: BJ
Country: China

202.97.63.121
City: Beijing
Region: BJ
Country: China

202.97.14.245
City: Shenzhen
Region: GD
Country: China

202.97.34.157
City: Beijing
Region: BJ
Country: China

Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-4-ec898e800cdb>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

36.110.238.10
City: Beijing
Region: BJ
Country: China

Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-4-ec898e800cdb>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out


36.110.213.10
City: Beijing
Region: BJ
Country: China
```

### Ruta către IP2
```
Output-ul programului pentru ip-ul '130.102.184.3' al unui site din Australia cu extensia .au


172.253.50.216
City: Ashburn
Region: VA
Country: United States

209.85.251.141
City: Newark
Region: NJ
Country: United States

172.253.79.101
City: Englewood
Region: CO
Country: United States

108.170.247.57
City: Ashburn
Region: VA
Country: United States

Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-3-776065ba1e6f>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out


113.197.15.17
City: Caulfield
Region: VIC
Country: Australia

138.44.129.158
City: Brisbane
Region: QLD
Country: Australia

130.102.159.58
City: Saint Lucia
Region: QLD
Country: Australia

130.102.159.61
City: Saint Lucia
Region: QLD
Country: Australia

Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-3-776065ba1e6f>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out


Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-3-776065ba1e6f>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out

130.102.184.3
City: Saint Lucia
Region: QLD
Country: Australia
```

### Ruta către IP3
```
Output-ul programului pentru ip-ul '196.21.45.86' al unui site din Africa cu extensia .za


142.250.224.58
City: Ashburn
Region: VA
Country: United States

72.14.239.154
City: Ashburn
Region: VA
Country: United States

72.14.234.8
City: Ashburn
Region: VA
Country: United States

216.239.57.197
City: Broken Arrow
Region: OK
Country: United States

172.253.65.165
City: Englewood
Region: CO
Country: United States

64.233.175.112
City: Ashburn
Region: VA
Country: United States

172.253.67.160
City: Englewood
Region: CO
Country: United States

209.85.253.247
City: Ashburn
Region: VA
Country: United States

Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-5-23fbe8aabced>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out


Socket timeout  timed out
Traceback (most recent call last):
  File "<ipython-input-5-23fbe8aabced>", line 30, in traceroute
    data, addr = icmp_recv_socket.recvfrom(63535)
socket.timeout: timed out


155.232.128.135
City: Cape Town
Region: WC
Country: South Africa

155.232.1.67
City: Pretoria
Region: GP
Country: South Africa

155.232.64.61
City: Cape Town
Region: WC
Country: South Africa

155.232.64.86
City: Cape Town
Region: WC
Country: South Africa

155.232.64.138
City: Cape Town
Region: WC
Country: South Africa

155.232.27.237
City: Cape Town
Region: WC
Country: South Africa

196.11.235.1
City: Cape Town
Region: WC
Country: South Africa

196.21.45.86
City: Bellville
Region: WC
Country: South Africa

```