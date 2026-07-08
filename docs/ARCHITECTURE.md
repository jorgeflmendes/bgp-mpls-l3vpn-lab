# Architecture Notes - BGP/MPLS L3VPN Lab

## Lab Topology

The GNS3 topology has customer edge routers for blue and red tenants, provider edge routers PE1/PE2, and a provider core router P. OSPF and LDP build the underlay; MP-BGP VPNv4 transports tenant routes.

## Evidence Flow

Router configuration sessions, verification outputs, ping/traceroute results, and tshark summaries are included. Raw PCAPs are excluded.

## Publication Boundary

The repository keeps report source and selected reviewed evidence. It deliberately excludes:

- IOS image files
- raw PCAP captures
- course slides/guides
- temporary convergence/debug logs
- local GNS3 state

## Reproduction Assumptions

The lab was executed in GNS3 using Cisco/GNS3 appliances and Linux containers. Re-running the full topology requires local access to those appliances and the original lab guide.
