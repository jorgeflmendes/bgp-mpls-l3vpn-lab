# Architecture

PE1, P, and PE2 form an OSPF/LDP provider core. PE1 and PE2 run MP-BGP VPNv4 between loopbacks `1.1.1.1` and `2.2.2.2`.

Blue uses RD/RT `1:1`; red uses RD/RT `2:2`. The customer loopbacks are `192.168.101.0/24` and `192.168.102.0/24` for blue, and `192.168.111.0/24` and `192.168.112.0/24` for red.
