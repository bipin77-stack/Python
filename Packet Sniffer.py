import socket
import struct
import textwrap

def  main():
    HOST = '192.168.1.183'
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    conn.bind((HOST, 0))

    while True:
        raw_data, _ = conn.recvfrom(65000)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\n Ethernet_frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))


# Unpack Ethernet Frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

# Return properly formatted mac-address(AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


main()

