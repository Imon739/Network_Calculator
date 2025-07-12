import ipaddress

def main():
    ip_with_prefix = input("Enter IP address with prefix (e.g. 192.168.1.10/24): ")

    try:
        net = ipaddress.IPv4Interface(ip_with_prefix).network

        print(f"\nSubnet Address:     {net.network_address}")
        print(f"Broadcast Address:  {net.broadcast_address}")
        print(f"Subnet Mask:        {net.netmask}")
        print(f"CIDR Notation:      {net.with_prefixlen}")
        print(f"Number of Hosts:    {net.num_addresses - 2}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()