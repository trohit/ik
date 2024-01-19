# IPv6
- [IPv6](https://en.wikipedia.org/wiki/IPv6) has 128 bit addrs. made in 1998 to deal with IPv4 addr exhaustion
- tot addrs: 2^128, respresented as eight groups of four hex digits each. OR 8 groups of 16bits each.
- eg.  2001:0db8:0000:0000:0000:8a2e:0370:7334
- addressing arch of IPv6 defined in [RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291)
- 3 diff kinds of transmission in IPv6: unicast, multicast, anycast
- 3 diff kinds of transmission in IPv4: unicast, multicast, broadcast
- loopback IPv6 addr: [::1] in IPv4 loopback: 127.0.0.1
- features of IPv6
	- can support 4GB jumbograms as max_pkt_size: 2^32-1 vs IPv4 max_pkt_size: 2^16-1= 655535 bytes
	- unlike IPv4, routers never frag an IPv6 pkt, instead IPv6 hosts expected to use PMTU to make pkts small enough not to need fragmentation.
	- Anycast delivers a message to any one out of a group of nodes, typically the one nearest to the source using a one-to-one-of-many association where datagrams are routed to any single member of a group of potential receivers that are all identified by the same destination address. The routing algorithm selects the single receiver from the group based on which is the nearest according to some distance or cost measure.
	
- uses of IPv6
	- IPv6 renders CIDR and NATing obosolete
	- instead of DHCP, IPv6 supports SLAAC( stateless addr auto-config) where IPv6 hosts self-generates unique IPv6 ips 
	- IPSec orig dev for IPv6 but found widespread adoption in IPv4.
- examples
	- unicast IPv6 addrs
		- Global : 2000::/3
		- Link local: fe80::/10
		- loopback: ::1/128
    - ULA uniq local : read RFC 4193
      - 1st half of ULA fc00::/8, is reserved for a future global authority to assign.
      - 2nd half of the ULA address range, fd00::/8, can be assigned locally, with restrictions. The next 40 bits must be randomly chosen, and you cannot assign prefixes in any particular order.
		- embedded IPv4 ::/80
	- multicast IPv6
		- well known: ff00::/12
		- transient: ff10::/12
	- anycast
		- 

# References
- https://www.nwkings.com/types-of-ipv6-addresses
