# Terminology
# Basic IP cmds
    # ip addr in brief
    ip -br a

    # show IPV4 addrs in color 'c'
    ip -4 -br -c a
    
    # show ipv4 addrs in one line
    ip -4 -o a

    # show routes nicely
    ip -c r | column -t

    # del default route
    ip r delete default
   
# Network Namespaces
## List network namespace
    ip netns

## Create a network namespace
    ip netns add red
    ip netns add blue

## Execute a cmd in network namespace

    # Normal execution of a cmd
    ip link
    
    # Execution of same cmd in n/w ns
    ip netns exec red ip link
    
    # Another Alternative
    ip -n red link

    # arp
    arp
    ip netns exec red arp
    ip -n red arp

    # route
    ip netns exec red route

## connect 2 namespaces by adding veth pair
![image](https://github.com/trohit/ik/assets/466385/b584ab2e-11b8-4ec6-9225-de2a6b7b1d5e)
https://www.youtube.com/watch?v=j_UUnlVC2Ss&t=434s

    # create veth pair
    ip link add veth-red type veth peer name veth-blue

    # connect veth-pair to namespaces
    ip link set veth-red  netns red
    ip link set veth-blue netns blue

    # assign addresses
    ip -n red  addr add 192.168.15.1 dev veth-red
    ip -n blue addr add 192.168.15.2 dev veth-blue

    # bring veth-pair up
    ip -n red  link set veth-red  up
    ip -n blue link set veth-blue up

    # test connectivity of veth-pair
    ip netns exec red ping 192.168.15.2 

    # check namespace arp entries
    ip netns exec red  arp
    ip netns exec blue arp

    # connect network namespaces to exeternal world : using either linux bridge or OpenVSwitch
    
    # Linux bridge way to connect namespaces to external/ host network

    ## first create a bridge
    ip link add vnet0 type bridge
    ip link
    ip link set dev vnet0 up

    # delete the veth pair, deleting any one endpoint automatically deletes the other endpoint
    ip -n red link del veth-red

    # create veth pairs that will connect netns to bridge
    ip link add veth-red type veth peer name veth-red-br
    ip link add veth-blue type veth peer name veth-blue-br
    ip link set veth-red-br  up
    ip link set veth-blue-br up

    # connect veth pair endpoints one to ns and other end to bridge if
    ip link set veth-red    netns red
    ip link set veth-red-br master vnet0

    ip link set veth-blue   netns blue
    ip link set veth-blue-br master vnet0

    # assign ip addrs to veth pairs and the vnet bridge
    ip -n red addr add 192.168.15.1/24 dev veth-red
    ip -n red addr add 192.168.15.2/24 dev veth-red
    ip addr add 192.168.15.5/24 dev vnet0
    
    # bring up the veth-pair
    ip -n red  link set veth-red  up
    ip -n blue link set veth-blue up

![image](https://github.com/trohit/ik/assets/466385/68c68d38-7694-48e3-b83f-00fac2cd0626)

![image](https://github.com/trohit/ik/assets/466385/30fc1948-a472-48ce-9c09-9ffd971ec19d)

## pinging from within n/w ns to external n/w

    ip netns exec blue ping 192.168.1.3
    ip netns exec blue route
    ip netns exec blue route add 192.168.1.0/24 via 192.168.15.5

![image](https://github.com/trohit/ik/assets/466385/80484202-c5dc-4690-a015-e7e55d92abcc)

## for reaching the external n/w using NAT and ip forwarding, enable this on host gateway

    iptables -t NAT -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE
    sysctl -w net.ipv4.ip_forward=1

## to allow hosting http server from within the container namespace to external world use NAT on host gateway
    iptable -t NAT -A PREROUTING --dport 80 --to-destination 192.168.15.2:80 -j DNAT


# Iptables cmds

## to list iptables

## to flush iptables


    
## 
# [Zero conf networking](https://en.wikipedia.org/wiki/Zero-configuration_networking)
## APIPA vs SLAAC
- Usually DHCP server helps auto configure Ip on a node. but if DHCP fails node can remain without an IP.
- APIPA : Automatic pvt IP addressing :
  - mechanism that runs on all Win systems that guarantees that when DHCP server fails, node will still get a [link local IP address](https://en.wikipedia.org/wiki/Link-local_address).
  - Addresses used in APIPA
    - Both IPv4
      - IPv4 unicast: 169.254.x.x/16
        - The entire range may be used for this purpose 169.254.0.0 – 169.254.255.255
        - except for the first 256 and last 256 addresses (169.254.0.0/24 and 169.254.255.0/24), reserved for future use and must not be selected by a host using this dynamic configuration mechanism.
        - Link-local addresses are assigned to interfaces by host-internal, i.e. stateless, address autoconfiguration when other means of address assignment are not available.
        - Before auto assigning a node checks for DHCP server and then does ARP to see if the candidate link local addr it desires to assign is already taken.
 
      - IPv4 multicast : 224.0.0.0/24
    - and IPv6 link local addrs supported
      - IPv6 local unicast : fe80::/10
      - IPv6 local multiicast : ff02::/16
  - SLAAC: Stateless address auto-config 
# factors to consider when choosing network
- throughout
- latency
- jitter
- packet loss
- availability & reliability

# Mechanisms for HA and Fast failover on the web  
- can use anycast instead of a LB : [Cloudflare](https://blog.cloudflare.com/cloudflares-architecture-eliminating-single-p/) and Dukaan use anycast for zero failover time
