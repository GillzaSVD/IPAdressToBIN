import sys

ip = input('Введите ip: ')
mask = input('Введите маску: ')
space = ''

parts = map(int, ip.split('.'))
for part in parts:
    if part > 255 or part < 0:
        print('Неправильный адрес ip')
        sys.exit()

def zamena(addr):
    return addr.replace('0', '#').replace('1', '0').replace('#', '1')

def to_bin(addr):
    a1, a2, a3, a4 = map(int, addr.split('.'))
    return f'{a1:08b}{a2:08b}{a3:08b}{a4:08b}'

full_ip = to_bin(ip)
full_mask = to_bin(mask)

address_bin = f'{full_ip[0:8]}.{full_ip[8:16]}.{full_ip[16:24]}.{full_ip[24:32]}'
netmask_bin = f'{full_mask[0:8]}.{full_mask[8:16]}.{full_mask[16:24]}.{full_mask[24:32]}'

bitmask = netmask_bin.count('1')

wildcard_bin = f'{int(zamena(full_mask[0:8]), 10):08}.{int(zamena(full_mask[8:16]), 10):08}.{int(zamena(full_mask[16:24]), 10):08}.{int(zamena(full_mask[24:32]), 10):08}'
wildcard_dec = f'{int(zamena(full_mask[0:8]), 2)}.{int(zamena(full_mask[8:16]), 2)}.{int(zamena(full_mask[16:24]), 2)}.{int(zamena(full_mask[24:32]), 2)}'

net_addr = full_ip[0:bitmask] + ('0' * (32 - bitmask))
hosts_addr = full_ip[0:bitmask] + ('1' * (32 - bitmask))

network_dec = f'{int(net_addr[0:8], 2)}.{int(net_addr[8:16], 2)}.{int(net_addr[16:24], 2)}.{int(net_addr[24:32], 2)}'
network_bin = f'{net_addr[0:8]}.{net_addr[8:16]}.{net_addr[16:24]}.{net_addr[24:32]}'

broadcast_dec = f'{int(hosts_addr[0:8], 2)}.{int(hosts_addr[8:16], 2)}.{int(hosts_addr[16:24], 2)}.{int(hosts_addr[24:32], 2)}'
broadcast_bin = f'{hosts_addr[0:8]}.{hosts_addr[8:16]}.{hosts_addr[16:24]}.{hosts_addr[24:32]}'

host_min_bin = f'{net_addr[0:8]}.{net_addr[8:16]}.{net_addr[16:24]}.00000001'
host_min_dec = f'{int(host_min_bin[0:8], 2)}.{int(host_min_bin[9:17], 2)}.{int(host_min_bin[18:26], 2)}.1'

host_max_bin = f'{hosts_addr[0:8]}.{hosts_addr[8:16]}.{hosts_addr[16:24]}.11111110'
host_max_dec = f'{int(host_max_bin[0:8], 2)}.{int(host_max_bin[9:17], 2)}.{int(host_max_bin[18:26], 2)}.254'

hosts = 2 ** (32 - bitmask) - 2

print(f'|Address:\t|{ip:^30}|{address_bin:^50}|')
print(f'|Bitmask:\t|{bitmask:^30}|{space:^50}|')
print(f'|Netmask:\t|{mask:^30}|{netmask_bin:^50}|')
print(f'|Wildcard:\t|{wildcard_dec:^30}|{wildcard_bin:^50}|')
print(f'|Network:\t|{network_dec:^30}|{network_bin:^50}|')
print(f'|Broadcast:\t|{broadcast_dec:^30}|{broadcast_bin:^50}|')
print(f'|HostMin:\t|{host_min_dec:^30}|{host_min_bin:^50}|')
print(f'|HostMax:\t|{host_max_dec:^30}|{host_max_bin:^50}|')
print(f'|Hosts/Net:\t|{hosts:^30}|{space:^50}|')
