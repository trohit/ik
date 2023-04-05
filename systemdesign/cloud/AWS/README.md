# AZ
- one or more DCs that share power|networking|cooling, so share same failure domain
- each az is separate from the other in that if one fails the other should still be up.
- eg. us-east-1[a|b|c]

# VPC

- a logical contruct that overlays across all az's in a region
- a vpc can have subnets in multiple AZ's
- not restricted to single subnet per AZ.
- traffic between diff subnets in the same AZ is called intra-zone(not charged)
- traffic between diff subnets across AZ's is called inter-zone traffic.(chargeable)
- When creating a VPC need to specify CIDR range (/16 | /28) for that VPC to use.
  - /16 gives 2^(32 -'16' - 2 => 65534 usable IPv4 IPs
  - /28 gives 2^(32 -'28' - 2 => 2 usable IPs.
  - RFC 1918 CIDR addrs preferred
    - 10.x.y.z/8 | 192.168.x.y/16 | 172.168.0.0/12
    - In each subnet we create in a VPC, AWS reserves 5 of those usable IPs.    
    - ![image](https://user-images.githubusercontent.com/466385/230108842-43cea789-bfbc-4f4d-ad4e-ea4771745632.png)
  - see CIDR cheatsheet at 
    - https://pbxbook.com/other/cidrcheat.html
    - https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/
  -    
