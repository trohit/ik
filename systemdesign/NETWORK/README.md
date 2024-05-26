# Terminology
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
