# BEAVER / neutron — Schema 与业务口径解释

该数据库的存档目录包含 175 张表、819 个物理列、183 条关系，以及 444 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## address_scopes

Stores definitions of address scopes, which are named collections of IP addresses or subnets used for network segmentation and policy application within a tenant.

恢复表名: address scopes / address scope / ip address scopes / network address scopes / address scope definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| address_scopes.id | id / identifier / address scope id / scope id / unique identifier / primary key / uuid | varchar(36) | schema / address_scopes |
| address_scopes.name | name / address scope name / scope name / label / title | varchar(255) | schema / address_scopes |
| address_scopes.tenant_id | tenant id / tenant identifier / project id / owner id / account id | varchar(255) | schema / address_scopes |
| address_scopes.shared | shared / is shared / shared flag / visibility / public / shared status | tinyint(1) | schema / address_scopes |
| address_scopes.ip_version | ip version / protocol version / ipv4 ipv6 / address family / version | int | schema / address_scopes |

## agents

Stores metadata and status information for Neutron network agents (e.g., Open vSwitch, L3, DHCP) running on compute nodes, including their type, host, heartbeat status, and configuration.

恢复表名: agents / neutron agents / openstack agents / network agents / agent list / agent registry
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| agents.id | id / identifier / agent id / agent uuid / unique agent identifier / agent primary key | varchar(36) | schema / agents |
| agents.agent_type | agent type / type of agent / agent category / agent kind / openvswitch agent / l3 agent / dhcp agent | varchar(255) | schema / agents |
| agents.binary | binary / agent binary name / executable name / agent process name / neutron-openvswitch-agent | varchar(255) | schema / agents |
| agents.topic | topic / message topic / agent topic / rpc topic | varchar(255) | schema / agents |
| agents.host | host / agent host / compute node / server name / hostname / node name | varchar(255) | schema / agents |
| agents.admin_state_up | admin state up / admin state / agent enabled / agent active / is agent up / admin up | tinyint(1) | schema / agents |
| agents.created_at | created at / creation time / agent created date / registration time / created timestamp | datetime | schema / agents |
| agents.started_at | started at / start time / agent start date / last start time / started timestamp | datetime | schema / agents |
| agents.heartbeat_timestamp | heartbeat timestamp / last heartbeat / heartbeat time / last seen / agent alive time / heartbeat date | datetime | schema / agents |
| agents.description | description / agent description / notes / agent info / description text | varchar(255) | schema / agents |
| agents.configurations | configurations / agent config / configuration json / agent settings / ovs config / tunneling ip | varchar(4095) | schema / agents |
| agents.load | load / agent load / workload / load factor / current load | int | schema / agents |
| agents.availability_zone | availability zone / az / zone / agent zone | varchar(255) | schema / agents |
| agents.resource_versions | resource versions / resource version / version info / qos policy version / resource versions json | varchar(8191) | schema / agents |

## alembic_version

Tracks the current database schema migration version applied by the Alembic migration tool.

恢复表名: alembic version / database migration version / schema version / migration state / alembic metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alembic_version.version_num | version num / version number / migration id / schema version / alembic version / current revision / migration hash | varchar(32) | schema / alembic_version |

## alembic_version_fwaas

Tracks the current Alembic database migration version for the FWAAS schema.

恢复表名: alembic version fwaas / fwaas schema version / fwaas migration version / database version fwaas / alembic version table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alembic_version_fwaas.version_num | version num / version number / migration version / schema version / alembic version / db version / revision id | varchar(32) | schema / alembic_version_fwaas |

## alembic_version_lbaas

Tracks the current database schema migration version for the Load Balancer as a Service (LBaaS) component using Alembic.

恢复表名: alembic version lbaas / lbaas migration version / lbaas schema version / alembic lbaas / lbaas db version
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| alembic_version_lbaas.version_num | version num / version number / migration version / schema version / alembic version / db version / lbaas version | varchar(32) | schema / alembic_version_lbaas |

## allowedaddresspairs

Stores additional MAC and IP address pairs allowed on a specific Neutron port, enabling ports to have multiple allowed addresses beyond their primary assignment.

恢复表名: allowedaddresspairs / allowed address pairs / aap / port allowed addresses / allowed mac ip pairs / port security allowed addresses
SQL表别名: a, aap

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| allowedaddresspairs.port_id | port id / port identifier / associated port / parent port id / network port id | varchar(36) | neutron_106, neutron_12, neutron_237, neutron_281, neutron_286, neutron_30, neutron_601, neutron_87 |
| allowedaddresspairs.mac_address | mac address / allowed mac / media access control address / allowed mac address / hardware address | varchar(32) | neutron_106, neutron_12, neutron_237, neutron_281, neutron_286, neutron_30, neutron_601, neutron_87 |
| allowedaddresspairs.ip_address | ip address / allowed ip / allowed ip address / ipv4 address / ipv6 address / network address | varchar(64) | neutron_106, neutron_12, neutron_237, neutron_281, neutron_286, neutron_30, neutron_601, neutron_87 |

## arista_provisioned_nets

Stores provisioning details for Arista networks, linking network identifiers to tenant and segmentation information.

恢复表名: arista provisioned nets / arista provisioned networks / arista nets / provisioned arista networks / arista network provisioning / arista net records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| arista_provisioned_nets.tenant_id | tenant id / tenant identifier / project id / project identifier / owner id / tenant uuid | varchar(255) | schema / arista_provisioned_nets |
| arista_provisioned_nets.id | id / identifier / record id / primary key / unique id / arista net id / provisioning id | varchar(36) | schema / arista_provisioned_nets |
| arista_provisioned_nets.network_id | network id / network identifier / net id / openstack network id / neutron network id / associated network | varchar(36) | schema / arista_provisioned_nets |
| arista_provisioned_nets.segmentation_id | segmentation id / segmentation identifier / segment id / vlan id / vlan / network segment | int | schema / arista_provisioned_nets |

## arista_provisioned_tenants

Stores records of tenants provisioned in the Arista network environment, linking internal system IDs to tenant identifiers.

恢复表名: arista provisioned tenants / arista tenants / provisioned tenants / arista tenant list / tenant provisioning records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| arista_provisioned_tenants.tenant_id | tenant id / tenant identifier / tenant name / arista tenant id / tenant key | varchar(255) | schema / arista_provisioned_tenants |
| arista_provisioned_tenants.id | id / identifier / record id / primary key / row id / tenant record id | varchar(36) | schema / arista_provisioned_tenants |

## arista_provisioned_vms

Tracks virtual machines provisioned on Arista infrastructure, linking VMs to their hosting resources, network ports, and tenants.

恢复表名: arista provisioned vms / provisioned virtual machines / arista vm inventory / provisioned vm records / arista vm provisioning
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| arista_provisioned_vms.tenant_id | tenant id / tenant identifier / customer id / project id / organization id / tenant | varchar(255) | schema / arista_provisioned_vms |
| arista_provisioned_vms.id | id / identifier / record id / primary key / row id / provisioning id / unique id | varchar(36) | schema / arista_provisioned_vms |
| arista_provisioned_vms.vm_id | vm id / vm identifier / virtual machine id / instance id / vm uuid / virtual machine / vm | varchar(255) | schema / arista_provisioned_vms |
| arista_provisioned_vms.host_id | host id / host identifier / physical host id / server id / compute node id / host / hypervisor id | varchar(255) | schema / arista_provisioned_vms |
| arista_provisioned_vms.port_id | port id / port identifier / network port id / interface id / port uuid / port / network interface | varchar(36) | schema / arista_provisioned_vms |
| arista_provisioned_vms.network_id | network id / network identifier / network uuid / subnet id / virtual network id / network / vnet id | varchar(36) | schema / arista_provisioned_vms |

## auto_allocated_topologies

Stores the automatically allocated network topologies, linking tenants to specific networks and routers.

恢复表名: auto allocated topologies / auto topology / auto allocated network topology / network topology allocation / auto router topology
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| auto_allocated_topologies.tenant_id | tenant id / tenant identifier / project id / customer id / account id | varchar(255) | schema / auto_allocated_topologies |
| auto_allocated_topologies.network_id | network id / network identifier / subnet id / network uuid / associated network | varchar(36) | schema / auto_allocated_topologies |
| auto_allocated_topologies.router_id | router id / router identifier / gateway id / router uuid / associated router | varchar(36) | schema / auto_allocated_topologies |

## bgp_peers

Stores configuration details for Border Gateway Protocol (BGP) peer relationships, including authentication, IP addresses, and autonomous system numbers.

恢复表名: bgp peers / BGP Peer Configuration / Border Gateway Protocol Peers / BGP Neighbor List / External BGP Peers / iBGP Peers
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bgp_peers.id | id / identifier / BGP Peer ID / Peer Identifier / Unique Peer ID / BGP Session ID | varchar(36) | schema / bgp_peers |
| bgp_peers.name | name / Peer Name / BGP Peer Name / Neighbor Name / Peer Label / Configuration Name | varchar(255) | schema / bgp_peers |
| bgp_peers.auth_type | auth type / Authentication Type / Auth Method / BGP Auth Type / Security Type / Password Type | varchar(16) | schema / bgp_peers |
| bgp_peers.password | password / BGP Password / Auth Password / Peer Password / MD5 Key / Session Password | varchar(255) | schema / bgp_peers |
| bgp_peers.peer_ip | peer ip / Peer IP Address / BGP Neighbor IP / Remote IP / Peer Address / Neighbor Address | varchar(64) | schema / bgp_peers |
| bgp_peers.remote_as | remote as / Remote AS Number / Peer AS / Autonomous System Number / Remote ASN / Neighbor AS | int | schema / bgp_peers |
| bgp_peers.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Customer ID / Service Tenant | varchar(255) | schema / bgp_peers |

## bgp_speaker_dragent_bindings

Maps BGP speakers to their associated agents, establishing the binding relationship between BGP speaker configurations and the agents that manage or represent them.

恢复表名: bgp speaker dragent bindings / BGP Speaker Agent Bindings / BGP Speaker Agent Associations / BGP Speaker to Agent Mapping / BGP Agent Bindings / BGP Speaker Agent Links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bgp_speaker_dragent_bindings.agent_id | agent id / agent identifier / Agent UUID / Agent Key / Associated Agent ID | varchar(36) | schema / bgp_speaker_dragent_bindings |
| bgp_speaker_dragent_bindings.bgp_speaker_id | bgp speaker id / bgp speaker identifier / BGP Speaker UUID / BGP Speaker Key / Associated BGP Speaker ID | varchar(36) | schema / bgp_speaker_dragent_bindings |

## bgp_speaker_network_bindings

Maps BGP speakers to specific networks and IP versions, defining which networks a BGP speaker is bound to for routing purposes.

恢复表名: bgp speaker network bindings / BGP network associations / BGP speaker network links / BGP network bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bgp_speaker_network_bindings.bgp_speaker_id | bgp speaker id / bgp speaker identifier / speaker ID / speaker uuid | varchar(36) | schema / bgp_speaker_network_bindings |
| bgp_speaker_network_bindings.network_id | network id / network identifier / network uuid / associated network | varchar(36) | schema / bgp_speaker_network_bindings |
| bgp_speaker_network_bindings.ip_version | ip version / IP protocol version / IPv4/IPv6 version / network address family | int | schema / bgp_speaker_network_bindings |

## bgp_speaker_peer_bindings

Maps BGP speakers to their associated BGP peers, defining the binding or association between a speaker and a peer in the network configuration.

恢复表名: bgp speaker peer bindings / BGP Speaker Peer Associations / BGP Speaker Peer Links / BGP Speaker Peer Relationships / BGP Speaker Peer Mappings / BGP Speaker Peer Connections
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bgp_speaker_peer_bindings.bgp_speaker_id | bgp speaker id / bgp speaker identifier / Speaker ID / Speaker UUID / BGP Speaker Key / Speaker Reference | varchar(36) | schema / bgp_speaker_peer_bindings |
| bgp_speaker_peer_bindings.bgp_peer_id | bgp peer id / bgp peer identifier / Peer ID / Peer UUID / BGP Peer Key / Peer Reference | varchar(36) | schema / bgp_speaker_peer_bindings |

## bgp_speakers

Stores configuration details for BGP speakers used to advertise tenant networks and floating IP host routes in the Neutron networking service.

恢复表名: bgp speakers / BGP speaker configurations / Border Gateway Protocol speakers / BGP peering settings / Neutron BGP speakers
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bgp_speakers.id | id / identifier / BGP speaker ID / speaker identifier / unique ID / primary key | varchar(36) | schema / bgp_speakers |
| bgp_speakers.name | name / BGP speaker name / speaker label / configuration name / display name | varchar(255) | schema / bgp_speakers |
| bgp_speakers.local_as | local as / local AS number / autonomous system number / AS number / AS ID | int | schema / bgp_speakers |
| bgp_speakers.ip_version | ip version / protocol version / IPv4/IPv6 / address family version | int | schema / bgp_speakers |
| bgp_speakers.tenant_id | tenant id / tenant identifier / project ID / owner ID / customer ID / account ID | varchar(255) | schema / bgp_speakers |
| bgp_speakers.advertise_floating_ip_host_routes | advertise floating ip host routes / advertise floating IP routes / floating IP host routes enabled / advertise FIP host routes / FIP route advertisement | tinyint(1) | schema / bgp_speakers |
| bgp_speakers.advertise_tenant_networks | advertise tenant networks / tenant network advertisement / advertise project networks / network route advertisement | tinyint(1) | schema / bgp_speakers |

## brocadenetworks

Stores network configuration details, specifically VLAN identifiers, for Brocade network infrastructure.

恢复表名: brocadenetworks / Brocade Networks / Brocade Network Configurations / Network VLANs / Brocade VLAN Table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| brocadenetworks.id | id / identifier / Network ID / Brocade Network ID / Record ID / Unique Identifier | varchar(36) | schema / brocadenetworks |
| brocadenetworks.vlan | vlan / VLAN ID / VLAN Number / Virtual LAN / Network Segment / VLAN Tag | varchar(10) | schema / brocadenetworks |

## brocadeports

Stores configuration and status details for Brocade network ports, including VLAN assignments, administrative state, and physical interface mappings.

恢复表名: brocadeports / Brocade ports / Brocade port table / Brocade network ports / Brocade VLAN ports / Brocade interface ports
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| brocadeports.port_id | port id / port identifier / Unique port ID / Brocade port ID | varchar(36) | schema / brocadeports |
| brocadeports.network_id | network id / network identifier / Associated network / Network UUID | varchar(36) | schema / brocadeports |
| brocadeports.admin_state_up | admin state up / Administrative status / Port enabled / Admin up / Port active | tinyint(1) | schema / brocadeports |
| brocadeports.physical_interface | physical interface / Physical port name / Hardware interface / Interface name / Physical port | varchar(36) | schema / brocadeports |
| brocadeports.vlan_id | vlan id / vlan identifier / Virtual LAN ID / VLAN number / VLAN tag | varchar(36) | schema / brocadeports |
| brocadeports.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Project identifier | varchar(36) | schema / brocadeports |

## cisco_csr_identifier_map

Maps IPSec site connection identifiers to Cisco CSR (Cloud Services Router) tunnel, IKE, and IPSec policy identifiers for a specific tenant.

恢复表名: cisco csr identifier map / CSR ID Mapping / IPSec Site Connection to CSR Mapping / Cisco Router Identifier Map / CSR Tunnel Policy Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_csr_identifier_map.tenant_id | tenant id / tenant identifier / Customer ID / Account ID / Organization ID | varchar(255) | schema / cisco_csr_identifier_map |
| cisco_csr_identifier_map.ipsec_site_conn_id | ipsec site conn id / ipsec site conn identifier / IPSec Site Connection ID / Site Connection ID / IPSec Connection ID / Site-to-Site Connection ID / VPN Connection ID | varchar(64) | schema / cisco_csr_identifier_map |
| cisco_csr_identifier_map.csr_tunnel_id | csr tunnel id / csr tunnel identifier / Tunnel Identifier / Router Tunnel ID / CSR Tunnel Number / Tunnel ID | int | schema / cisco_csr_identifier_map |
| cisco_csr_identifier_map.csr_ike_policy_id | csr ike policy id / csr ike policy identifier / IKE Policy Identifier / Router IKE Policy ID / IKE Proposal ID / Phase 1 Policy ID | int | schema / cisco_csr_identifier_map |
| cisco_csr_identifier_map.csr_ipsec_policy_id | csr ipsec policy id / csr ipsec policy identifier / IPSec Policy Identifier / Router IPSec Policy ID / IPSec Transform Set ID / Phase 2 Policy ID | int | schema / cisco_csr_identifier_map |

## cisco_firewall_associations

Stores the association between Cisco firewall instances, network ports, and access control lists (ACLs), including the direction of traffic and the associated router.

恢复表名: cisco firewall associations / firewall associations / cisco firewall rules / firewall acl mappings / cisco firewall port bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_firewall_associations.fw_id | fw id / fw identifier / firewall id / cisco firewall id / firewall identifier | varchar(36) | schema / cisco_firewall_associations |
| cisco_firewall_associations.port_id | port id / port identifier / network port id / firewall port | varchar(36) | schema / cisco_firewall_associations |
| cisco_firewall_associations.direction | direction / traffic direction / flow direction / inbound outbound / direction of traffic | varchar(16) | schema / cisco_firewall_associations |
| cisco_firewall_associations.acl_id | acl id / acl identifier / access control list id / security policy id | varchar(36) | schema / cisco_firewall_associations |
| cisco_firewall_associations.router_id | router id / router identifier / cisco router id / associated router | varchar(36) | schema / cisco_firewall_associations |

## cisco_hosting_devices

Stores metadata and configuration details for Cisco hosting devices managed by the Neutron service, including their administrative state, management ports, and associated agents.

恢复表名: cisco hosting devices / cisco hosting device / hosting devices / cisco devices / hosting device table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_hosting_devices.tenant_id | tenant id / tenant identifier / project id / tenant / project / owner id / customer id | varchar(255) | schema / cisco_hosting_devices |
| cisco_hosting_devices.id | id / identifier / device id / hosting device id / primary key / record id / uuid | varchar(36) | schema / cisco_hosting_devices |
| cisco_hosting_devices.complementary_id | complementary id / complementary identifier / secondary id / related id / paired id / complement id | varchar(36) | schema / cisco_hosting_devices |
| cisco_hosting_devices.device_id | device id / device identifier / physical device id / hardware id / cisco device id | varchar(255) | schema / cisco_hosting_devices |
| cisco_hosting_devices.admin_state_up | admin state up / admin state / administrative state / enabled / active / up / admin up | tinyint(1) | schema / cisco_hosting_devices |
| cisco_hosting_devices.management_port_id | management port id / management port identifier / mgmt port id / management interface id / port id / mgmt interface | varchar(36) | schema / cisco_hosting_devices |
| cisco_hosting_devices.protocol_port | protocol port / port number / service port / communication port / port | int | schema / cisco_hosting_devices |
| cisco_hosting_devices.cfg_agent_id | cfg agent id / cfg agent identifier / configuration agent id / agent id / config agent / management agent id | varchar(36) | schema / cisco_hosting_devices |
| cisco_hosting_devices.created_at | created at / creation date / created date / timestamp / date created | datetime | schema / cisco_hosting_devices |
| cisco_hosting_devices.status | status / device status / state / operational status / current status | varchar(16) | schema / cisco_hosting_devices |

## cisco_ml2_apic_contracts

Maps Cisco ML2 APIC contracts to specific routers, likely indicating which routers are associated with or enforce specific network contracts in a Cisco ACI environment.

恢复表名: cisco ml2 apic contracts / APIC Contract Router Mapping / ML2 APIC Contract Association / Cisco ACI Contract Routers
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_apic_contracts.tenant_id | tenant id / tenant identifier / Project ID / Project Identifier / Neutron Tenant / Network Tenant | varchar(255) | schema / cisco_ml2_apic_contracts |
| cisco_ml2_apic_contracts.router_id | router id / router identifier / Network Router ID / L3 Router ID / Gateway Router ID / APIC Router ID | varchar(64) | schema / cisco_ml2_apic_contracts |

## cisco_ml2_apic_host_links

Stores the mapping between compute hosts and their physical network interface connections to Cisco APIC switches, including interface names, MAC addresses, and switch port details.

恢复表名: cisco ml2 apic host links / cisco_ml2_apic_host_links / APIC host links / Cisco ML2 APIC host interface links / host switch port mappings / APIC host connectivity
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_apic_host_links.host | host / hostname / compute node / server name / vm host / node | varchar(255) | schema / cisco_ml2_apic_host_links |
| cisco_ml2_apic_host_links.ifname | ifname / interface name / port name / nic name / network interface / ethernet interface | varchar(64) | schema / cisco_ml2_apic_host_links |
| cisco_ml2_apic_host_links.ifmac | ifmac / mac address / interface mac / hardware address / physical address / nic mac | varchar(32) | schema / cisco_ml2_apic_host_links |
| cisco_ml2_apic_host_links.swid | swid / switch id / switch identifier / apic switch id / leaf switch id / switch name | varchar(32) | schema / cisco_ml2_apic_host_links |
| cisco_ml2_apic_host_links.module | module / switch module / line card / slot number / module id / chassis module | varchar(32) | schema / cisco_ml2_apic_host_links |
| cisco_ml2_apic_host_links.port | port / switch port / port number / physical port / interface port / port id | varchar(32) | schema / cisco_ml2_apic_host_links |

## cisco_ml2_apic_names

Maps Neutron resource identifiers and types to their corresponding Cisco APIC names for ML2 integration.

恢复表名: cisco ml2 apic names / APIC Name Mapping / Neutron APIC Name Table / ML2 APIC Names / Cisco APIC Name Registry
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_apic_names.neutron_id | neutron id / neutron identifier / Neutron Resource ID / Neutron UUID / Resource ID / Neutron Object ID | varchar(36) | schema / cisco_ml2_apic_names |
| cisco_ml2_apic_names.neutron_type | neutron type / Resource Type / Neutron Object Type / Neutron Entity Type / Type | varchar(32) | schema / cisco_ml2_apic_names |
| cisco_ml2_apic_names.apic_name | apic name / Cisco APIC Name / APIC Identifier / APIC Object Name / Name | varchar(255) | schema / cisco_ml2_apic_names |

## cisco_ml2_n1kv_network_bindings

Stores the binding information between OpenStack networks and Cisco N1KV (Network 1000 Virtualization) profiles, including segmentation details and network types for the ML2 plugin.

恢复表名: cisco ml2 n1kv network bindings / N1KV Network Bindings / ML2 N1KV Network Bindings / Cisco N1KV Network Bindings / N1KV Network Binding Table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_network_bindings.network_id | network id / network identifier / OpenStack Network ID / Net ID / Network UUID | varchar(36) | schema / cisco_ml2_n1kv_network_bindings |
| cisco_ml2_n1kv_network_bindings.network_type | network type / L2 Network Type / Segmentation Type / Network Protocol / VLAN Type / VXLAN Type | varchar(32) | schema / cisco_ml2_n1kv_network_bindings |
| cisco_ml2_n1kv_network_bindings.segmentation_id | segmentation id / segmentation identifier / VLAN ID / VXLAN VNI / Segment ID / Network Segment Identifier | int | schema / cisco_ml2_n1kv_network_bindings |
| cisco_ml2_n1kv_network_bindings.profile_id | profile id / profile identifier / N1KV Profile ID / Cisco Profile ID / Network Profile Identifier / Profile UUID | varchar(36) | schema / cisco_ml2_n1kv_network_bindings |

## cisco_ml2_n1kv_network_profiles

Stores configuration details for Cisco ML2 N1KV network profiles, including segment types, ranges, and multicast settings.

恢复表名: cisco ml2 n1kv network profiles / N1KV Network Profile / ML2 Network Profile / Cisco Network Profile / N1KV Profile
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_network_profiles.id | id / identifier / Profile ID / Unique Identifier / Primary Key | varchar(36) | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.name | name / Profile Name / Network Profile Name / Label | varchar(255) | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.segment_type | segment type / Type / Encapsulation Type / VLAN/VXLAN Type | enum('vlan','vxlan') | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.segment_range | segment range / Range / VLAN Range / VXLAN Range / ID Range | varchar(255) | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.multicast_ip_index | multicast ip index / MC IP Index / Index / Multicast Index | int | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.multicast_ip_range | multicast ip range / MC IP Range / Multicast Address Range / IP Range | varchar(255) | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.sub_type | sub type / Subtype / Profile Subtype / Variant | varchar(255) | schema / cisco_ml2_n1kv_network_profiles |
| cisco_ml2_n1kv_network_profiles.physical_network | physical network / Network Name / Phys Net / Underlay Network | varchar(255) | schema / cisco_ml2_n1kv_network_profiles |

## cisco_ml2_n1kv_policy_profiles

Stores policy profile definitions for Cisco ML2 N1KV (Nexus 1000V) network virtualization, linking policy names to specific VSM instances.

恢复表名: cisco ml2 n1kv policy profiles / N1KV Policy Profile / ML2 N1KV Policy / Cisco Nexus 1000V Policy Profile / Nexus 1000V Policy
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_policy_profiles.id | id / identifier / Policy Profile ID / Profile ID / Unique Identifier / Policy ID / N1KV Profile ID | varchar(36) | schema / cisco_ml2_n1kv_policy_profiles |
| cisco_ml2_n1kv_policy_profiles.name | name / Policy Profile Name / Profile Name / Policy Name / N1KV Policy Name / Profile Label | varchar(255) | schema / cisco_ml2_n1kv_policy_profiles |
| cisco_ml2_n1kv_policy_profiles.vsm_ip | vsm ip / VSM IP Address / Virtual Switch Manager IP / Nexus 1000V VSM IP / Controller IP | varchar(16) | schema / cisco_ml2_n1kv_policy_profiles |

## cisco_ml2_n1kv_port_bindings

Stores the binding relationships between logical port identifiers and specific N1KV profiles in the Cisco ML2 (Mechanism Driver) context.

恢复表名: cisco ml2 n1kv port bindings / N1KV Port Binding Table / ML2 N1KV Port Bindings / Cisco N1KV Port Bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_port_bindings.port_id | port id / port identifier / Logical Port ID / Port UUID / Binding Port ID | varchar(36) | schema / cisco_ml2_n1kv_port_bindings |
| cisco_ml2_n1kv_port_bindings.profile_id | profile id / profile identifier / N1KV Profile ID / Binding Profile ID / Cisco Profile ID | varchar(36) | schema / cisco_ml2_n1kv_port_bindings |

## cisco_ml2_n1kv_profile_bindings

Stores the binding relationships between tenants and Cisco N1KV profiles (network or policy) within the ML2 plugin.

恢复表名: cisco ml2 n1kv profile bindings / n1kv profile bindings / cisco n1kv profile bindings / ml2 n1kv profile bindings / cisco ml2 profile bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_profile_bindings.profile_type | profile type / type of profile / profile category / binding type / n1kv profile type | enum('network','policy') | schema / cisco_ml2_n1kv_profile_bindings |
| cisco_ml2_n1kv_profile_bindings.tenant_id | tenant id / tenant identifier / project id / project identifier / owner id / tenant uuid | varchar(36) | schema / cisco_ml2_n1kv_profile_bindings |
| cisco_ml2_n1kv_profile_bindings.profile_id | profile id / profile identifier / n1kv profile id / profile uuid / bound profile id | varchar(36) | schema / cisco_ml2_n1kv_profile_bindings |

## cisco_ml2_n1kv_vlan_allocations

Tracks the allocation status of VLANs to physical networks for Cisco N1KV integration in the ML2 plugin.

恢复表名: cisco ml2 n1kv vlan allocations / N1KV VLAN Allocation Table / Cisco N1KV VLAN Mapping / ML2 N1KV VLAN State / Physical Network VLAN Allocation
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_vlan_allocations.physical_network | physical network / Physical Network Name / Phys Net / Network Name / Physical Network Identifier / PhysNet | varchar(64) | schema / cisco_ml2_n1kv_vlan_allocations |
| cisco_ml2_n1kv_vlan_allocations.vlan_id | vlan id / vlan identifier / VLAN Number / VLAN Tag / VLAN | int | schema / cisco_ml2_n1kv_vlan_allocations |
| cisco_ml2_n1kv_vlan_allocations.allocated | allocated / Allocation Status / Is Allocated / VLAN Allocated / Allocation Flag / Allocated Status | tinyint(1) | schema / cisco_ml2_n1kv_vlan_allocations |
| cisco_ml2_n1kv_vlan_allocations.network_profile_id | network profile id / network profile identifier / Profile ID / N1KV Profile ID / Profile UUID | varchar(36) | schema / cisco_ml2_n1kv_vlan_allocations |

## cisco_ml2_n1kv_vxlan_allocations

Tracks the allocation status of VXLAN IDs for Cisco N1KV network profiles in the ML2 plugin.

恢复表名: cisco ml2 n1kv vxlan allocations / vxlan_allocations / cisco_vxlan_allocations / n1kv_vxlan_allocations / vxlan_id_allocation_table / ml2_vxlan_allocations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_n1kv_vxlan_allocations.vxlan_id | vxlan id / vxlan identifier / vxlan_id / vxlan number / segment id / vxlan segment id | int | schema / cisco_ml2_n1kv_vxlan_allocations |
| cisco_ml2_n1kv_vxlan_allocations.allocated | allocated / allocation status / is allocated / vxlan allocated / allocation flag / status | tinyint(1) | schema / cisco_ml2_n1kv_vxlan_allocations |
| cisco_ml2_n1kv_vxlan_allocations.network_profile_id | network profile id / network profile identifier / network_profile_id / profile id / n1kv profile id / profile uuid / network profile | varchar(36) | schema / cisco_ml2_n1kv_vxlan_allocations |

## cisco_ml2_nexus_nve

Stores the mapping between Cisco Nexus switches and their Network Virtualization Encapsulation (NVE) identifiers, including the VNI and multicast group used for overlay traffic.

恢复表名: cisco ml2 nexus nve / Nexus NVE Configuration / Nexus VTEP Mapping / ML2 Nexus NVE Table / Nexus Overlay Node / Cisco Nexus NVE
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_nexus_nve.vni | vni / Virtual Network Identifier / Overlay ID / Tunnel ID / Segment ID | int | schema / cisco_ml2_nexus_nve |
| cisco_ml2_nexus_nve.switch_ip | switch ip / Nexus IP / Device IP / Management IP / Node Address / VTEP IP | varchar(255) | schema / cisco_ml2_nexus_nve |
| cisco_ml2_nexus_nve.device_id | device id / device identifier / Nexus ID / Switch ID / Node ID / Hardware ID / System ID | varchar(255) | schema / cisco_ml2_nexus_nve |
| cisco_ml2_nexus_nve.mcast_group | mcast group / Multicast Group / Multicast Address / Group Address / Overlay Multicast / Broadcast Group | varchar(255) | schema / cisco_ml2_nexus_nve |

## cisco_ml2_nexusport_bindings

Stores the binding relationships between Cisco Nexus switch ports and OpenStack network resources, including VLAN and VNI assignments for provider and tenant networks.

恢复表名: cisco ml2 nexusport bindings / cisco nexus port bindings / nexus port binding table / cisco ml2 nexus bindings / nexus switch port mappings / cisco network port bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_ml2_nexusport_bindings.binding_id | binding id / binding identifier / id / primary key / record id | int | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.port_id | port id / port identifier / switch port / nexus port / physical port | varchar(255) | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.vlan_id | vlan id / vlan identifier / vlan / virtual lan / vlan number / network vlan | int | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.switch_ip | switch ip / ip address / nexus ip / switch address / management ip | varchar(255) | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.instance_id | instance id / instance identifier / vm id / server id / openstack instance / compute instance | varchar(255) | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.vni | vni / vxlan id / virtual network identifier / vxlan vni / network vni | int | schema / cisco_ml2_nexusport_bindings |
| cisco_ml2_nexusport_bindings.is_provider_vlan | is provider vlan / provider vlan / provider network / external vlan / provider flag | tinyint(1) | schema / cisco_ml2_nexusport_bindings |

## cisco_port_mappings

Stores the mapping between logical OpenStack ports and physical Cisco network resources, including port types, network types, and segmentation identifiers.

恢复表名: cisco port mappings / cisco port mapping / cisco port map / cisco port mapping table / cisco port mapping records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_port_mappings.logical_resource_id | logical resource id / logical resource identifier / resource id / resource identifier / logical resource | varchar(36) | schema / cisco_port_mappings |
| cisco_port_mappings.logical_port_id | logical port id / logical port identifier / port id / port identifier / logical port | varchar(36) | schema / cisco_port_mappings |
| cisco_port_mappings.port_type | port type / type of port / port category / port kind / port classification | varchar(32) | schema / cisco_port_mappings |
| cisco_port_mappings.network_type | network type / type of network / network category / network kind / network classification | varchar(32) | schema / cisco_port_mappings |
| cisco_port_mappings.hosting_port_id | hosting port id / hosting port identifier / host port id / host port identifier / hosting port | varchar(36) | schema / cisco_port_mappings |
| cisco_port_mappings.segmentation_id | segmentation id / segmentation identifier / segment id / segment identifier / vlan id / segmentation | int | schema / cisco_port_mappings |

## cisco_router_mappings

Stores mapping configurations and scheduling settings for Cisco routers, linking router identifiers to their hosting devices.

恢复表名: cisco router mappings / router mappings / cisco mappings / router configuration mappings / cisco device mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cisco_router_mappings.router_id | router id / router identifier / cisco router id / device id / router uuid | varchar(36) | schema / cisco_router_mappings |
| cisco_router_mappings.auto_schedule | auto schedule / automatic scheduling / schedule enabled / auto schedule flag / scheduling mode | tinyint(1) | schema / cisco_router_mappings |
| cisco_router_mappings.hosting_device_id | hosting device id / hosting device identifier / host device id / parent device id / hosting identifier / device host id | varchar(36) | schema / cisco_router_mappings |

## consistencyhashes

Stores consistency hash identifiers and their corresponding hash values for load balancing or data distribution.

恢复表名: consistencyhashes / consistency hashes / hash table / hashing configuration / consistency hash records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| consistencyhashes.hash_id | hash id / hash identifier / id / identifier / primary key | varchar(255) | schema / consistencyhashes |
| consistencyhashes.hash | hash / hash value / hash string / consistency hash / hash code / hash key | varchar(255) | schema / consistencyhashes |

## default_security_group

Maps tenants to their default security group identifiers in the Neutron networking service.

恢复表名: default security group / default security groups / default sg / default security group mapping / tenant default security group
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| default_security_group.tenant_id | tenant id / tenant identifier / project id / tenant / project / owner id / account id | varchar(255) | schema / default_security_group |
| default_security_group.security_group_id | security group id / security group identifier / sg id / security group / default sg id / group id | varchar(36) | schema / default_security_group |

## dnsnameservers

Stores the DNS nameserver configurations (IP addresses and priority order) associated with specific subnets in the Neutron network.

恢复表名: dnsnameservers / DNS nameservers / DNS servers / nameservers / DNS configuration / subnet DNS
SQL表别名: d, d2, dn, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| dnsnameservers.address | address / DNS address / nameserver IP / DNS IP / server address / DNS server address / nameserver address | varchar(128) | neutron_322, neutron_336, neutron_4, neutron_557 |
| dnsnameservers.subnet_id | subnet id / subnet identifier / associated subnet / subnet reference / parent subnet ID | varchar(36) | neutron_322, neutron_336, neutron_4, neutron_557, neutron_102, neutron_112, neutron_122, neutron_157 |
| dnsnameservers.order | order / DNS order / nameserver order / priority / sequence number / DNS priority / server order | int | neutron_322, neutron_336, neutron_4, neutron_557, neutron_102, neutron_112, neutron_122, neutron_157 |

## dvr_host_macs

Stores the mapping between DVR hosts and their associated MAC addresses.

恢复表名: dvr host macs / DVR host MAC addresses / DVR host network interfaces / DVR host MAC mapping / DVR host MAC table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| dvr_host_macs.host | host / DVR host / host name / DVR host identifier / host ID / DVR host name | varchar(255) | schema / dvr_host_macs |
| dvr_host_macs.mac_address | mac address / MAC / Media Access Control address / network MAC / host MAC / MAC ID | varchar(32) | schema / dvr_host_macs |

## externalnetworks

Tracks which networks are designated as external networks in the Neutron service, including whether they are set as the default external network.

恢复表名: externalnetworks / external networks / external network / default external networks / neutron external networks / external network registry
SQL表别名: e, en

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| externalnetworks.network_id | network id / network identifier / external network id / network uuid / id of the external network | varchar(36) | neutron_209, neutron_215, neutron_221, neutron_222, neutron_261, neutron_267, neutron_3, neutron_344 |
| externalnetworks.is_default | is default / default flag / default external network flag / is default external / default status | tinyint(1) | neutron_209, neutron_215, neutron_221, neutron_222, neutron_261, neutron_267, neutron_3, neutron_344 |

## extradhcpopts

Stores additional DHCP options configured for network ports, including the option name, value, and IP version.

恢复表名: extradhcpopts / extra dhcp options / dhcp options / port dhcp options / additional dhcp settings / dhcp option configurations
SQL表别名: e

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| extradhcpopts.id | id / identifier / dhcp option id / option identifier / primary key / record id | varchar(36) | schema / extradhcpopts |
| extradhcpopts.port_id | port id / port identifier / network port id / associated port / linked port | varchar(36) | neutron_518, neutron_559 |
| extradhcpopts.opt_name | opt name / option name / dhcp option name / option label / dhcp setting name / option key | varchar(64) | schema / extradhcpopts |
| extradhcpopts.opt_value | opt value / option value / dhcp option value / option data / dhcp setting value / option content | varchar(255) | schema / extradhcpopts |
| extradhcpopts.ip_version | ip version / ipv4 ipv6 / protocol version / ip type / version | int | neutron_518, neutron_559 |

## firewall_policies

Stores definitions of firewall policies that control network traffic access for tenants in the Neutron networking service.

恢复表名: firewall policies / firewall policy / security group / security groups / network policy / network policies / firewall rules / access control policy
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| firewall_policies.tenant_id | tenant id / tenant identifier / project id / owner id / account id / customer id / organization id | varchar(255) | schema / firewall_policies |
| firewall_policies.id | id / identifier / policy id / firewall policy id / unique id / policy identifier / uuid | varchar(36) | schema / firewall_policies |
| firewall_policies.name | name / policy name / firewall name / policy title / label / display name | varchar(255) | schema / firewall_policies |
| firewall_policies.description | description / policy description / notes / details / summary / explanation | varchar(1024) | schema / firewall_policies |
| firewall_policies.shared | shared / is shared / shared flag / public visibility / multi-tenant / shared status | tinyint(1) | schema / firewall_policies |
| firewall_policies.audited | audited / is audited / audit flag / logging enabled / audit status / monitored | tinyint(1) | schema / firewall_policies |

## firewall_router_associations

Maps the many-to-many relationship between firewalls and routers, indicating which routers are associated with which firewalls.

恢复表名: firewall router associations / firewall router mapping / router firewall links / firewall router junction / firewall router relationship
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| firewall_router_associations.fw_id | fw id / fw identifier / firewall id / firewall identifier / firewall uuid / firewall key | varchar(36) | schema / firewall_router_associations |
| firewall_router_associations.router_id | router id / router identifier / router uuid / router key / network router id | varchar(36) | schema / firewall_router_associations |

## firewall_rules

Stores individual firewall rule definitions including source/destination IP and port ranges, protocol, action, and associated firewall policy for network traffic control.

恢复表名: firewall rules / network firewall rules / security group rules / firewall policies / network access rules / traffic rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| firewall_rules.tenant_id | tenant id / tenant identifier / project id / owner id / account id / user id / organization id | varchar(255) | schema / firewall_rules |
| firewall_rules.id | id / identifier / rule id / firewall rule id / primary key / unique identifier / rule identifier | varchar(36) | schema / firewall_rules |
| firewall_rules.name | name / rule name / firewall rule name / label / title / rule title | varchar(255) | schema / firewall_rules |
| firewall_rules.description | description / rule description / notes / details / explanation / comment | varchar(1024) | schema / firewall_rules |
| firewall_rules.firewall_policy_id | firewall policy id / firewall policy identifier / policy id / group id / security group id / parent policy id | varchar(36) | schema / firewall_rules |
| firewall_rules.shared | shared / is shared / shared flag / public rule / shared status / visibility | tinyint(1) | schema / firewall_rules |
| firewall_rules.protocol | protocol / network protocol / ip protocol / transport protocol / protocol type / tcp udp icmp | varchar(40) | schema / firewall_rules |
| firewall_rules.ip_version | ip version / ipv4 ipv6 / address family / ip type / version | int | schema / firewall_rules |
| firewall_rules.source_ip_address | source ip address / source ip / src ip / origin ip / from ip / source address | varchar(46) | schema / firewall_rules |
| firewall_rules.destination_ip_address | destination ip address / destination ip / dest ip / target ip / to ip / destination address | varchar(46) | schema / firewall_rules |
| firewall_rules.source_port_range_min | source port range min / source port range minimum / source port min / src port start / source port lower bound / min source port / source port from | int | schema / firewall_rules |
| firewall_rules.source_port_range_max | source port range max / source port range maximum / source port max / src port end / source port upper bound / max source port / source port to | int | schema / firewall_rules |
| firewall_rules.destination_port_range_min | destination port range min / destination port range minimum / destination port min / dest port start / destination port lower bound / min destination port / destination port from | int | schema / firewall_rules |
| firewall_rules.destination_port_range_max | destination port range max / destination port range maximum / destination port max / dest port end / destination port upper bound / max destination port / destination port to | int | schema / firewall_rules |
| firewall_rules.action | action / rule action / permit deny / allow block / traffic action / decision | enum('allow','deny','reject') | schema / firewall_rules |
| firewall_rules.enabled | enabled / is enabled / active / status / enabled flag / rule status | tinyint(1) | schema / firewall_rules |
| firewall_rules.position | position / rule position / order / priority / sequence number / rule index | int | schema / firewall_rules |

## firewalls

Stores metadata and configuration for OpenStack Neutron firewall resources, including their status, ownership, and associated policies.

恢复表名: firewalls / firewall / network firewalls / firewall resources / security firewalls
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| firewalls.tenant_id | tenant id / tenant identifier / tenant / project / project_id / owner / account / user_id | varchar(255) | schema / firewalls |
| firewalls.id | id / identifier / firewall_id / uuid / primary key / resource id | varchar(36) | schema / firewalls |
| firewalls.name | name / firewall name / title / label / display name | varchar(255) | schema / firewalls |
| firewalls.description | description / firewall description / notes / details / comment | varchar(1024) | schema / firewalls |
| firewalls.shared | shared / is_shared / shared flag / visibility / public / private | tinyint(1) | schema / firewalls |
| firewalls.admin_state_up | admin state up / admin state / enabled / active / up / down | tinyint(1) | schema / firewalls |
| firewalls.status | status / firewall status / state / operational status / health | varchar(16) | schema / firewalls |
| firewalls.firewall_policy_id | firewall policy id / firewall policy identifier / policy_id / firewall policy / associated policy / policy reference | varchar(36) | schema / firewalls |

## flavors

Stores definitions of instance flavors, specifying resource configurations (like CPU, RAM, disk) and metadata for virtual machines or compute instances.

恢复表名: flavors / flavor / instance_flavors / vm_flavors / compute_flavors / resource_flavors / flavor_definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| flavors.id | id / identifier / flavor_id / uuid / primary_key / flavor_uuid | varchar(36) | schema / flavors |
| flavors.name | name / flavor_name / label / title / flavor_label / instance_type_name | varchar(255) | schema / flavors |
| flavors.description | description / flavor_description / details / notes / flavor_details / summary | varchar(1024) | schema / flavors |
| flavors.enabled | enabled / is_enabled / active / status / availability / flavor_status | tinyint(1) | schema / flavors |
| flavors.service_type | service type / type / category / flavor_type / service_category / kind | varchar(36) | schema / flavors |

## flavorserviceprofilebindings

Maps specific flavors to service profiles, establishing the binding relationship between compute flavors and their associated service configurations.

恢复表名: flavorserviceprofilebindings / flavor service profile bindings / flavor profile mapping / service profile flavor associations / flavor to profile links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| flavorserviceprofilebindings.service_profile_id | service profile id / service profile identifier / profile id / profile uuid | varchar(36) | schema / flavorserviceprofilebindings |
| flavorserviceprofilebindings.flavor_id | flavor id / flavor identifier / compute flavor id / flavor uuid | varchar(36) | schema / flavorserviceprofilebindings |

## floatingipdnses

Stores DNS name and domain mappings for floating IP addresses, including both internal and published DNS records.

恢复表名: floatingipdnses / floating IP DNS records / floating IP DNS mappings / public IP DNS entries / floating IP name resolution / floating IP DNS configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| floatingipdnses.floatingip_id | floatingip id / floatingip identifier / floating IP ID / floating IP identifier / FIP ID / floating IP UUID / IP ID | varchar(36) | schema / floatingipdnses |
| floatingipdnses.dns_name | dns name / hostname / internal DNS name / FQDN name / domain name | varchar(255) | schema / floatingipdnses |
| floatingipdnses.dns_domain | dns domain / domain / internal domain / DNS zone / domain suffix | varchar(255) | schema / floatingipdnses |
| floatingipdnses.published_dns_name | published dns name / public DNS name / external hostname / published hostname / public FQDN | varchar(255) | schema / floatingipdnses |
| floatingipdnses.published_dns_domain | published dns domain / public DNS domain / external domain / published domain / public zone | varchar(255) | schema / floatingipdnses |

## floatingips

Stores OpenStack Neutron floating IP resources, mapping public external IP addresses to internal fixed IP addresses on ports for NAT and external connectivity.

恢复表名: floatingips / floating IPs / floating IP addresses / public IPs / external IPs / SNAT mappings / NAT floating IPs / OpenStack floating IPs
SQL表别名: f

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| floatingips.tenant_id | tenant id / tenant identifier / project ID / project / owner ID / owner / tenant / customer ID | varchar(255) | schema / floatingips |
| floatingips.id | id / identifier / floating IP ID / resource ID / UUID / floating IP identifier / FIP ID | varchar(36) | neutron_10, neutron_13, neutron_148, neutron_15, neutron_165, neutron_186, neutron_24, neutron_260 |
| floatingips.floating_ip_address | floating ip address / public IP / external IP / floating IP / NAT IP / internet IP / global IP | varchar(64) | schema / floatingips |
| floatingips.floating_network_id | floating network id / floating network identifier / external network ID / public network ID / floating network / NAT network ID | varchar(36) | schema / floatingips |
| floatingips.floating_port_id | floating port id / floating port identifier / port ID / network port ID / interface ID / port identifier | varchar(36) | schema / floatingips |
| floatingips.fixed_port_id | fixed port id / fixed port identifier / internal port ID / private port ID / instance port ID / target port ID / port ID | varchar(36) | neutron_10, neutron_13, neutron_148, neutron_15, neutron_165, neutron_186, neutron_24, neutron_260 |
| floatingips.fixed_ip_address | fixed ip address / private IP / internal IP / local IP / instance IP / subnet IP | varchar(64) | neutron_544 |
| floatingips.router_id | router id / router identifier / gateway router ID / NAT router ID | varchar(36) | schema / floatingips |
| floatingips.last_known_router_id | last known router id / last known router identifier / previous router ID / last router ID / historical router ID | varchar(36) | schema / floatingips |
| floatingips.status | status / state / floating IP status / operational status / FIP state | varchar(16) | neutron_544 |
| floatingips.standard_attr_id | standard attr id / standard attr identifier / standard attribute ID / resource attribute ID / metadata ID / standardattributes ID | bigint | neutron_544 |

## ha_router_agent_port_bindings

Tracks the binding of network ports to specific L3 agents for high-availability routers, indicating whether each agent is in an active or standby state.

恢复表名: ha router agent port bindings / High availability router port bindings / Router agent port bindings / HA router bindings / Router port agent bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ha_router_agent_port_bindings.port_id | port id / port identifier / network port id / port uuid / bound port | varchar(36) | schema / ha_router_agent_port_bindings |
| ha_router_agent_port_bindings.router_id | router id / router identifier / ha router id / router uuid / associated router | varchar(36) | schema / ha_router_agent_port_bindings |
| ha_router_agent_port_bindings.l3_agent_id | l3 agent id / l3 agent identifier / layer 3 agent id / agent id / routing agent id | varchar(36) | schema / ha_router_agent_port_bindings |
| ha_router_agent_port_bindings.state | state / agent state / binding state / ha state / active standby status | enum('active','standby') | schema / ha_router_agent_port_bindings |

## ha_router_networks

Maps High Availability (HA) routers to the networks they are connected to, serving as a junction table for router-network relationships in the Neutron networking service.

恢复表名: ha router networks / High Availability Router Networks / Router Network Associations / HA Router Interface Networks
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ha_router_networks.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Customer ID / Account ID / Organization ID | varchar(255) | schema / ha_router_networks |
| ha_router_networks.network_id | network id / network identifier / Subnet ID / VLAN ID / Connected Network / Interface Network | varchar(36) | schema / ha_router_networks |

## ha_router_vrid_allocations

Tracks the allocation of Virtual Router IDs (VRIDs) to specific networks for High Availability (HA) routers, ensuring unique VRID assignment per network.

恢复表名: ha router vrid allocations / High Availability Router Virtual Router ID Allocations / VRID Allocation Table / Router VRID Mapping / HA Router VRID Assignments
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ha_router_vrid_allocations.network_id | network id / network identifier / Net ID / Network UUID / Associated Network / Network Reference | varchar(36) | schema / ha_router_vrid_allocations |
| ha_router_vrid_allocations.vr_id | vr id / vr identifier / VRID / Virtual Router ID / Router ID / Virtual Router Identifier / VRID Number | int | schema / ha_router_vrid_allocations |

## healthmonitors

Stores configuration details for health monitors used to check the status of load balancer members, including protocol type, timing, and expected responses.

恢复表名: healthmonitors / health monitors / monitor / load balancer health monitor / lb health monitor / monitoring configuration / health check
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| healthmonitors.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner / account id / customer id | varchar(255) | schema / healthmonitors |
| healthmonitors.id | id / identifier / monitor id / uuid / unique identifier / monitor uuid / primary key | varchar(36) | schema / healthmonitors |
| healthmonitors.type | type / protocol / monitor type / check type / method / health check protocol | enum('PING','TCP','HTTP','HTTPS') | schema / healthmonitors |
| healthmonitors.delay | delay / interval / check interval / frequency / period / seconds between checks | int | schema / healthmonitors |
| healthmonitors.timeout | timeout / response timeout / max wait time / timeout seconds / deadline | int | schema / healthmonitors |
| healthmonitors.max_retries | max retries / maximum retries / retries / retry count / max attempts / failure threshold | int | schema / healthmonitors |
| healthmonitors.http_method | http method / request method / http verb / method / get post put | varchar(16) | schema / healthmonitors |
| healthmonitors.url_path | url path / path / endpoint / url / check path / resource path | varchar(255) | schema / healthmonitors |
| healthmonitors.expected_codes | expected codes / expected status codes / success codes / valid responses / http status codes / expected response | varchar(64) | schema / healthmonitors |
| healthmonitors.admin_state_up | admin state up / enabled / active / status / admin state / is up | tinyint(1) | schema / healthmonitors |

## ikepolicies

Stores the configuration parameters for Internet Key Exchange (IKE) policies used in IPsec VPN connections, including encryption, authentication, and lifetime settings.

恢复表名: ikepolicies / IKE Policies / IPsec IKE Policies / IKE Policy Definitions / IPsec Phase 1 Policies / IKE Security Policies
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ikepolicies.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Account ID / Service Tenant | varchar(255) | schema / ikepolicies |
| ikepolicies.id | id / identifier / Policy ID / Unique Identifier / IKE Policy ID / Resource ID / UUID | varchar(36) | schema / ikepolicies |
| ikepolicies.name | name / Policy Name / IKE Policy Name / Label / Title / Display Name | varchar(255) | schema / ikepolicies |
| ikepolicies.description | description / Policy Description / Notes / Details / Comment / Description Text | varchar(255) | schema / ikepolicies |
| ikepolicies.auth_algorithm | auth algorithm / Authentication Algorithm / Auth Algo / Hash Algorithm / Integrity Algorithm / Authentication Method | enum('sha1') | schema / ikepolicies |
| ikepolicies.encryption_algorithm | encryption algorithm / Cipher / Encryption Method / Crypto Algorithm / Encryption Type | enum('3des','aes-128','aes-256','aes-192') | schema / ikepolicies |
| ikepolicies.phase1_negotiation_mode | phase1 negotiation mode / Phase 1 Mode / Negotiation Mode / IKE Phase 1 Mode / Main Mode / Aggressive Mode | enum('main') | schema / ikepolicies |
| ikepolicies.lifetime_units | lifetime units / Lifetime Unit / Time Unit / Duration Unit / Measurement Unit / Lifetime Metric | enum('seconds','kilobytes') | schema / ikepolicies |
| ikepolicies.lifetime_value | lifetime value / Duration / Time Limit / Data Limit / Policy Lifetime | int | schema / ikepolicies |
| ikepolicies.ike_version | ike version / Protocol Version / Version / IKEv1 / IKEv2 | enum('v1','v2') | schema / ikepolicies |
| ikepolicies.pfs | pfs / Perfect Forward Secrecy / PFS Group / Diffie-Hellman Group / DH Group / Forward Secrecy Group | enum('group2','group5','group14') | schema / ikepolicies |

## ipallocationpools

Stores the IP address allocation pools (ranges) defined for subnets, specifying the first and last IP addresses available for allocation within a specific subnet.

恢复表名: ipallocationpools / ip_allocation_pools / allocation_pools / ip_pools / subnet_allocation_pools / ip_range_pools
SQL表别名: iap, p, p2, p3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipallocationpools.id | id / identifier / pool_id / allocation_pool_id / ip_pool_id / unique_identifier / primary_key | varchar(36) | neutron_190, neutron_262, neutron_657, neutron_791, neutron_792 |
| ipallocationpools.subnet_id | subnet id / subnet identifier / subnet_identifier / parent_subnet_id / associated_subnet / subnet_reference / foreign_key_subnet | varchar(36) | neutron_190, neutron_262, neutron_657, neutron_791, neutron_792, neutron_1008, neutron_108, neutron_28 |
| ipallocationpools.first_ip | first ip / start_ip / beginning_ip / lowest_ip / pool_start / allocation_start_ip / first_address | varchar(64) | neutron_190, neutron_262, neutron_657, neutron_791, neutron_792, neutron_1008, neutron_108, neutron_28 |
| ipallocationpools.last_ip | last ip / end_ip / ending_ip / highest_ip / pool_end / allocation_end_ip / last_address | varchar(64) | neutron_190, neutron_262, neutron_657, neutron_791, neutron_792, neutron_1008, neutron_108, neutron_28 |

## ipallocations

Stores the mapping of allocated IP addresses to network ports, including the specific subnet and network context for each allocation.

恢复表名: ipallocations / ip_allocations / ip_allocation / ip_allocation_records / allocated_ips / port_ip_mappings / network_ip_assignments
SQL表别名: a, ia, ip

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipallocations.port_id | port id / port identifier / port uuid / associated port / network port id / port reference | varchar(36) | neutron_125, neutron_610, neutron_10, neutron_1001, neutron_1002, neutron_111, neutron_128, neutron_13 |
| ipallocations.ip_address | ip address / allocated ip / address / ipv4 address / ipv6 address / network address / assigned ip | varchar(64) | neutron_125, neutron_610, neutron_10, neutron_1001, neutron_1002, neutron_111, neutron_128, neutron_13 |
| ipallocations.subnet_id | subnet id / subnet identifier / subnet uuid / associated subnet / subnet reference / network segment id | varchar(36) | neutron_125, neutron_610, neutron_10, neutron_1001, neutron_1002, neutron_111, neutron_128, neutron_13 |
| ipallocations.network_id | network id / network identifier / network uuid / associated network / network reference / parent network id | varchar(36) | neutron_125, neutron_610 |

## ipamallocationpools

Stores IP address allocation pool definitions, specifying the range of IP addresses (from first to last) allocated to a specific IPAM subnet.

恢复表名: ipamallocationpools / IPAM Allocation Pools / IP Allocation Pools / IPAM Pools / IP Pool Allocations / IP Address Allocation Pools
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipamallocationpools.id | id / identifier / Allocation Pool ID / Pool ID / IPAM Pool ID / Unique Identifier / Pool Identifier | varchar(36) | schema / ipamallocationpools |
| ipamallocationpools.ipam_subnet_id | ipam subnet id / ipam subnet identifier / Subnet ID / Parent Subnet ID / Associated Subnet | varchar(36) | schema / ipamallocationpools |
| ipamallocationpools.first_ip | first ip / First IP Address / Start IP / Beginning IP / Lowest IP / Pool Start Address / First IP in Range | varchar(64) | schema / ipamallocationpools |
| ipamallocationpools.last_ip | last ip / Last IP Address / End IP / Ending IP / Highest IP / Pool End Address / Last IP in Range | varchar(64) | schema / ipamallocationpools |

## ipamallocations

Stores records of IP address allocations within IPAM subnets, tracking the status of each allocated IP address.

恢复表名: ipamallocations / IPAM Allocations / IP Address Allocations / IP Allocation Records / IPAM Allocation Table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipamallocations.ip_address | ip address / Allocated IP / IP / Address / IPv4 Address / IPv6 Address | varchar(64) | schema / ipamallocations |
| ipamallocations.status | status / Allocation Status / State / IP Status / Current Status / Lifecycle State | varchar(36) | schema / ipamallocations |
| ipamallocations.ipam_subnet_id | ipam subnet id / ipam subnet identifier / Subnet ID / Subnet Identifier / Parent Subnet ID / IPAM Subnet | varchar(36) | schema / ipamallocations |

## ipamavailabilityranges

Stores the defined IP address ranges (from first to last IP) associated with specific allocation pools in the IPAM system.

恢复表名: ipamavailabilityranges / IPAM Availability Ranges / IP Availability Ranges / IPAM Ranges / IP Ranges / Availability Ranges / IPAM IP Ranges
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipamavailabilityranges.allocation_pool_id | allocation pool id / allocation pool identifier / Pool ID / IPAM Pool ID / Pool Identifier | varchar(36) | schema / ipamavailabilityranges |
| ipamavailabilityranges.first_ip | first ip / Start IP / Beginning IP / Low IP / First Address / Start Address | varchar(64) | schema / ipamavailabilityranges |
| ipamavailabilityranges.last_ip | last ip / End IP / Ending IP / High IP / Last Address / End Address | varchar(64) | schema / ipamavailabilityranges |

## ipamsubnets

Maps Neutron subnets to IP Address Management (IPAM) resources, linking network segments to their IP allocation contexts.

恢复表名: ipamsubnets / IPAM Subnets / IP Address Management Subnets / Subnet IPAM Mapping / Neutron Subnet IPAM / IPAM Network Segments
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipamsubnets.id | id / identifier / IPAM Subnet ID / Record ID / Primary Key / Unique Identifier / IPAM Subnet UUID | varchar(36) | schema / ipamsubnets |
| ipamsubnets.neutron_subnet_id | neutron subnet id / neutron subnet identifier / Subnet UUID / Network Subnet Identifier / Neutron Network Segment ID / Associated Subnet ID | varchar(36) | schema / ipamsubnets |

## ipavailabilityranges

Stores the ranges of available IP addresses within specific allocation pools, defined by their first and last IP addresses.

恢复表名: ipavailabilityranges / IP Availability Ranges / IP Ranges / Available IP Ranges / IP Allocation Pools / Network IP Ranges
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipavailabilityranges.allocation_pool_id | allocation pool id / allocation pool identifier / Pool ID / IP Pool ID / Pool UUID | varchar(36) | schema / ipavailabilityranges |
| ipavailabilityranges.first_ip | first ip / Start IP / Beginning IP / Lower IP Bound / Initial IP Address / First IP Address | varchar(64) | schema / ipavailabilityranges |
| ipavailabilityranges.last_ip | last ip / End IP / Final IP / Upper IP Bound / Terminating IP Address / Last IP Address | varchar(64) | schema / ipavailabilityranges |

## ipsec_site_connections

Stores configuration details for IPSec site-to-site VPN connections, including peer addresses, authentication methods, DPD settings, and associated policies.

恢复表名: ipsec site connections / site-to-site VPN connections / IPSec tunnels / VPN site connections / site connections
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipsec_site_connections.tenant_id | tenant id / tenant identifier / project ID / project / tenant / owner / account ID | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.id | id / identifier / connection ID / site connection ID / UUID / primary key | varchar(36) | schema / ipsec_site_connections |
| ipsec_site_connections.name | name / connection name / label / title / display name | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.description | description / notes / details / comment / description text | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.peer_address | peer address / remote IP / peer IP / remote address / gateway IP / public IP | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.peer_id | peer id / peer identifier / remote ID / remote certificate ID / peer cert | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.route_mode | route mode / routing mode / mode / static / dynamic | varchar(8) | schema / ipsec_site_connections |
| ipsec_site_connections.mtu | mtu / maximum transmission unit / MTU size / packet size | int | schema / ipsec_site_connections |
| ipsec_site_connections.initiator | initiator / initiation mode / bidirectional / response only / initiator type | enum('bi-directional','response-only') | schema / ipsec_site_connections |
| ipsec_site_connections.auth_mode | auth mode / authentication mode / auth type / pre-shared key / certificate | varchar(16) | schema / ipsec_site_connections |
| ipsec_site_connections.psk | psk / pre-shared key / secret / password / shared secret | varchar(255) | schema / ipsec_site_connections |
| ipsec_site_connections.dpd_action | dpd action / dead peer detection action / keepalive action / failure action | enum('hold','clear','restart','disabled','restart-by-peer') | schema / ipsec_site_connections |
| ipsec_site_connections.dpd_interval | dpd interval / dead peer detection interval / keepalive interval / check interval | int | schema / ipsec_site_connections |
| ipsec_site_connections.dpd_timeout | dpd timeout / dead peer detection timeout / keepalive timeout / failure timeout | int | schema / ipsec_site_connections |
| ipsec_site_connections.status | status / connection status / state / active / inactive | varchar(16) | schema / ipsec_site_connections |
| ipsec_site_connections.admin_state_up | admin state up / admin up / enabled / disabled / administrative state | tinyint(1) | schema / ipsec_site_connections |
| ipsec_site_connections.vpnservice_id | vpnservice id / vpnservice identifier / VPN service ID / service ID / parent service | varchar(36) | schema / ipsec_site_connections |
| ipsec_site_connections.ipsecpolicy_id | ipsecpolicy id / ipsecpolicy identifier / IPSec policy ID / policy ID / security policy | varchar(36) | schema / ipsec_site_connections |
| ipsec_site_connections.ikepolicy_id | ikepolicy id / ikepolicy identifier / IKE policy ID / IKE policy / key exchange policy | varchar(36) | schema / ipsec_site_connections |

## ipsecpeercidrs

Stores the CIDR blocks of remote networks (peers) associated with specific IPsec site connections in the Neutron networking service.

恢复表名: ipsecpeercidrs / IPsec peer CIDRs / IPsec peer networks / IPsec site connection peer CIDRs / IPsec remote networks / IPsec tunnel peer subnets
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipsecpeercidrs.cidr | cidr / network CIDR / peer CIDR / remote CIDR / subnet CIDR / network address / IP range | varchar(32) | schema / ipsecpeercidrs |
| ipsecpeercidrs.ipsec_site_connection_id | ipsec site connection id / ipsec site connection identifier / connection ID / IPsec connection ID / site connection ID / tunnel ID / IPsec tunnel ID | varchar(36) | schema / ipsecpeercidrs |

## ipsecpolicies

Stores configuration details for IPsec security policies, including encryption, authentication, and lifetime parameters used for secure network communication.

恢复表名: ipsecpolicies / IPsec Policies / IPsec Policy / Security Policies / IP Security Policies / IPsec Security Association Policies
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ipsecpolicies.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Account ID | varchar(255) | schema / ipsecpolicies |
| ipsecpolicies.id | id / identifier / Policy ID / IPsec Policy ID / Unique Identifier / Policy UUID / Record ID | varchar(36) | schema / ipsecpolicies |
| ipsecpolicies.name | name / Policy Name / IPsec Policy Name / Label / Policy Title / Display Name | varchar(255) | schema / ipsecpolicies |
| ipsecpolicies.description | description / Policy Description / Notes / Comments / Policy Details / Description Text | varchar(255) | schema / ipsecpolicies |
| ipsecpolicies.transform_protocol | transform protocol / IPsec Protocol / Security Protocol / Protocol Type / ESP/AH Mode | enum('esp','ah','ah-esp') | schema / ipsecpolicies |
| ipsecpolicies.auth_algorithm | auth algorithm / Authentication Algorithm / Hash Algorithm / Integrity Algorithm / Authentication Method | enum('sha1') | schema / ipsecpolicies |
| ipsecpolicies.encryption_algorithm | encryption algorithm / Cipher / Encryption Method / Crypto Algorithm / Data Encryption Standard | enum('3des','aes-128','aes-256','aes-192') | schema / ipsecpolicies |
| ipsecpolicies.encapsulation_mode | encapsulation mode / IPsec Mode / Tunnel/Transport Mode / Mode / Packet Mode | enum('tunnel','transport') | schema / ipsecpolicies |
| ipsecpolicies.lifetime_units | lifetime units / SA Lifetime Units / Time/Size Unit / Lifetime Measurement / Unit of Lifetime | enum('seconds','kilobytes') | schema / ipsecpolicies |
| ipsecpolicies.lifetime_value | lifetime value / SA Lifetime / Policy Duration / Lifetime Limit / Max Lifetime | int | schema / ipsecpolicies |
| ipsecpolicies.pfs | pfs / Perfect Forward Secrecy / PFS Group / Diffie-Hellman Group / Key Exchange Group / PFS Setting | enum('group2','group5','group14') | schema / ipsecpolicies |

## lbaas_healthmonitors

Stores configuration details for health monitors used by OpenStack Load Balancer (LBaaS) to check the status of backend pool members.

恢复表名: lbaas healthmonitors / load balancer health monitors / health monitor / lbaas health monitor / openstack load balancer health check / health check configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_healthmonitors.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner / account id | varchar(255) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.id | id / identifier / health monitor id / monitor id / uuid / unique identifier | varchar(36) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.type | type / monitor type / protocol / check type / health check protocol | enum('PING','TCP','HTTP','HTTPS') | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.delay | delay / interval / check interval / frequency / polling delay | int | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.timeout | timeout / response timeout / wait time / max wait / check timeout | int | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.max_retries | max retries / maximum retries / retries / max attempts / retry limit / failure threshold | int | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.http_method | http method / request method / http verb / method / get post put | varchar(16) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.url_path | url path / path / endpoint path / url / check path | varchar(255) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.expected_codes | expected codes / expected status codes / valid codes / success codes / http status codes | varchar(64) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.admin_state_up | admin state up / enabled / active / admin state / status enabled | tinyint(1) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.provisioning_status | provisioning status / status / state / provisioning state / current status | varchar(16) | schema / lbaas_healthmonitors |
| lbaas_healthmonitors.name | name / monitor name / label / display name / title | varchar(255) | schema / lbaas_healthmonitors |

## lbaas_l7policies

Stores Layer 7 (HTTP/HTTPS) policies for OpenStack Load Balancer as a Service (LBaaS), defining actions like redirects or rejections based on listener rules.

恢复表名: lbaas l7policies / L7 Policies / Layer 7 Policies / Load Balancer L7 Policies / LBaaS L7 Policies / HTTP Policies / Web Policies
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_l7policies.tenant_id | tenant id / tenant identifier / Project ID / Project / Tenant / Owner / Account ID / User ID | varchar(255) | schema / lbaas_l7policies |
| lbaas_l7policies.id | id / identifier / Policy ID / L7 Policy ID / Unique ID / Policy UUID | varchar(36) | schema / lbaas_l7policies |
| lbaas_l7policies.name | name / Policy Name / Label / Title / Display Name | varchar(255) | schema / lbaas_l7policies |
| lbaas_l7policies.description | description / Policy Description / Notes / Details / Comment | varchar(255) | schema / lbaas_l7policies |
| lbaas_l7policies.listener_id | listener id / listener identifier / Associated Listener / LB Listener / Parent Listener | varchar(36) | schema / lbaas_l7policies |
| lbaas_l7policies.action | action / Policy Action / Behavior / Response Type / L7 Action / Handling Method | enum('REJECT','REDIRECT_TO_URL','REDIRECT_TO_POOL') | schema / lbaas_l7policies |
| lbaas_l7policies.redirect_pool_id | redirect pool id / redirect pool identifier / Target Pool ID / Redirect Pool / Destination Pool / Pool ID | varchar(36) | schema / lbaas_l7policies |
| lbaas_l7policies.redirect_url | redirect url / Target URL / Destination URL / Link | varchar(255) | schema / lbaas_l7policies |
| lbaas_l7policies.position | position / Order / Priority / Sequence / Rank / Index | int | schema / lbaas_l7policies |
| lbaas_l7policies.provisioning_status | provisioning status / Status / State / Provisioning State / Health Status | varchar(16) | schema / lbaas_l7policies |
| lbaas_l7policies.admin_state_up | admin state up / Enabled / Active / Admin State / Up/Down / Status Flag | tinyint(1) | schema / lbaas_l7policies |

## lbaas_l7rules

Stores Layer 7 (application layer) rules for OpenStack Load Balancer as a Service (LBaaS), defining conditions based on HTTP headers, cookies, hostnames, paths, or file types to route traffic.

恢复表名: lbaas l7rules / L7 Rules / Layer 7 Rules / Load Balancer L7 Rules / LBaaS L7 Rules / HTTP Rules / Advanced Load Balancing Rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_l7rules.tenant_id | tenant id / tenant identifier / Project ID / Project / Tenant / Owner / Account ID / User Project | varchar(255) | schema / lbaas_l7rules |
| lbaas_l7rules.id | id / identifier / Rule ID / Unique Identifier / UUID / Rule UUID / Primary Key | varchar(36) | schema / lbaas_l7rules |
| lbaas_l7rules.l7policy_id | l7policy id / l7policy identifier / Policy ID / L7 Policy ID / Parent Policy / Associated Policy / Policy UUID | varchar(36) | schema / lbaas_l7rules |
| lbaas_l7rules.type | type / Rule Type / Condition Type / Match Type / Attribute Type / HTTP Attribute | enum('HOST_NAME','PATH','FILE_TYPE','HEADER','COOKIE') | schema / lbaas_l7rules |
| lbaas_l7rules.compare_type | compare type / Comparison Type / Operator / Match Operator / Comparison Operator / Logic Type | enum('REGEX','STARTS_WITH','ENDS_WITH','CONTAINS','EQUAL_TO') | schema / lbaas_l7rules |
| lbaas_l7rules.invert | invert / Invert Flag / Negate / Not Match / Inverse / Boolean Invert | tinyint(1) | schema / lbaas_l7rules |
| lbaas_l7rules.key | key / Rule Key / Header Name / Cookie Name / Attribute Name / Field Name | varchar(255) | schema / lbaas_l7rules |
| lbaas_l7rules.value | value / Rule Value / Match Value / Expected Value / Pattern / Target Value | varchar(255) | schema / lbaas_l7rules |
| lbaas_l7rules.provisioning_status | provisioning status / Status / Provisioning State / Rule Status / Lifecycle Status / State | varchar(16) | schema / lbaas_l7rules |
| lbaas_l7rules.admin_state_up | admin state up / Admin State / Enabled / Active Flag / Admin Enabled / State Up | tinyint(1) | schema / lbaas_l7rules |

## lbaas_listeners

Stores configuration details for OpenStack Load Balancer (LBaaS) listeners, including protocol, port, associated load balancer, and default pool.

恢复表名: lbaas listeners / load balancer listeners / lb listeners / listener configurations / network listeners / lbaas listener table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_listeners.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner id / account id | varchar(255) | schema / lbaas_listeners |
| lbaas_listeners.id | id / identifier / listener id / uuid / unique identifier / listener uuid | varchar(36) | schema / lbaas_listeners |
| lbaas_listeners.name | name / listener name / display name / label / title | varchar(255) | schema / lbaas_listeners |
| lbaas_listeners.description | description / listener description / notes / details / comment | varchar(255) | schema / lbaas_listeners |
| lbaas_listeners.protocol | protocol / listener protocol / network protocol / communication protocol / http tcp https | enum('HTTP','HTTPS','TCP','TERMINATED_HTTPS') | schema / lbaas_listeners |
| lbaas_listeners.protocol_port | protocol port / port / listener port / network port / port number | int | schema / lbaas_listeners |
| lbaas_listeners.connection_limit | connection limit / max connections / connection cap / limit / concurrency limit | int | schema / lbaas_listeners |
| lbaas_listeners.loadbalancer_id | loadbalancer id / loadbalancer identifier / load balancer id / lb id / parent lb / associated load balancer | varchar(36) | schema / lbaas_listeners |
| lbaas_listeners.default_pool_id | default pool id / default pool identifier / pool id / default pool / backend pool / associated pool | varchar(36) | schema / lbaas_listeners |
| lbaas_listeners.admin_state_up | admin state up / admin state / enabled / active flag / status up | tinyint(1) | schema / lbaas_listeners |
| lbaas_listeners.provisioning_status | provisioning status / provisioning state / creation status / resource status / state | varchar(16) | schema / lbaas_listeners |
| lbaas_listeners.operating_status | operating status / operating state / runtime status / online status / health status | varchar(16) | schema / lbaas_listeners |
| lbaas_listeners.default_tls_container_id | default tls container id / default tls container identifier / tls container id / ssl container / certificate container / tls id | varchar(128) | schema / lbaas_listeners |

## lbaas_loadbalancer_statistics

Stores performance and traffic statistics for OpenStack Load Balancer (LBaaS) resources, including byte counts and connection metrics, linked to specific load balancer instances.

恢复表名: lbaas loadbalancer statistics / load balancer statistics / lb statistics / loadbalancer stats / lb stats / load balancer metrics / lb metrics / load balancer performance data
SQL表别名: s, stats, stats2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_loadbalancer_statistics.loadbalancer_id | loadbalancer id / loadbalancer identifier / load balancer id / lb id / lb identifier / balancer id / load balancer uuid | varchar(36) | neutron_228, neutron_23, neutron_258, neutron_293, neutron_318, neutron_326, neutron_328, neutron_369 |
| lbaas_loadbalancer_statistics.bytes_in | bytes in / incoming bytes / input bytes / bytes received / download bytes / inbound traffic bytes / bytes downloaded | bigint | neutron_228, neutron_23, neutron_258, neutron_293, neutron_318, neutron_326, neutron_328, neutron_369 |
| lbaas_loadbalancer_statistics.bytes_out | bytes out / outgoing bytes / output bytes / bytes sent / upload bytes / outbound traffic bytes / bytes uploaded | bigint | schema / lbaas_loadbalancer_statistics |
| lbaas_loadbalancer_statistics.active_connections | active connections / current connections / open connections / live connections / concurrent connections / active session count | bigint | schema / lbaas_loadbalancer_statistics |
| lbaas_loadbalancer_statistics.total_connections | total connections / connection count / total connection count / cumulative connections / total sessions / connection total | bigint | neutron_228, neutron_23, neutron_258, neutron_293, neutron_318, neutron_326, neutron_328, neutron_369 |

## lbaas_loadbalanceragentbindings

Maps load balancer instances to the specific agents responsible for managing them in the Neutron LBaaS service.

恢复表名: lbaas loadbalanceragentbindings / load balancer agent bindings / lbaas agent bindings / load balancer to agent mapping / agent load balancer associations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_loadbalanceragentbindings.loadbalancer_id | loadbalancer id / loadbalancer identifier / load balancer id / lb id / load balancer uuid / balancer identifier | varchar(36) | schema / lbaas_loadbalanceragentbindings |
| lbaas_loadbalanceragentbindings.agent_id | agent id / agent identifier / agent uuid / load balancer agent identifier / managing agent id | varchar(36) | schema / lbaas_loadbalanceragentbindings |

## lbaas_loadbalancers

Stores metadata for OpenStack Load Balancer as a Service (LBaaS) load balancer instances, including their identity, ownership, network attachment, and operational status.

恢复表名: lbaas loadbalancers / load balancers / loadbalancers / LBs / load_balancers / lbaas_loadbalancer / OpenStack LBaaS load balancers
SQL表别名: lb, lb2, lb3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_loadbalancers.tenant_id | tenant id / tenant identifier / tenant / project / project_id / owner / account / customer | varchar(255) | neutron_23, neutron_400, neutron_275, neutron_293, neutron_318, neutron_326, neutron_68 |
| lbaas_loadbalancers.id | id / identifier / load balancer ID / LB ID / loadbalancer_id / uuid / primary key / resource ID | varchar(36) | neutron_23, neutron_400, neutron_275, neutron_247, neutron_293, neutron_318, neutron_326, neutron_593 |
| lbaas_loadbalancers.name | name / load balancer name / LB name / title / label / display name | varchar(255) | neutron_23, neutron_275, neutron_247, neutron_293, neutron_318, neutron_326, neutron_593, neutron_607 |
| lbaas_loadbalancers.description | description / load balancer description / LB description / notes / details / comment | varchar(255) | schema / lbaas_loadbalancers |
| lbaas_loadbalancers.vip_port_id | vip port id / vip port identifier / port ID / virtual IP port / network port / port_uuid | varchar(36) | schema / lbaas_loadbalancers |
| lbaas_loadbalancers.vip_subnet_id | vip subnet id / vip subnet identifier / subnet ID / virtual IP subnet / network subnet / subnet_uuid | varchar(36) | neutron_400 |
| lbaas_loadbalancers.vip_address | vip address / Virtual IP / IP address / load balancer IP / floating IP / endpoint IP | varchar(36) | neutron_23, neutron_247, neutron_293, neutron_318, neutron_326, neutron_593, neutron_607, neutron_620 |
| lbaas_loadbalancers.admin_state_up | admin state up / admin state / enabled / active flag / admin enabled / status up | tinyint(1) | neutron_275, neutron_68, neutron_798 |
| lbaas_loadbalancers.provisioning_status | provisioning status / LB status / resource status / creation status / state | varchar(16) | neutron_400, neutron_247, neutron_293, neutron_318, neutron_326, neutron_593, neutron_607, neutron_620 |
| lbaas_loadbalancers.operating_status | operating status / operational status / runtime status / online status / health status | varchar(16) | neutron_23, neutron_400, neutron_275, neutron_247, neutron_593, neutron_607, neutron_620, neutron_68 |
| lbaas_loadbalancers.flavor_id | flavor id / flavor identifier / LB flavor / size / specification / capacity tier | varchar(36) | schema / lbaas_loadbalancers |

## lbaas_members

Stores the backend server members associated with load balancer pools, including their network addresses, ports, weights, and operational status.

恢复表名: lbaas members / load balancer members / lb members / pool members / member pool / lbaas member / load balancer pool member
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_members.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner / account id / user id | varchar(255) | schema / lbaas_members |
| lbaas_members.id | id / identifier / member id / uuid / unique identifier / member uuid / primary key | varchar(36) | schema / lbaas_members |
| lbaas_members.pool_id | pool id / pool identifier / pool / load balancer pool / lb pool / pool uuid / associated pool | varchar(36) | schema / lbaas_members |
| lbaas_members.subnet_id | subnet id / subnet identifier / subnet / network subnet / subnet uuid / network id / associated subnet | varchar(36) | schema / lbaas_members |
| lbaas_members.address | address / ip address / ip / server ip / backend ip / member ip / address with cidr | varchar(64) | schema / lbaas_members |
| lbaas_members.protocol_port | protocol port / port / backend port / server port / protocol port number / member port | int | schema / lbaas_members |
| lbaas_members.weight | weight / load weight / traffic weight / member weight / distribution weight | int | schema / lbaas_members |
| lbaas_members.admin_state_up | admin state up / admin state / enabled / active state / admin enabled / up state | tinyint(1) | schema / lbaas_members |
| lbaas_members.provisioning_status | provisioning status / provisioning state / status / provisioning / resource status | varchar(16) | schema / lbaas_members |
| lbaas_members.operating_status | operating status / operating state / online status / health status / operational status | varchar(16) | schema / lbaas_members |
| lbaas_members.name | name / member name / label / display name / member label | varchar(255) | schema / lbaas_members |

## lbaas_pools

Stores configuration and status details for load balancer pools, including protocol, load balancing algorithm, and associated load balancer and health monitor references.

恢复表名: lbaas pools / load balancer pools / lb pools / pools / load balancer pool / lbaas pool / pool
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_pools.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner id / account id / user id | varchar(255) | schema / lbaas_pools |
| lbaas_pools.id | id / identifier / pool id / uuid / unique identifier / pool uuid / primary key | varchar(36) | schema / lbaas_pools |
| lbaas_pools.name | name / pool name / label / title / display name | varchar(255) | schema / lbaas_pools |
| lbaas_pools.description | description / pool description / notes / details / remarks | varchar(255) | schema / lbaas_pools |
| lbaas_pools.protocol | protocol / lb protocol / network protocol / service protocol / http tcp https | enum('HTTP','HTTPS','TCP') | schema / lbaas_pools |
| lbaas_pools.lb_algorithm | lb algorithm / load balancing algorithm / balancing method / distribution algorithm / round robin / least connections / source ip | enum('ROUND_ROBIN','LEAST_CONNECTIONS','SOURCE_IP') | schema / lbaas_pools |
| lbaas_pools.healthmonitor_id | healthmonitor id / healthmonitor identifier / health monitor id / monitor id / health check id / monitor uuid | varchar(36) | schema / lbaas_pools |
| lbaas_pools.admin_state_up | admin state up / admin state / enabled / active state / up down / status flag | tinyint(1) | schema / lbaas_pools |
| lbaas_pools.provisioning_status | provisioning status / provisioning state / creation status / build status / active pending | varchar(16) | schema / lbaas_pools |
| lbaas_pools.operating_status | operating status / operating state / runtime status / online offline / health status | varchar(16) | schema / lbaas_pools |
| lbaas_pools.loadbalancer_id | loadbalancer id / loadbalancer identifier / load balancer id / lb id / parent lb id / load balancer uuid | varchar(36) | schema / lbaas_pools |

## lbaas_sessionpersistences

Stores session persistence configurations for load balancer pools, defining how client sessions are maintained across backend members.

恢复表名: lbaas sessionpersistences / load balancer session persistences / session persistence configurations / lbaas session persistence / load balancer persistence settings / session affinity rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_sessionpersistences.pool_id | pool id / pool identifier / load balancer pool id / pool uuid / associated pool | varchar(36) | schema / lbaas_sessionpersistences |
| lbaas_sessionpersistences.type | type / persistence type / session persistence method / affinity type / persistence mode | enum('SOURCE_IP','HTTP_COOKIE','APP_COOKIE') | schema / lbaas_sessionpersistences |
| lbaas_sessionpersistences.cookie_name | cookie name / cookie identifier / persistence cookie name / session cookie / cookie label | varchar(1024) | schema / lbaas_sessionpersistences |

## lbaas_sni

Stores Server Name Indication (SNI) configurations associated with specific load balancer listeners and TLS containers, including their ordering position.

恢复表名: lbaas sni / Load Balancer SNI / SNI Configuration / Server Name Indication / TLS SNI Mapping / Listener SNI / SNI Hosts
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lbaas_sni.listener_id | listener id / listener identifier / LB Listener ID / Load Balancer Listener / Associated Listener / Listener UUID | varchar(36) | schema / lbaas_sni |
| lbaas_sni.tls_container_id | tls container id / tls container identifier / TLS ID / Certificate Container / TLS Certificate ID / Security Container ID | varchar(128) | schema / lbaas_sni |
| lbaas_sni.position | position / Order / Priority / Sequence Number / SNI Order | int | schema / lbaas_sni |

## lsn

Stores logical sequence number (LSN) records, likely tracking transaction log positions or commit points, associated with specific network identifiers.

恢复表名: lsn / logical sequence numbers / lsn table / log sequence numbers
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lsn.lsn_id | lsn id / lsn identifier / logical sequence number id / log sequence number id / lsn uuid / primary key | varchar(36) | schema / lsn |
| lsn.net_id | net id / net identifier / network id / network identifier / associated network / network uuid | varchar(36) | schema / lsn |

## lsn_port

Maps logical switch network (LSN) ports to specific physical or virtual network ports, identified by MAC address and subscription context.

恢复表名: lsn port / lsn_port / logical_switch_network_port / lsn_ports / network_port_mapping / port_assignment
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| lsn_port.lsn_port_id | lsn port id / lsn port identifier / lsn_port_id / port_id / lsn_port_identifier / unique_port_id / port_uuid | varchar(36) | schema / lsn_port |
| lsn_port.lsn_id | lsn id / lsn identifier / lsn_id / logical_switch_network_id / network_id / lsn_identifier / network_uuid | varchar(36) | schema / lsn_port |
| lsn_port.sub_id | sub id / sub identifier / sub_id / subscription_id / subscriber_id / sub_identifier / tenant_id | varchar(36) | schema / lsn_port |
| lsn_port.mac_addr | mac addr / mac address / mac_addr / mac_address / media_access_control_address / hardware_address / physical_address | varchar(32) | schema / lsn_port |

## maclearningstates

Stores the MAC learning enablement status for each network port in the Neutron networking service.

恢复表名: maclearningstates / mac_learning_states / mac_learning_config / port_mac_learning / mac_learning_settings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| maclearningstates.port_id | port id / port identifier / port_id / port_uuid / network_port_id / port_identifier | varchar(36) | schema / maclearningstates |
| maclearningstates.mac_learning_enabled | mac learning enabled / mac_learning_enabled / mac_learning / mac_learning_state / mac_learning_flag / is_mac_learning_on | tinyint(1) | schema / maclearningstates |

## members

Stores the backend server members associated with a load balancer pool, including their network address, port, weight, and operational status.

恢复表名: members / load_balancer_members / lb_members / pool_members / member / load balancer member
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| members.tenant_id | tenant id / tenant identifier / project_id / project / tenant / owner / account_id / user_id | varchar(255) | schema / members |
| members.id | id / identifier / member_id / uuid / unique_id / primary_key / member_uuid | varchar(36) | schema / members |
| members.pool_id | pool id / pool identifier / pool / load_balancer_pool_id / associated_pool / parent_pool / pool_uuid | varchar(36) | schema / members |
| members.address | address / ip_address / server_ip / backend_ip / host_address / network_address / ip | varchar(64) | schema / members |
| members.protocol_port | protocol port / port / server_port / backend_port / destination_port / port_number | int | schema / members |
| members.weight | weight / load_weight / traffic_weight / priority / distribution_weight / member_weight | int | schema / members |
| members.status | status / operational_status / state / member_state / health_status / current_status | varchar(16) | schema / members |
| members.status_description | status description / status_reason / error_message / description / status_details / health_check_result | varchar(255) | schema / members |
| members.admin_state_up | admin state up / enabled / is_enabled / admin_enabled / active_flag / up_down | tinyint(1) | schema / members |

## meteringlabelrules

Defines rules for applying metering labels to network traffic based on direction and remote IP prefixes, with options to exclude specific traffic.

恢复表名: meteringlabelrules / metering label rules / metering rules / label rules / traffic metering rules / network metering configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| meteringlabelrules.id | id / identifier / rule id / primary key / unique id | varchar(36) | schema / meteringlabelrules |
| meteringlabelrules.direction | direction / traffic direction / ingress egress / flow direction / network direction | enum('ingress','egress') | schema / meteringlabelrules |
| meteringlabelrules.remote_ip_prefix | remote ip prefix / remote ip / ip prefix / source ip / destination ip / network prefix | varchar(64) | schema / meteringlabelrules |
| meteringlabelrules.metering_label_id | metering label id / metering label identifier / label id / metering label / label identifier / associated label | varchar(36) | schema / meteringlabelrules |
| meteringlabelrules.excluded | excluded / is excluded / exclusion flag / exclude traffic / active status | tinyint(1) | schema / meteringlabelrules |

## meteringlabels

Stores definitions and metadata for metering labels used to categorize or tag metering data within the Neutron system.

恢复表名: meteringlabels / metering labels / metering label / label / labels / metering label definitions / label metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| meteringlabels.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner id / account id | varchar(255) | schema / meteringlabels |
| meteringlabels.id | id / identifier / label id / primary key / unique id | varchar(36) | schema / meteringlabels |
| meteringlabels.name | name / label name / label title / label key / label identifier name | varchar(255) | schema / meteringlabels |
| meteringlabels.description | description / label description / label details / label notes / label info | varchar(1024) | schema / meteringlabels |
| meteringlabels.shared | shared / is shared / visibility / public label / shared flag / access scope | tinyint(1) | schema / meteringlabels |

## ml2_brocadenetworks

Stores network configuration details for Brocade fabric networks, including VLAN assignments and segment identifiers within the Neutron ML2 plugin.

恢复表名: ml2 brocadenetworks / Brocade Networks / ML2 Brocade Network / Brocade Network Configuration / Fabric Network / Brocade VLAN Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_brocadenetworks.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Customer ID / Account ID | varchar(255) | schema / ml2_brocadenetworks |
| ml2_brocadenetworks.id | id / identifier / Network ID / Unique ID / Primary Key / Record ID / Brocade Network ID | varchar(36) | schema / ml2_brocadenetworks |
| ml2_brocadenetworks.vlan | vlan / VLAN ID / VLAN Tag / Virtual LAN / VLAN Number / Network VLAN | varchar(10) | schema / ml2_brocadenetworks |
| ml2_brocadenetworks.segment_id | segment id / segment identifier / Network Segment / Physical Segment / Fabric Segment | varchar(36) | schema / ml2_brocadenetworks |
| ml2_brocadenetworks.network_type | network type / Type / Network Category / Protocol Type / Fabric Type | varchar(10) | schema / ml2_brocadenetworks |

## ml2_brocadeports

Stores configuration details for Brocade physical network ports managed by the OpenStack ML2 plugin, including VLAN assignments and administrative states.

恢复表名: ml2 brocadeports / Brocade ports / Brocade port configuration / ML2 Brocade ports / Physical Brocade ports / Brocade network ports
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_brocadeports.tenant_id | tenant id / tenant identifier / tenant / project / project_id / owner | varchar(255) | schema / ml2_brocadeports |
| ml2_brocadeports.id | id / identifier / port id / port identifier / unique id / primary key | varchar(36) | schema / ml2_brocadeports |
| ml2_brocadeports.network_id | network id / network identifier / network / associated network / network uuid | varchar(36) | schema / ml2_brocadeports |
| ml2_brocadeports.admin_state_up | admin state up / admin state / administrative state / enabled / active state / port status | tinyint(1) | schema / ml2_brocadeports |
| ml2_brocadeports.physical_interface | physical interface / interface / physical port name / hardware interface / port name / switch port | varchar(36) | schema / ml2_brocadeports |
| ml2_brocadeports.vlan_id | vlan id / vlan identifier / vlan / vlan number / vlan tag / virtual lan | varchar(36) | schema / ml2_brocadeports |

## ml2_dvr_port_bindings

Stores binding information for ports associated with Distributed Virtual Routers (DVR) in the ML2 plugin, linking ports to specific compute hosts and routers.

恢复表名: ml2 dvr port bindings / DVR port bindings / Distributed Virtual Router port bindings / ML2 DVR bindings / DVR port binding table / Distributed router port bindings
SQL表别名: b

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_dvr_port_bindings.port_id | port id / port identifier / network port ID / port uuid / bound port ID | varchar(36) | neutron_518 |
| ml2_dvr_port_bindings.host | host / compute host / host name / DVR host / physical host / node name / server host | varchar(255) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.router_id | router id / router identifier / DVR router ID / distributed router ID / network router ID | varchar(36) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.vif_type | vif type / virtual interface type / port driver type / binding driver / VIF driver | varchar(64) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.vif_details | vif details / virtual interface details / port binding details / VIF configuration / interface metadata | varchar(4095) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.vnic_type | vnic type / virtual network interface card type / port VNIC type / network interface type / VNIC category | varchar(64) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.profile | profile / binding profile / port profile / VIF profile / binding configuration profile / interface profile | varchar(4095) | schema / ml2_dvr_port_bindings |
| ml2_dvr_port_bindings.status | status / binding status / port binding status / DVR binding status / state / current status | varchar(16) | schema / ml2_dvr_port_bindings |

## ml2_flat_allocations

Stores the allocation of physical networks to flat network segments in the OpenStack Neutron ML2 plugin.

恢复表名: ml2 flat allocations / flat network allocations / flat network config / openstack flat networks
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_flat_allocations.physical_network | physical network / physical network name / flat network name / network identifier / phys net | varchar(64) | schema / ml2_flat_allocations |

## ml2_geneve_allocations

Tracks the allocation status of Geneve Virtual Network Identifiers (VNIs) for the ML2 plugin to manage tunnel endpoint identifiers.

恢复表名: ml2 geneve allocations / Geneve VNI allocations / Geneve tunnel ID assignments / VNI allocation table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_geneve_allocations.geneve_vni | geneve vni / VNI / Virtual Network Identifier / Tunnel ID / Geneve ID / VNI ID | int | schema / ml2_geneve_allocations |
| ml2_geneve_allocations.allocated | allocated / Allocation status / Is allocated / VNI status / In use / Available / Allocated flag | tinyint(1) | schema / ml2_geneve_allocations |

## ml2_geneve_endpoints

Stores the IP addresses and hostnames of compute nodes or network agents that support the Geneve tunneling protocol for OpenStack Neutron networking.

恢复表名: ml2 geneve endpoints / geneve_endpoints / ml2_geneve_endpoints / geneve endpoint table / openstack geneve endpoints / network geneve endpoints
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_geneve_endpoints.ip_address | ip address / ip / endpoint ip / geneve ip / node ip / host ip | varchar(64) | schema / ml2_geneve_endpoints |
| ml2_geneve_endpoints.host | host / hostname / node name / agent host / server name / compute node / endpoint host | varchar(255) | schema / ml2_geneve_endpoints |

## ml2_gre_allocations

Tracks the allocation status of GRE tunnel IDs for the ML2 plugin in OpenStack Neutron, managing which tunnel identifiers are currently in use or available.

恢复表名: ml2 gre allocations / GRE allocations / GRE tunnel allocations / ML2 GRE allocation table / OpenStack GRE tunnel IDs / GRE tunnel ID pool
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_gre_allocations.gre_id | gre id / gre identifier / GRE tunnel ID / tunnel identifier / tunnel number / tunnel key | int | schema / ml2_gre_allocations |
| ml2_gre_allocations.allocated | allocated / allocation status / is allocated / tunnel status / usage flag / availability | tinyint(1) | schema / ml2_gre_allocations |

## ml2_gre_endpoints

Stores the mapping between GRE tunnel endpoint IP addresses and the physical or virtual hosts they reside on within the ML2 plugin.

恢复表名: ml2 gre endpoints / GRE endpoints / GRE tunnel endpoints / OpenStack GRE endpoints / GRE host mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_gre_endpoints.ip_address | ip address / GRE IP / tunnel IP / endpoint IP / source IP / destination IP | varchar(64) | schema / ml2_gre_endpoints |
| ml2_gre_endpoints.host | host / host name / server name / node name / compute host / physical host / machine name | varchar(255) | schema / ml2_gre_endpoints |

## ml2_network_segments

Stores the physical network segmentation details (type, physical network, and ID) for each OpenStack Neutron network, defining how virtual networks are mapped to physical infrastructure.

恢复表名: ml2 network segments / network segments / ml2 segments / network segment definitions / physical network segments / segmentation details
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_network_segments.id | id / identifier / segment id / segment identifier / unique segment id / primary key | varchar(36) | schema / ml2_network_segments |
| ml2_network_segments.network_id | network id / network identifier / neutron network id / associated network / parent network id / virtual network id | varchar(36) | schema / ml2_network_segments |
| ml2_network_segments.network_type | network type / segment type / encapsulation type / network encapsulation / tunnel type / segmentation type | varchar(32) | schema / ml2_network_segments |
| ml2_network_segments.physical_network | physical network / physical network name / physnet / underlay network / physical interface / network name | varchar(64) | schema / ml2_network_segments |
| ml2_network_segments.segmentation_id | segmentation id / segmentation identifier / segment id / vlan id / tunnel id / vid / tunnel identifier | int | schema / ml2_network_segments |
| ml2_network_segments.is_dynamic | is dynamic / dynamic flag / dynamic segment / static or dynamic | tinyint(1) | schema / ml2_network_segments |
| ml2_network_segments.segment_index | segment index / index / segment order / position | int | schema / ml2_network_segments |

## ml2_nexus_vxlan_allocations

Tracks the allocation status of VXLAN Virtual Network Identifiers (VNIs) for the ML2 Nexus driver.

恢复表名: ml2 nexus vxlan allocations / VXLAN allocations / VXLAN VNI allocation table / VXLAN segment allocations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_nexus_vxlan_allocations.vxlan_vni | vxlan vni / VNI / Virtual Network Identifier / VXLAN ID / Segment ID | int | schema / ml2_nexus_vxlan_allocations |
| ml2_nexus_vxlan_allocations.allocated | allocated / Allocation status / Is allocated / VNI allocated / Allocation flag / Status | tinyint(1) | schema / ml2_nexus_vxlan_allocations |

## ml2_nexus_vxlan_mcast_groups

Stores the mapping between VXLAN multicast groups and their associated VNI (VXLAN Network Identifier) for the ML2 Nexus driver.

恢复表名: ml2 nexus vxlan mcast groups / VXLAN multicast groups / VXLAN mcast group mapping / Multicast group configuration / VXLAN multicast group table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_nexus_vxlan_mcast_groups.id | id / identifier / Primary Key / Record ID / Unique ID | varchar(36) | schema / ml2_nexus_vxlan_mcast_groups |
| ml2_nexus_vxlan_mcast_groups.mcast_group | mcast group / Multicast Group / Multicast Address / Group Address / VXLAN Mcast Group / Multicast IP | varchar(64) | schema / ml2_nexus_vxlan_mcast_groups |
| ml2_nexus_vxlan_mcast_groups.associated_vni | associated vni / VNI / VXLAN Network Identifier / Network ID / VXLAN ID / Tunnel ID | int | schema / ml2_nexus_vxlan_mcast_groups |

## ml2_port_binding_levels

Stores the binding information for OpenStack Neutron ports to specific compute hosts and network drivers, including the binding level and segment details.

恢复表名: ml2 port binding levels / port binding levels / ML2 port bindings / network port binding levels / OVS port bindings / compute node port bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_port_binding_levels.port_id | port id / port identifier / network port id / port uuid / bound port id | varchar(36) | schema / ml2_port_binding_levels |
| ml2_port_binding_levels.host | host / host name / compute node / compute host / node name / physical host / server name | varchar(255) | schema / ml2_port_binding_levels |
| ml2_port_binding_levels.level | level / binding level / binding priority / binding index | int | schema / ml2_port_binding_levels |
| ml2_port_binding_levels.driver | driver / network driver / mechanism driver / OVS driver / binding driver / network agent | varchar(64) | schema / ml2_port_binding_levels |
| ml2_port_binding_levels.segment_id | segment id / segment identifier / network segment id / physical network segment | varchar(36) | schema / ml2_port_binding_levels |

## ml2_port_bindings

Stores the binding information for OpenStack Neutron ports, linking a port to a specific compute host and defining the virtual interface (VIF) and virtual network interface card (VNIC) types used for network connectivity.

恢复表名: ml2 port bindings / port bindings / ML2 bindings / virtual interface bindings / port binding details / network port bindings
SQL表别名: b, b2, mb, mpb, pb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_port_bindings.port_id | port id / port identifier / network port ID / port UUID / bound port ID | varchar(36) | neutron_1004, neutron_116, neutron_119, neutron_131, neutron_135, neutron_138, neutron_154, neutron_160 |
| ml2_port_bindings.host | host / host name / compute host / node name / physical host / server host / binding host | varchar(255) | neutron_1004, neutron_116, neutron_119, neutron_131, neutron_135, neutron_138, neutron_154, neutron_160 |
| ml2_port_bindings.vif_type | vif type / virtual interface type / interface type / VIF driver / network interface type | varchar(64) | neutron_1004, neutron_116, neutron_119, neutron_131, neutron_135, neutron_138, neutron_154, neutron_160 |
| ml2_port_bindings.vnic_type | vnic type / virtual NIC type / network interface card type / VNIC mode / port VNIC type | varchar(64) | neutron_1004, neutron_116, neutron_119, neutron_131, neutron_135, neutron_138, neutron_154, neutron_160 |
| ml2_port_bindings.vif_details | vif details / virtual interface details / binding details / VIF configuration / interface metadata | varchar(4095) | schema / ml2_port_bindings |
| ml2_port_bindings.profile | profile / binding profile / port profile / network profile / binding profile data | varchar(4095) | schema / ml2_port_bindings |

## ml2_ucsm_port_profiles

Maps VLAN IDs to UCSM port profile identifiers and tracks whether the profile was created on the UCS manager.

恢复表名: ml2 ucsm port profiles / UCSM port profiles / port profile mapping / VLAN to profile mapping / ML2 UCSM port profile table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_ucsm_port_profiles.vlan_id | vlan id / vlan identifier / VLAN / Virtual LAN ID / VLAN number / network segment ID | int | schema / ml2_ucsm_port_profiles |
| ml2_ucsm_port_profiles.profile_id | profile id / profile identifier / Port Profile ID / UCSM Profile ID / Port Profile Name / UCSM Port Profile | varchar(64) | schema / ml2_ucsm_port_profiles |
| ml2_ucsm_port_profiles.created_on_ucs | created on ucs / UCS Created Flag / Profile Created on UCS Manager / Auto-created on UCS / UCS Origin Flag | tinyint(1) | schema / ml2_ucsm_port_profiles |

## ml2_vlan_allocations

Tracks the allocation status of specific VLAN IDs on physical networks for OpenStack Neutron ML2 plugin.

恢复表名: ml2 vlan allocations / VLAN allocations / ML2 VLAN allocation table / OpenStack VLAN ID pool / Network VLAN mapping / VLAN ID registry
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_vlan_allocations.physical_network | physical network / physical network name / network segment / phys net / underlay network / physical network identifier | varchar(64) | schema / ml2_vlan_allocations |
| ml2_vlan_allocations.vlan_id | vlan id / vlan identifier / VLAN number / virtual LAN ID / network vlan | int | schema / ml2_vlan_allocations |
| ml2_vlan_allocations.allocated | allocated / allocation status / is allocated / vlan status / availability flag / in use | tinyint(1) | schema / ml2_vlan_allocations |

## ml2_vxlan_allocations

Tracks the allocation status of VXLAN Virtual Network Identifiers (VNIs) for the ML2 plugin to manage overlay network tunnel IDs.

恢复表名: ml2 vxlan allocations / VXLAN allocations / VXLAN VNI allocation table / ML2 VXLAN allocation records / VXLAN tunnel ID assignments
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_vxlan_allocations.vxlan_vni | vxlan vni / VNI / Virtual Network Identifier / Tunnel ID / VXLAN ID / Overlay ID | int | schema / ml2_vxlan_allocations |
| ml2_vxlan_allocations.allocated | allocated / Allocation status / Is allocated / VNI allocated / Assignment status / In use / Available | tinyint(1) | schema / ml2_vxlan_allocations |

## ml2_vxlan_endpoints

Stores the mapping of VXLAN tunnel endpoints, linking IP addresses and UDP ports to specific hosts for OpenStack Neutron's ML2 VXLAN mechanism driver.

恢复表名: ml2 vxlan endpoints / VXLAN endpoints / VXLAN endpoint table / VXLAN tunnel endpoints / Overlay network endpoints
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ml2_vxlan_endpoints.ip_address | ip address / VXLAN IP / Endpoint IP / Tunnel IP / Host IP / Overlay IP | varchar(64) | schema / ml2_vxlan_endpoints |
| ml2_vxlan_endpoints.udp_port | udp port / VXLAN port / Tunnel port / Endpoint port / Overlay port / VXLAN UDP port | int | schema / ml2_vxlan_endpoints |
| ml2_vxlan_endpoints.host | host / Hostname / Compute node / Endpoint host / VXLAN host / Server name | varchar(255) | schema / ml2_vxlan_endpoints |

## multi_provider_networks

Stores metadata and identifiers for network resources managed across multiple cloud providers.

恢复表名: multi provider networks / networks / provider networks / network registry
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| multi_provider_networks.network_id | network id / network identifier / id / network uuid / network key | varchar(36) | schema / multi_provider_networks |

## networkconnections

Maps network ports to specific networks and network gateways, defining the segmentation type and ID for each connection.

恢复表名: networkconnections / network connections / network connection / port network mappings / port network bindings / network port associations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkconnections.tenant_id | tenant id / tenant identifier / project id / owner id / project identifier | varchar(255) | schema / networkconnections |
| networkconnections.network_gateway_id | network gateway id / network gateway identifier / gateway id / gateway identifier / router gateway id | varchar(36) | schema / networkconnections |
| networkconnections.network_id | network id / network identifier / net id / network uuid | varchar(36) | schema / networkconnections |
| networkconnections.segmentation_type | segmentation type / segment type / network segmentation / vlan type / flat type | enum('flat','vlan') | schema / networkconnections |
| networkconnections.segmentation_id | segmentation id / segmentation identifier / segment id / vlan id / segment identifier | int | schema / networkconnections |
| networkconnections.port_id | port id / port identifier / port uuid / network port id | varchar(36) | schema / networkconnections |

## networkdhcpagentbindings

Maps OpenStack networks to the DHCP agents responsible for providing DHCP services to them.

恢复表名: networkdhcpagentbindings / network dhcp agent bindings / dhcp agent network bindings / network to dhcp agent mapping / dhcp agent assignments / network dhcp bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkdhcpagentbindings.network_id | network id / network identifier / network uuid / bound network / network | varchar(36) | schema / networkdhcpagentbindings |
| networkdhcpagentbindings.dhcp_agent_id | dhcp agent id / dhcp agent identifier / dhcp agent uuid / agent identifier / dhcp agent / assigned agent | varchar(36) | schema / networkdhcpagentbindings |

## networkdnsdomains

Stores the DNS domain names associated with specific networks in the Neutron networking service.

恢复表名: networkdnsdomains / network DNS domains / DNS domains / network dns / dns domain table / network dns configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkdnsdomains.network_id | network id / network identifier / net id / associated network / network uuid | varchar(36) | schema / networkdnsdomains |
| networkdnsdomains.dns_domain | dns domain / domain name / dns name / domain / dns zone | varchar(255) | schema / networkdnsdomains |

## networkgatewaydevicereferences

Maps network gateways to their associated device interfaces, linking gateway identifiers to specific interface names.

恢复表名: networkgatewaydevicereferences / network gateway device references / network gateway interfaces / gateway device mappings / network gateway device links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkgatewaydevicereferences.id | id / identifier / reference id / record id / primary key / unique identifier | varchar(36) | schema / networkgatewaydevicereferences |
| networkgatewaydevicereferences.network_gateway_id | network gateway id / network gateway identifier / gateway id / gateway reference / parent gateway id | varchar(36) | schema / networkgatewaydevicereferences |
| networkgatewaydevicereferences.interface_name | interface name / interface / device interface / port name / network interface name | varchar(64) | schema / networkgatewaydevicereferences |

## networkgatewaydevices

Stores metadata and configuration details for network gateway devices managed by the Neutron service, including their connection status and network identifiers.

恢复表名: networkgatewaydevices / network gateway devices / gateway devices / network gateways / gateway device table / neutron network gateway devices
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkgatewaydevices.tenant_id | tenant id / tenant identifier / project id / owner id / customer id / account id | varchar(255) | schema / networkgatewaydevices |
| networkgatewaydevices.id | id / identifier / device id / gateway id / primary key / unique identifier / resource id | varchar(36) | schema / networkgatewaydevices |
| networkgatewaydevices.nsx_id | nsx id / nsx identifier / nsx uuid / external nsx id / nsx resource id / vmware nsx id | varchar(36) | schema / networkgatewaydevices |
| networkgatewaydevices.name | name / device name / gateway name / display name / label / title | varchar(255) | schema / networkgatewaydevices |
| networkgatewaydevices.connector_type | connector type / connection type / link type / interface type / connector kind / port type | varchar(10) | schema / networkgatewaydevices |
| networkgatewaydevices.connector_ip | connector ip / ip address / connector ip address / device ip / gateway ip / network address | varchar(64) | schema / networkgatewaydevices |
| networkgatewaydevices.status | status / device status / state / operational status / health status / current state | varchar(16) | schema / networkgatewaydevices |

## networkgateways

Stores metadata for network gateways (routers) in the Neutron networking service, including their unique identifiers, names, owning tenants, and default status.

恢复表名: networkgateways / network gateways / router / routers / gateway / gateways / network gateway table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkgateways.id | id / identifier / gateway id / router id / unique identifier / uuid / primary key | varchar(36) | schema / networkgateways |
| networkgateways.name | name / gateway name / router name / display name / label | varchar(255) | schema / networkgateways |
| networkgateways.tenant_id | tenant id / tenant identifier / project id / owner id / user id / account id | varchar(36) | schema / networkgateways |
| networkgateways.default | default / is default / default flag / default status / primary gateway | tinyint(1) | schema / networkgateways |

## networkqueuemappings

Maps network identifiers to queue identifiers, likely for traffic shaping or QoS configuration in a neutron-like networking context.

恢复表名: networkqueuemappings / network queue mappings / network queue map / queue network associations / network to queue links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkqueuemappings.network_id | network id / network identifier / net id / network uuid / associated network | varchar(36) | schema / networkqueuemappings |
| networkqueuemappings.queue_id | queue id / queue identifier / q id / queue uuid / associated queue | varchar(36) | schema / networkqueuemappings |

## networkrbacs

Stores Role-Based Access Control (RBAC) rules that define how networks are shared or accessed by other tenants, specifying the action type and target tenant.

恢复表名: networkrbacs / network RBACs / network access control rules / network sharing rules / RBAC policies / network permissions
SQL表别名: n, n2, nr, r, r2, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networkrbacs.id | id / identifier / RBAC ID / rule ID / policy ID / access rule identifier | varchar(36) | neutron_134, neutron_215, neutron_166, neutron_229, neutron_243, neutron_36, neutron_389, neutron_468 |
| networkrbacs.object_id | object id / object identifier / network ID / subnet ID / resource ID / target resource ID / associated network ID | varchar(36) | neutron_134, neutron_215, neutron_166, neutron_209, neutron_229, neutron_243, neutron_36, neutron_389 |
| networkrbacs.tenant_id | tenant id / tenant identifier / owner tenant ID / project ID / source tenant ID | varchar(255) | neutron_134, neutron_215, neutron_209 |
| networkrbacs.target_tenant | target tenant / shared to tenant / destination tenant ID / target project ID / accessing tenant ID | varchar(255) | neutron_134, neutron_215, neutron_166, neutron_209, neutron_229, neutron_243, neutron_36, neutron_389 |
| networkrbacs.action | action / RBAC action / access type / permission action / sharing action | varchar(255) | neutron_134, neutron_215, neutron_166, neutron_209, neutron_229, neutron_243, neutron_36, neutron_389 |

## networks

Stores metadata for OpenStack Neutron virtual networks, including ownership, status, MTU, and administrative state.

恢复表名: networks / network / neutron_networks / virtual_networks / networks_table / network_definitions
SQL表别名: n, n2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networks.tenant_id | tenant id / tenant identifier / project_id / owner_id / tenant / project / account_id / customer_id | varchar(255) | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.id | id / identifier / network_id / uuid / network_uuid / primary_key / net_id | varchar(36) | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.name | name / network_name / label / title / display_name / net_name | varchar(255) | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.status | status / state / network_status / operational_status / lifecycle_state / active_flag | varchar(16) | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.admin_state_up | admin state up / admin_up / administrative_state / enabled / is_up / admin_enabled / state_up | tinyint(1) | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.mtu | mtu / max_transmission_unit / frame_size / packet_size / mtu_size / max_frame_length | int | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.vlan_transparent | vlan transparent / transparent_vlan / vlan_passthrough / is_transparent / vlan_mode / transparent_flag | tinyint(1) | schema / networks |
| networks.standard_attr_id | standard attr id / standard attr identifier / standard_attribute_id / attr_id / standard_id / metadata_id / common_attr_id | bigint | neutron_1002, neutron_1004, neutron_108, neutron_110, neutron_132, neutron_141, neutron_160, neutron_162 |
| networks.availability_zone_hints | availability zone hints / az_hints / availability_zones / zone_hints / az_list / placement_hints | varchar(255) | schema / networks |

## networksecuritybindings

Stores security binding configurations for networks, specifically indicating whether port security is enabled for each network.

恢复表名: networksecuritybindings / network security bindings / security bindings / port security settings / network security group bindings
SQL表别名: b, nsb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networksecuritybindings.network_id | network id / network identifier / network uuid / associated network / parent network id | varchar(36) | neutron_169, neutron_222, neutron_230, neutron_263, neutron_313, neutron_342, neutron_394, neutron_451 |
| networksecuritybindings.port_security_enabled | port security enabled / port security flag / security group binding order / port security status / is port security on | tinyint(1) | neutron_169, neutron_222, neutron_230, neutron_263, neutron_313, neutron_342, neutron_394, neutron_451 |

## neutron_nsx_network_mappings

Maps Neutron network identifiers to their corresponding NSX network identifiers for cross-platform network resource resolution.

恢复表名: neutron nsx network mappings / network mapping table / neutron to nsx network map / network id mapping / nsx network mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| neutron_nsx_network_mappings.neutron_id | neutron id / neutron identifier / neutron network id / openstack network id / neutron uuid / network id in neutron | varchar(36) | schema / neutron_nsx_network_mappings |
| neutron_nsx_network_mappings.nsx_id | nsx id / nsx identifier / nsx network id / vmware nsx network id / nsx uuid / network id in nsx | varchar(36) | schema / neutron_nsx_network_mappings |

## neutron_nsx_port_mappings

Maps Neutron port identifiers to their corresponding NSX logical switch and port identifiers for network integration.

恢复表名: neutron nsx port mappings / nsx port mapping / neutron to nsx port map / port mapping table / neutron nsx port association
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| neutron_nsx_port_mappings.neutron_id | neutron id / neutron identifier / neutron port id / neutron port uuid / openstack port id / neutron port identifier / port id | varchar(36) | schema / neutron_nsx_port_mappings |
| neutron_nsx_port_mappings.nsx_switch_id | nsx switch id / nsx switch identifier / nsx logical switch id / nsx switch uuid / nsx network id / nsx segment id / logical switch identifier | varchar(36) | schema / neutron_nsx_port_mappings |
| neutron_nsx_port_mappings.nsx_port_id | nsx port id / nsx port identifier / nsx port uuid / nsx endpoint id / nsx port reference | varchar(36) | schema / neutron_nsx_port_mappings |

## neutron_nsx_router_mappings

Maps Neutron router identifiers to their corresponding NSX router identifiers for cross-platform resource correlation.

恢复表名: neutron nsx router mappings / router mapping table / neutron to nsx router map / router id mapping / nsx router mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| neutron_nsx_router_mappings.neutron_id | neutron id / neutron identifier / neutron router id / router id in neutron / openstack router id / neutron uuid | varchar(36) | schema / neutron_nsx_router_mappings |
| neutron_nsx_router_mappings.nsx_id | nsx id / nsx identifier / nsx router id / router id in nsx / vmware nsx router id / nsx uuid | varchar(36) | schema / neutron_nsx_router_mappings |

## neutron_nsx_security_group_mappings

Maps Neutron security group identifiers to their corresponding NSX security group identifiers.

恢复表名: neutron nsx security group mappings / security group mapping / nsx security group map / neutron to nsx sg mapping / security group id mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| neutron_nsx_security_group_mappings.neutron_id | neutron id / neutron identifier / neutron security group id / neutron sg id / openstack security group id / neutron uuid | varchar(36) | schema / neutron_nsx_security_group_mappings |
| neutron_nsx_security_group_mappings.nsx_id | nsx id / nsx identifier / nsx security group id / nsx sg id / vmware nsx group id / nsx uuid | varchar(36) | schema / neutron_nsx_security_group_mappings |

## nexthops

Stores the mapping between routing rules and their corresponding next hop destinations for packet forwarding.

恢复表名: nexthops / next hops / routing nexthops / forwarding destinations / next hop table / route targets
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nexthops.rule_id | rule id / rule identifier / routing rule id / rule number / policy rule id / rule key | int | schema / nexthops |
| nexthops.nexthop | nexthop / next hop address / forwarding destination / gateway ip / next hop ip / route target / outbound interface address | varchar(64) | schema / nexthops |

## nsxv_edge_dhcp_static_bindings

Stores static DHCP bindings (reservations) on NSX-V Edge nodes, mapping specific MAC addresses to reserved IP configurations.

恢复表名: nsxv edge dhcp static bindings / NSX-V Edge DHCP Static Bindings / NSX-V DHCP Static Bindings / Edge DHCP Static Bindings / NSX-V DHCP Reservations / NSX-V Edge DHCP Reservations / DHCP Static Bindings / NSX-V DHCP Static IP Bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_edge_dhcp_static_bindings.edge_id | edge id / edge identifier / NSX-V Edge ID / Edge Node ID / NSX Edge ID / Edge UUID | varchar(36) | schema / nsxv_edge_dhcp_static_bindings |
| nsxv_edge_dhcp_static_bindings.mac_address | mac address / Media Access Control Address / Physical Address / Hardware Address / Client MAC / Device MAC | varchar(32) | schema / nsxv_edge_dhcp_static_bindings |
| nsxv_edge_dhcp_static_bindings.binding_id | binding id / binding identifier / DHCP Binding ID / Reservation ID / Static Binding Identifier / Binding UUID / DHCP Reservation Identifier | varchar(36) | schema / nsxv_edge_dhcp_static_bindings |

## nsxv_edge_monitor_mappings

Maps NSX-V edge instances to their specific monitoring configurations or monitor IDs, linking edge identifiers with monitor identifiers for observability and status tracking.

恢复表名: nsxv edge monitor mappings / NSX-V Edge Monitor Mappings / Edge Monitor Mapping / NSX Edge Monitoring Configuration / Edge Monitor Association / NSX-V Edge Monitor Links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_edge_monitor_mappings.monitor_id | monitor id / monitor identifier / Monitoring ID / Global Monitor ID / Monitor UUID | varchar(36) | schema / nsxv_edge_monitor_mappings |
| nsxv_edge_monitor_mappings.edge_id | edge id / edge identifier / NSX Edge ID / Edge UUID / NSX-V Edge ID | varchar(36) | schema / nsxv_edge_monitor_mappings |
| nsxv_edge_monitor_mappings.edge_monitor_id | edge monitor id / edge monitor identifier / Local Monitor ID / Edge-Specific Monitor ID / Monitor Instance ID | varchar(36) | schema / nsxv_edge_monitor_mappings |

## nsxv_edge_pool_mappings

Maps NSX-V edge instances to their associated edge pools, establishing the relationship between specific edge nodes and the logical pools they belong to.

恢复表名: nsxv edge pool mappings / NSX-V Edge Pool Mappings / Edge Pool Mapping / NSX Edge Pool Association / Edge to Pool Mapping / NSX-V Edge Pool Link
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_edge_pool_mappings.pool_id | pool id / pool identifier / Edge Pool Identifier / Pool UUID / Logical Pool ID / NSX Pool ID | varchar(36) | schema / nsxv_edge_pool_mappings |
| nsxv_edge_pool_mappings.edge_id | edge id / edge identifier / Edge UUID / NSX Edge ID / Edge Node ID | varchar(36) | schema / nsxv_edge_pool_mappings |
| nsxv_edge_pool_mappings.edge_pool_id | edge pool id / edge pool identifier / Mapping ID / Association ID / Link ID | varchar(36) | schema / nsxv_edge_pool_mappings |

## nsxv_edge_vip_mappings

Stores the mapping relationships between NSX-V Edge virtual IP (VIP) pools and associated Edge services such as application profiles, virtual server entities, and firewall rules.

恢复表名: nsxv edge vip mappings / NSX-V Edge VIP Mappings / Edge VIP Mapping Table / NSX Edge Virtual IP Mappings / Edge Load Balancer VIP Config / NSX-V VIP to Edge Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_edge_vip_mappings.pool_id | pool id / pool identifier / VIP Pool ID / Load Balancer Pool ID / NSX Pool ID / Virtual IP Pool ID | varchar(36) | schema / nsxv_edge_vip_mappings |
| nsxv_edge_vip_mappings.edge_id | edge id / edge identifier / NSX Edge ID / Load Balancer Edge ID / NSX-V Edge Identifier | varchar(36) | schema / nsxv_edge_vip_mappings |
| nsxv_edge_vip_mappings.edge_app_profile_id | edge app profile id / edge app profile identifier / Application Profile ID / App Profile Identifier / NSX App Profile ID / Load Balancer App Profile ID | varchar(36) | schema / nsxv_edge_vip_mappings |
| nsxv_edge_vip_mappings.edge_vse_id | edge vse id / edge vse identifier / Virtual Server Entity ID / VSE Identifier / NSX VSE ID / Edge Virtual Server ID | varchar(36) | schema / nsxv_edge_vip_mappings |
| nsxv_edge_vip_mappings.edge_fw_rule_id | edge fw rule id / edge fw rule identifier / Edge Firewall Rule ID / Firewall Rule ID / FW Rule Identifier / NSX Firewall Rule ID / Edge Security Rule ID | varchar(36) | schema / nsxv_edge_vip_mappings |

## nsxv_edge_vnic_bindings

Stores the binding relationships between NSX-V Edge nodes, their virtual network interface cards (VNICs), tunnel indices, and associated logical networks.

恢复表名: nsxv edge vnic bindings / NSX-V Edge VNIC Bindings / Edge VNIC Binding Table / NSX Edge Network Interface Bindings / Edge Tunnel Bindings / NSX-V Edge Interface Configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_edge_vnic_bindings.edge_id | edge id / edge identifier / Edge Node ID / NSX Edge ID / Edge UUID | varchar(36) | schema / nsxv_edge_vnic_bindings |
| nsxv_edge_vnic_bindings.vnic_index | vnic index / Virtual NIC Index / Interface Index / VNIC Number / Network Interface Index | int | schema / nsxv_edge_vnic_bindings |
| nsxv_edge_vnic_bindings.tunnel_index | tunnel index / Tunnel ID / VXLAN Tunnel Index / Overlay Tunnel Index / Tunnel Number | int | schema / nsxv_edge_vnic_bindings |
| nsxv_edge_vnic_bindings.network_id | network id / network identifier / Logical Network ID / NSX Network ID / Segment ID | varchar(36) | schema / nsxv_edge_vnic_bindings |

## nsxv_firewall_rule_bindings

Maps NSX-V firewall rules to specific NSX edges and virtual switch endpoints, defining where firewall policies are applied within the NSX-V infrastructure.

恢复表名: nsxv firewall rule bindings / NSX-V Firewall Rule Bindings / Firewall Rule Edge Bindings / NSX Firewall Rule Associations / Edge Firewall Rule Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_firewall_rule_bindings.rule_id | rule id / rule identifier / Firewall Rule ID / NSX Rule ID / Firewall Policy ID / Rule UUID | varchar(36) | schema / nsxv_firewall_rule_bindings |
| nsxv_firewall_rule_bindings.edge_id | edge id / edge identifier / NSX Edge Identifier / Edge Node ID / Firewall Edge ID / NSX Edge UUID | varchar(36) | schema / nsxv_firewall_rule_bindings |
| nsxv_firewall_rule_bindings.rule_vse_id | rule vse id / rule vse identifier / Virtual Switch Endpoint ID / VSE Identifier / Rule Virtual Switch ID / Endpoint ID | varchar(36) | schema / nsxv_firewall_rule_bindings |

## nsxv_internal_edges

Stores configuration details for internal NSX-V edge nodes, specifically identifying edges that serve inter-edge network purposes.

恢复表名: nsxv internal edges / NSX-V internal edges / internal edge list / NSX internal edge configuration / internal edge network / NSX-V edge interconnects
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_internal_edges.ext_ip_address | ext ip address / external IP / external IP address / edge IP / edge external address / public IP / external address | varchar(64) | schema / nsxv_internal_edges |
| nsxv_internal_edges.router_id | router id / router identifier / BGP router ID / edge router identifier / BGP ID / edge router ID | varchar(36) | schema / nsxv_internal_edges |
| nsxv_internal_edges.purpose | purpose / edge purpose / function / role / inter-edge network / edge type / usage | enum('inter_edge_net') | schema / nsxv_internal_edges |

## nsxv_internal_networks

Stores the mapping between NSX-V internal network purposes and their corresponding network identifiers.

恢复表名: nsxv internal networks / NSX-V internal networks / NSX internal network configuration / NSX-V network purpose mapping / NSX internal network IDs
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_internal_networks.network_purpose | network purpose / purpose / internal network purpose / NSX network purpose / inter edge net purpose | enum('inter_edge_net') | schema / nsxv_internal_networks |
| nsxv_internal_networks.network_id | network id / network identifier / NSX network ID / internal network ID / network uuid | varchar(36) | schema / nsxv_internal_networks |

## nsxv_port_index_mappings

Maps NSX-V port identifiers to their corresponding device IDs and index positions, likely used for tracking port ordering or association with specific devices in the NSX-V environment.

恢复表名: nsxv port index mappings / NSX-V Port Index Mappings / NSXV Port Index Map / Port Index Mapping Table / NSX-V Port to Index Mapping / Port Index Reference
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_port_index_mappings.port_id | port id / port identifier / NSX-V Port ID / Port UUID / Port Key | varchar(36) | schema / nsxv_port_index_mappings |
| nsxv_port_index_mappings.device_id | device id / device identifier / Host ID / VM ID / Associated Device / Device Key | varchar(255) | schema / nsxv_port_index_mappings |
| nsxv_port_index_mappings.index | index / Port Index / Position / Order / Sequence Number / Index Number | int | schema / nsxv_port_index_mappings |

## nsxv_port_vnic_mappings

Maps Neutron port identifiers to their corresponding NSX-V VNIC identifiers to maintain synchronization between the Neutron and NSX-V networking layers.

恢复表名: nsxv port vnic mappings / NSX-V Port VNIC Mappings / NSXV Port VNIC Mapping / Port VNIC Mapping / NSX Port to VNIC Map / Neutron NSXV Port VNIC Association
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_port_vnic_mappings.neutron_id | neutron id / neutron identifier / Neutron Port ID / Neutron Port UUID / Port ID / Neutron Port | varchar(36) | schema / nsxv_port_vnic_mappings |
| nsxv_port_vnic_mappings.nsx_id | nsx id / nsx identifier / NSX-V ID / NSX VNIC ID / NSX VNIC Identifier / NSX Port ID | varchar(42) | schema / nsxv_port_vnic_mappings |

## nsxv_router_bindings

Stores the binding relationships between NSX-V logical routers and their underlying physical or virtual edge appliances, including appliance sizing and type.

恢复表名: nsxv router bindings / NSX-V Router Bindings / Router Edge Bindings / NSX Router Appliance Mapping / Logical Router Bindings / NSXV Router Configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_router_bindings.status | status / Router Status / Binding Status / State / Operational Status / Router State | varchar(16) | schema / nsxv_router_bindings |
| nsxv_router_bindings.status_description | status description / Status Details / Error Message / Binding Description / State Description / Router Status Info | varchar(255) | schema / nsxv_router_bindings |
| nsxv_router_bindings.router_id | router id / router identifier / Logical Router ID / LR ID / NSX Router ID / Router UUID | varchar(36) | schema / nsxv_router_bindings |
| nsxv_router_bindings.edge_id | edge id / edge identifier / Edge Appliance ID / ESXi Edge ID / Physical Edge ID / Edge UUID | varchar(36) | schema / nsxv_router_bindings |
| nsxv_router_bindings.lswitch_id | lswitch id / lswitch identifier / Logical Switch ID / VDS ID / Distributed Switch ID / Network Switch ID | varchar(36) | schema / nsxv_router_bindings |
| nsxv_router_bindings.appliance_size | appliance size / Router Size / Edge Size / Sizing / Router Capacity | enum('compact','large','xlarge','quadlarge') | schema / nsxv_router_bindings |
| nsxv_router_bindings.edge_type | edge type / Edge Appliance Type / Router Type / Service Type / VDR Type / Edge Classification | enum('service','vdr') | schema / nsxv_router_bindings |

## nsxv_router_ext_attributes

Stores extended configuration attributes and properties for NSX-V logical routers, including distribution mode, router type, and service status.

恢复表名: nsxv router ext attributes / NSX-V Router Extended Attributes / Router Attributes / NSX Router Config / Virtual Router Properties / NSXV Router Metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_router_ext_attributes.router_id | router id / router identifier / Logical Router ID / NSX Router ID / Router UUID | varchar(36) | schema / nsxv_router_ext_attributes |
| nsxv_router_ext_attributes.distributed | distributed / Distributed Mode / Is Distributed / Distributed Router / DR Mode / Distributed Enabled | tinyint(1) | schema / nsxv_router_ext_attributes |
| nsxv_router_ext_attributes.router_type | router type / Shared or Exclusive / Router Category / NSX Router Type / Type of Router | enum('shared','exclusive') | schema / nsxv_router_ext_attributes |
| nsxv_router_ext_attributes.service_router | service router / Is Service Router / Service Enabled / SR Status / Service Router Flag | tinyint(1) | schema / nsxv_router_ext_attributes |

## nsxv_rule_mappings

Maps Neutron security group rules to their corresponding NSX-V firewall rules, maintaining the relationship between OpenStack Neutron and VMware NSX-V security configurations.

恢复表名: nsxv rule mappings / NSX-V rule mappings / NSX rule mapping table / Neutron NSX rule map / NSXV firewall rule mapping / NSX security rule mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_rule_mappings.neutron_id | neutron id / neutron identifier / Neutron rule ID / Neutron security group rule ID / OpenStack rule ID / Neutron firewall rule ID / Source rule ID | varchar(36) | schema / nsxv_rule_mappings |
| nsxv_rule_mappings.nsx_rule_id | nsx rule id / nsx rule identifier / NSX-V rule ID / NSX firewall rule ID / VMware NSX rule identifier / Target rule ID | varchar(36) | schema / nsxv_rule_mappings |

## nsxv_security_group_section_mappings

Maps Neutron security group rules to NSX-V IP sections, linking network security policies to specific IP address ranges or sections in the NSX-V environment.

恢复表名: nsxv security group section mappings / NSX-V Security Group Section Mappings / Security Group IP Section Mapping / NSXV SG Section Map / Security Group Rule Section Links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_security_group_section_mappings.neutron_id | neutron id / neutron identifier / Security Group Rule ID / Neutron Rule Identifier / SG Rule ID / Neutron Security Group ID | varchar(36) | schema / nsxv_security_group_section_mappings |
| nsxv_security_group_section_mappings.ip_section_id | ip section id / ip section identifier / NSX-V IP Section Identifier / IP Range Section ID / NSXV Section ID / IP Address Section ID | varchar(100) | schema / nsxv_security_group_section_mappings |

## nsxv_spoofguard_policy_network_mappings

Maps NSX-V networks to their associated SpoofGuard policies, defining which security policy applies to which network segment.

恢复表名: nsxv spoofguard policy network mappings / NSX-V SpoofGuard Policy Network Mappings / SpoofGuard Policy Network Mapping / NSX SpoofGuard Network Policy Association / Network SpoofGuard Policy Links
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_spoofguard_policy_network_mappings.network_id | network id / network identifier / NSX Network ID / Logical Network ID / Network UUID | varchar(36) | schema / nsxv_spoofguard_policy_network_mappings |
| nsxv_spoofguard_policy_network_mappings.policy_id | policy id / policy identifier / SpoofGuard Policy ID / Security Policy ID / SpoofGuard Policy UUID | varchar(36) | schema / nsxv_spoofguard_policy_network_mappings |

## nsxv_tz_network_bindings

Stores the mapping between logical NSX-V networks and physical network resources (VLANs, port groups, or flat networks) within a tenant zone.

恢复表名: nsxv tz network bindings / NSX-V tenant zone network bindings / NSX-V network binding configuration / Tenant zone network bindings / NSX-V physical network mappings / NSX-V VLAN and port group bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_tz_network_bindings.network_id | network id / network identifier / logical network ID / NSX network identifier / network UUID / logical network UUID / NSX-V network ID | varchar(36) | schema / nsxv_tz_network_bindings |
| nsxv_tz_network_bindings.binding_type | binding type / network binding type / binding mode / physical network type / connection type / binding category | enum('flat','vlan','portgroup') | schema / nsxv_tz_network_bindings |
| nsxv_tz_network_bindings.phy_uuid | phy uuid / physical network UUID / physical resource ID / port group UUID / physical network identifier / underlay network ID | varchar(36) | schema / nsxv_tz_network_bindings |
| nsxv_tz_network_bindings.vlan_id | vlan id / vlan identifier / VLAN number / virtual LAN ID / VLAN tag / physical VLAN identifier | int | schema / nsxv_tz_network_bindings |

## nsxv_vdr_dhcp_bindings

Stores the binding relationships between NSX-V Virtual Distributed Routers (VDR) and their associated DHCP services, linking the VDR router instance to the specific DHCP router and edge node responsible for DHCP operations.

恢复表名: nsxv vdr dhcp bindings / NSX-V VDR DHCP Bindings / VDR DHCP Binding Table / NSX-V Distributed Router DHCP Bindings / VDR DHCP Lease Bindings / NSX-V VDR DHCP Configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nsxv_vdr_dhcp_bindings.vdr_router_id | vdr router id / vdr router identifier / Virtual Distributed Router ID / NSX-V VDR ID / Distributed Router Identifier / VDR Instance ID | varchar(36) | schema / nsxv_vdr_dhcp_bindings |
| nsxv_vdr_dhcp_bindings.dhcp_router_id | dhcp router id / dhcp router identifier / DHCP Service Router ID / DHCP Edge Router ID / DHCP Provider ID / DHCP Service Identifier | varchar(36) | schema / nsxv_vdr_dhcp_bindings |
| nsxv_vdr_dhcp_bindings.dhcp_edge_id | dhcp edge id / dhcp edge identifier / DHCP Edge Node ID / DHCP Service Edge ID / DHCP Edge Instance ID | varchar(36) | schema / nsxv_vdr_dhcp_bindings |

## nuage_net_partition_router_mapping

Maps Nuage network partitions (VRFs) to physical or virtual routers, storing the specific Route Distinguisher (RD) and Route Target (RT) configurations used for routing isolation and policy application.

恢复表名: nuage net partition router mapping / Nuage Network Partition Router Mapping / Network Partition Router Association / Nuage Router Partition Link / VRF Router Mapping / Nuage VRF Router Table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nuage_net_partition_router_mapping.net_partition_id | net partition id / net partition identifier / Network Partition ID / VRF ID / Partition Identifier / Nuage Partition ID / VRF Identifier | varchar(36) | schema / nuage_net_partition_router_mapping |
| nuage_net_partition_router_mapping.router_id | router id / router identifier / Physical Router ID / Virtual Router ID / Device Router ID | varchar(36) | schema / nuage_net_partition_router_mapping |
| nuage_net_partition_router_mapping.nuage_router_id | nuage router id / nuage router identifier / Nuage Device ID / Nuage System Router ID / Nuage Router UUID | varchar(36) | schema / nuage_net_partition_router_mapping |
| nuage_net_partition_router_mapping.nuage_rtr_rd | nuage rtr rd / Route Distinguisher / RD / Router Route Distinguisher / Nuage RD / VRF Route Distinguisher | varchar(36) | schema / nuage_net_partition_router_mapping |
| nuage_net_partition_router_mapping.nuage_rtr_rt | nuage rtr rt / Route Target / RT / Router Route Target / Nuage RT / VRF Route Target | varchar(36) | schema / nuage_net_partition_router_mapping |

## nuage_net_partitions

Stores definitions of network partitions in the Nuage VSD, including their names, associated Layer 2 and Layer 3 domain templates, and zone isolation settings.

恢复表名: nuage net partitions / Nuage Network Partitions / Network Partitions / Nuage Partitions / Network Segments / Nuage Network Segments
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nuage_net_partitions.id | id / identifier / Partition ID / Network Partition ID / Nuage Partition ID / Partition Identifier / Unique Partition ID | varchar(36) | schema / nuage_net_partitions |
| nuage_net_partitions.name | name / Partition Name / Network Partition Name / Nuage Partition Name / Partition Label / Segment Name | varchar(64) | schema / nuage_net_partitions |
| nuage_net_partitions.l3dom_tmplt_id | l3dom tmplt id / l3dom tmplt identifier / L3 Domain Template ID / Layer 3 Domain Template ID / L3 Template ID / Layer 3 Template Identifier / L3 Domain ID | varchar(36) | schema / nuage_net_partitions |
| nuage_net_partitions.l2dom_tmplt_id | l2dom tmplt id / l2dom tmplt identifier / L2 Domain Template ID / Layer 2 Domain Template ID / L2 Template ID / Layer 2 Template Identifier / L2 Domain ID | varchar(36) | schema / nuage_net_partitions |
| nuage_net_partitions.isolated_zone | isolated zone / Isolation Zone / Isolated Zone Name / Isolation Zone Name / Isolated Zone ID | varchar(64) | schema / nuage_net_partitions |
| nuage_net_partitions.shared_zone | shared zone / Sharing Zone / Shared Zone Name / Sharing Zone Name / Shared Zone ID | varchar(64) | schema / nuage_net_partitions |

## nuage_provider_net_bindings

Maps logical network identifiers to physical network configurations and VLAN IDs for the Nuage provider.

恢复表名: nuage provider net bindings / Nuage provider network bindings / Nuage network bindings / Provider network bindings / Nuage VLAN bindings / Nuage physical network mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nuage_provider_net_bindings.network_id | network id / network identifier / logical network id / nuage network id / provider network id | varchar(36) | schema / nuage_provider_net_bindings |
| nuage_provider_net_bindings.network_type | network type / type of network / network category / provider network type / nuage network type | varchar(32) | schema / nuage_provider_net_bindings |
| nuage_provider_net_bindings.physical_network | physical network / physical network name / underlay network / physical network identifier / nuage physical network | varchar(64) | schema / nuage_provider_net_bindings |
| nuage_provider_net_bindings.vlan_id | vlan id / vlan identifier / vlan number / virtual lan id / nuage vlan | int | schema / nuage_provider_net_bindings |

## nuage_subnet_l2dom_mapping

Maps Nuage subnets to Layer 2 Domain (L2DOM) templates and network partitions, tracking ownership and management status for network segmentation.

恢复表名: nuage subnet l2dom mapping / Nuage Subnet L2 Domain Mapping / Subnet L2DOM Mapping / Nuage L2 Domain Subnet Association / Subnet to L2 Domain Template Mapping / Nuage Network Partition Subnet Mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| nuage_subnet_l2dom_mapping.subnet_id | subnet id / subnet identifier / Local Subnet ID / Subnet UUID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.net_partition_id | net partition id / net partition identifier / Network Partition ID / Partition Identifier / Network Segment ID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.nuage_subnet_id | nuage subnet id / nuage subnet identifier / Remote Subnet ID / Nuage Network Subnet ID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.nuage_l2dom_tmplt_id | nuage l2dom tmplt id / nuage l2dom tmplt identifier / Nuage L2DOM Template ID / L2 Domain Template ID / L2DOM Template Identifier / Layer 2 Domain Template ID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.nuage_user_id | nuage user id / nuage user identifier / User Identifier / Owner User ID / Nuage Account User ID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.nuage_group_id | nuage group id / nuage group identifier / Group Identifier / Organization Group ID / Nuage Tenant Group ID | varchar(36) | schema / nuage_subnet_l2dom_mapping |
| nuage_subnet_l2dom_mapping.nuage_managed_subnet | nuage managed subnet / Managed Subnet Flag / Is Managed Subnet / Subnet Management Status | tinyint(1) | schema / nuage_subnet_l2dom_mapping |

## poolloadbalanceragentbindings

Maps load balancer pools to their associated agents, defining which agents are bound to specific pools for traffic handling.

恢复表名: poolloadbalanceragentbindings / pool load balancer agent bindings / load balancer agent bindings / pool agent bindings / lb agent bindings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| poolloadbalanceragentbindings.pool_id | pool id / pool identifier / load balancer pool id / lb pool id / pool uuid | varchar(36) | schema / poolloadbalanceragentbindings |
| poolloadbalanceragentbindings.agent_id | agent id / agent identifier / load balancer agent id / lb agent id / agent uuid | varchar(36) | schema / poolloadbalanceragentbindings |

## poolmonitorassociations

Stores the many-to-many relationship between monitoring pools and individual monitors, including the association status.

恢复表名: poolmonitorassociations / pool monitor associations / monitor pool links / pool monitor mappings / monitor associations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| poolmonitorassociations.pool_id | pool id / pool identifier / monitoring pool id / pool uuid | varchar(36) | schema / poolmonitorassociations |
| poolmonitorassociations.monitor_id | monitor id / monitor identifier / monitoring id / monitor uuid | varchar(36) | schema / poolmonitorassociations |
| poolmonitorassociations.status | status / association status / link status / state / active status | varchar(16) | schema / poolmonitorassociations |
| poolmonitorassociations.status_description | status description / status details / description / reason / status message | varchar(255) | schema / poolmonitorassociations |

## pools

Stores load balancer pool configurations, including member distribution methods, protocols, and associated network resources in the Neutron service.

恢复表名: pools / load_balancer_pools / lb_pools / pool / load_balancer_pool / neutron_pools
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pools.tenant_id | tenant id / tenant identifier / project_id / project / tenant / owner_id / account_id / user_tenant | varchar(255) | schema / pools |
| pools.id | id / identifier / pool_id / uuid / unique_id / primary_key / resource_id | varchar(36) | schema / pools |
| pools.vip_id | vip id / vip identifier / load_balancer_id / lb_id / virtual_ip_id / parent_lb_id / associated_lb | varchar(36) | schema / pools |
| pools.name | name / pool_name / title / label / display_name | varchar(255) | schema / pools |
| pools.description | description / pool_description / notes / details / remarks | varchar(255) | schema / pools |
| pools.subnet_id | subnet id / subnet identifier / subnet / network_subnet_id / associated_subnet / subnet_uuid | varchar(36) | schema / pools |
| pools.protocol | protocol / lb_protocol / communication_protocol / http_protocol / tcp_protocol / protocol_type | enum('HTTP','HTTPS','TCP') | schema / pools |
| pools.lb_method | lb method / load_balancing_method / distribution_method / algorithm / round_robin / least_connections / source_ip | enum('ROUND_ROBIN','LEAST_CONNECTIONS','SOURCE_IP') | schema / pools |
| pools.status | status / pool_status / state / operational_status / current_state | varchar(16) | schema / pools |
| pools.status_description | status description / status_reason / state_details / status_message / error_message | varchar(255) | schema / pools |
| pools.admin_state_up | admin state up / enabled / is_active / admin_enabled / up_down / availability | tinyint(1) | schema / pools |

## poolstatisticss

Stores performance and usage statistics for connection pools, including data transfer volumes and connection counts.

恢复表名: poolstatisticss / pool statistics / connection pool stats / pool metrics / database pool performance / pool usage statistics
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| poolstatisticss.pool_id | pool id / pool identifier / pool uuid / connection pool id / pool key / pool reference | varchar(36) | schema / poolstatisticss |
| poolstatisticss.bytes_in | bytes in / incoming bytes / data received / input volume / bytes downloaded / inbound traffic / read bytes | bigint | schema / poolstatisticss |
| poolstatisticss.bytes_out | bytes out / outgoing bytes / data sent / output volume / bytes uploaded / outbound traffic / write bytes | bigint | schema / poolstatisticss |
| poolstatisticss.active_connections | active connections / current connections / open connections / live connections / active session count / in-use connections | bigint | schema / poolstatisticss |
| poolstatisticss.total_connections | total connections / cumulative connections / total connection count / historical connections / lifetime connections / all connections | bigint | schema / poolstatisticss |

## portbindingports

Stores the binding information for OpenStack Neutron ports, mapping each port to the compute host where it is currently bound.

恢复表名: portbindingports / port bindings / port binding ports / neutron port bindings / port to host bindings / network port bindings
SQL表别名: pbb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| portbindingports.port_id | port id / port identifier / network port id / port uuid / bound port id | varchar(36) | schema / portbindingports |
| portbindingports.host | host / host name / compute host / bound host / physical host / node name / server host | varchar(255) | schema / portbindingports |

## portdnses

Stores DNS name and domain records associated with network ports, tracking both current and previous DNS configurations for each port.

恢复表名: portdnses / port_dns / port_dns_records / dns_records / port_dns_mappings / dns_entries
SQL表别名: pd

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| portdnses.port_id | port id / port identifier / port uuid / associated port / port reference / port key | varchar(36) | neutron_100, neutron_128, neutron_178, neutron_183, neutron_2, neutron_200, neutron_217, neutron_25 |
| portdnses.current_dns_name | current dns name / current hostname / active dns name / current dns label / present dns name / current fqdn name part | varchar(255) | schema / portdnses |
| portdnses.current_dns_domain | current dns domain / current domain / active dns domain / current dns zone / present domain name / current fqdn domain part | varchar(255) | schema / portdnses |
| portdnses.previous_dns_name | previous dns name / old hostname / last dns name / historical dns name / prior dns label | varchar(255) | schema / portdnses |
| portdnses.previous_dns_domain | previous dns domain / old domain / last dns domain / historical dns zone / prior domain name | varchar(255) | schema / portdnses |

## portqueuemappings

Maps network ports to specific queues, likely for traffic shaping, QoS, or load balancing in a neutron networking context.

恢复表名: portqueuemappings / port queue mappings / port to queue mapping / queue port associations / port queue links / network port queue assignments
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| portqueuemappings.port_id | port id / port identifier / network port id / port uuid / port reference | varchar(36) | schema / portqueuemappings |
| portqueuemappings.queue_id | queue id / queue identifier / traffic queue id / queue uuid / queue reference | varchar(36) | schema / portqueuemappings |

## ports

Stores network port definitions including MAC addresses, network associations, device bindings, and administrative status for OpenStack Neutron.

恢复表名: ports / network ports / port / neutron ports / virtual ports / port records
SQL表别名: p, p2, p3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| ports.tenant_id | tenant id / tenant identifier / project ID / project / tenant / owner project | varchar(255) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.id | id / identifier / port ID / port identifier / port UUID / primary key / port key | varchar(36) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.name | name / port name / label / display name / port label | varchar(255) | neutron_113, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_725 |
| ports.network_id | network id / network identifier / network / subnet network / connected network | varchar(36) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.mac_address | mac address / MAC / hardware address / physical address / port MAC / media access control | varchar(32) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.admin_state_up | admin state up / admin state / administrative state / admin up / enabled / administratively up | tinyint(1) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.status | status / port status / state / operational status / ACTIVE / DOWN | varchar(16) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.device_id | device id / device identifier / instance ID / VM ID / bound device / compute instance | varchar(255) | neutron_175, neutron_680, neutron_692, neutron_704, neutron_707 |
| ports.device_owner | device owner / owner / service owner / compute:nova / service type | varchar(255) | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |
| ports.dns_name | dns name / hostname / domain name / port DNS | varchar(255) | schema / ports |
| ports.standard_attr_id | standard attr id / standard attr identifier / standard attribute ID / attribute ID / standardattributes ID / resource attribute | bigint | neutron_113, neutron_175, neutron_126, neutron_188, neutron_202, neutron_207, neutron_640, neutron_680 |

## portsecuritybindings

Stores port security configuration and status for network ports, indicating whether port security is enabled for each port.

恢复表名: portsecuritybindings / port security bindings / port security / port security configuration / port security settings / port security flags / port security status
SQL表别名: b, psb, psb2, psb3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| portsecuritybindings.port_id | port id / port identifier / port uuid / port reference / network port id / port key | varchar(36) | neutron_1006, neutron_101, neutron_109, neutron_117, neutron_118, neutron_125, neutron_132, neutron_133 |
| portsecuritybindings.port_security_enabled | port security enabled / port security flag / port security status / security enabled / port security active / port security on | tinyint(1) | neutron_1006, neutron_101, neutron_109, neutron_117, neutron_118, neutron_125, neutron_132, neutron_133 |

## providerresourceassociations

Maps network resources (such as load balancers) to their specific service providers (e.g., haproxy) to enable provider-specific filtering and aggregation.

恢复表名: providerresourceassociations / provider resource associations / provider associations / resource provider mapping / provider resource links / lb provider associations
SQL表别名: pra, pra2, pra3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| providerresourceassociations.provider_name | provider name / provider / service provider / provider type / lb provider | varchar(255) | neutron_228, neutron_23, neutron_235, neutron_247, neutron_254, neutron_258, neutron_269, neutron_275 |
| providerresourceassociations.resource_id | resource id / resource identifier / load balancer id / lb id / associated resource | varchar(36) | neutron_228, neutron_23, neutron_235, neutron_247, neutron_254, neutron_258, neutron_269, neutron_275 |

## qos_bandwidth_limit_rules

Stores specific bandwidth limitation rules (maximum throughput and burst rates) associated with Quality of Service (QoS) policies.

恢复表名: qos bandwidth limit rules / bandwidth limit rules / QoS rules / bandwidth limits / traffic shaping rules / QoS policy rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qos_bandwidth_limit_rules.id | id / identifier / rule id / bandwidth rule id / qos rule id / limit rule id / primary key | varchar(36) | schema / qos_bandwidth_limit_rules |
| qos_bandwidth_limit_rules.qos_policy_id | qos policy id / qos policy identifier / policy id / associated policy / parent policy id / qos policy reference | varchar(36) | schema / qos_bandwidth_limit_rules |
| qos_bandwidth_limit_rules.max_kbps | max kbps / maximum kbps / maximum bandwidth / max throughput / bandwidth limit / max rate kbps / sustained bandwidth limit | int | schema / qos_bandwidth_limit_rules |
| qos_bandwidth_limit_rules.max_burst_kbps | max burst kbps / maximum burst kbps / burst bandwidth / max burst rate / burst limit / peak bandwidth / max burst throughput | int | schema / qos_bandwidth_limit_rules |

## qos_network_policy_bindings

Maps OpenStack Neutron networks to their associated Quality of Service (QoS) policies, enabling traffic management and bandwidth control for specific network resources.

恢复表名: qos network policy bindings / network QoS bindings / QoS policy network associations / network quality of service bindings
SQL表别名: qnpb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qos_network_policy_bindings.policy_id | policy id / policy identifier / QoS policy ID / quality of service policy ID / QoS policy reference | varchar(36) | schema / qos_network_policy_bindings |
| qos_network_policy_bindings.network_id | network id / network identifier / Neutron network ID / associated network ID | varchar(36) | neutron_535 |

## qos_policies

Stores definitions for Quality of Service (QoS) policies used to manage network traffic bandwidth and priority.

恢复表名: qos policies / Quality of Service policies / network QoS / traffic shaping policies / bandwidth management policies
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qos_policies.id | id / identifier / policy ID / QoS policy ID / unique identifier / policy identifier | varchar(36) | schema / qos_policies |
| qos_policies.name | name / policy name / QoS name / policy title / service name | varchar(255) | schema / qos_policies |
| qos_policies.description | description / policy description / QoS details / notes / policy summary | varchar(255) | schema / qos_policies |
| qos_policies.tenant_id | tenant id / tenant identifier / project ID / owner ID / customer ID / account ID | varchar(255) | schema / qos_policies |

## qos_port_policy_bindings

Maps network ports to their associated Quality of Service (QoS) port policies, enabling the application of traffic shaping and bandwidth limits to specific ports.

恢复表名: qos port policy bindings / port policy bindings / QoS bindings / port QoS associations / network port QoS policy links
SQL表别名: q, qppb

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qos_port_policy_bindings.policy_id | policy id / policy identifier / QoS policy ID / service policy ID / traffic policy ID / bandwidth policy ID | varchar(36) | schema / qos_port_policy_bindings |
| qos_port_policy_bindings.port_id | port id / port identifier / network port identifier / port UUID / interface ID / port reference | varchar(36) | neutron_559 |

## qospolicyrbacs

Stores Role-Based Access Control (RBAC) rules defining which tenants or users are permitted to perform specific actions on Quality of Service (QoS) policies.

恢复表名: qospolicyrbacs / QoS Policy RBACs / Quality of Service Policy Access Controls / QoS Policy Permissions / QoS Policy Roles / QoS Policy Access Rights
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qospolicyrbacs.id | id / identifier / RBAC ID / Access Control ID / Policy Permission ID / QoS RBAC Identifier | varchar(36) | schema / qospolicyrbacs |
| qospolicyrbacs.tenant_id | tenant id / tenant identifier / Project ID / Owner Tenant / Service Tenant / Admin Tenant | varchar(255) | schema / qospolicyrbacs |
| qospolicyrbacs.target_tenant | target tenant / Authorized Tenant / Subject Tenant / User Tenant / Accessed Tenant | varchar(255) | schema / qospolicyrbacs |
| qospolicyrbacs.action | action / Permission Type / Allowed Operation / Access Level / Verb | varchar(255) | schema / qospolicyrbacs |
| qospolicyrbacs.object_id | object id / object identifier / QoS Policy ID / Resource ID / Policy Identifier / Target Object | varchar(36) | schema / qospolicyrbacs |

## qosqueues

Stores Quality of Service (QoS) queue definitions for network traffic management, including bandwidth limits, priority markings, and tenant associations.

恢复表名: qosqueues / QoS Queues / Quality of Service Queues / Network QoS / Traffic Queues / Bandwidth Queues
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| qosqueues.tenant_id | tenant id / tenant identifier / Project ID / Owner ID / Customer ID / Organization ID | varchar(255) | schema / qosqueues |
| qosqueues.id | id / identifier / Queue ID / Primary Key / Unique Identifier / Queue UUID | varchar(36) | schema / qosqueues |
| qosqueues.name | name / Queue Name / Label / Description / Queue Title | varchar(255) | schema / qosqueues |
| qosqueues.default | default / Is Default / Default Flag / Default Queue / Standard Queue | tinyint(1) | schema / qosqueues |
| qosqueues.min | min / minimum / Minimum Bandwidth / Min Kbps / Guaranteed Bandwidth / Lower Limit | int | schema / qosqueues |
| qosqueues.max | max / maximum / Maximum Bandwidth / Max Kbps / Upper Limit / Peak Bandwidth | int | schema / qosqueues |
| qosqueues.qos_marking | qos marking / Trust Level / Security Marking / Traffic Class | enum('untrusted','trusted') | schema / qosqueues |
| qosqueues.dscp | dscp / DSCP Value / Differentiated Services Code Point / IP Precedence / Traffic Priority Code | int | schema / qosqueues |

## quotas

Stores resource usage limits and quotas for specific network resources (such as ports, networks, and security groups) assigned to tenants.

恢复表名: quotas / quota / resource quotas / tenant quotas / network quotas / resource limits / quota limits
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| quotas.id | id / identifier / quota id / primary key / uuid | varchar(36) | schema / quotas |
| quotas.tenant_id | tenant id / tenant identifier / project id / tenant / project / customer id / account id | varchar(255) | schema / quotas |
| quotas.resource | resource / resource type / quota resource / network resource / resource name / resource kind | varchar(255) | schema / quotas |
| quotas.limit | limit / quota limit / max limit / maximum / cap / threshold / allowed amount | int | schema / quotas |

## quotausages

Tracks the current usage and reservation of network resources (such as ports, networks, and security groups) against tenant quotas in the Neutron service.

恢复表名: quotausages / quota usages / quota usage / resource quota usage / tenant quota usage / network quota usage / openstack quota usage
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| quotausages.tenant_id | tenant id / tenant identifier / project id / project / tenant / user id / account id | varchar(255) | schema / quotausages |
| quotausages.resource | resource / resource type / resource name / quota resource / network resource / resource kind | varchar(255) | schema / quotausages |
| quotausages.dirty | dirty / dirty flag / is dirty / needs update / stale flag / recalculation needed | tinyint(1) | schema / quotausages |
| quotausages.in_use | in use / in use count / used count / current usage / active count / consumed resources / usage count | int | schema / quotausages |
| quotausages.reserved | reserved / reserved count / reserved resources / pending count / reserved quota / held resources | int | schema / quotausages |

## reservations

Stores records of resource reservations, including unique identifiers, tenant ownership, and expiration timestamps.

恢复表名: reservations / reservation / booking / bookings / resource_reservations / resource_bookings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| reservations.id | id / identifier / reservation_id / reservation_uuid / booking_id / booking_uuid / reservation_identifier / unique_reservation_id | varchar(36) | schema / reservations |
| reservations.tenant_id | tenant id / tenant identifier / tenant / tenant_identifier / organization_id / org_id / account_id / customer_id | varchar(255) | schema / reservations |
| reservations.expiration | expiration / expiration_date / expiry_date / expiration_time / expiry_time / end_date / end_time / reservation_end | datetime | schema / reservations |

## resourcedeltas

Tracks incremental changes or deltas in resource consumption or allocation for specific resources identified by reservation.

恢复表名: resourcedeltas / resource deltas / resource changes / resource usage deltas / resource allocation changes / resource consumption records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| resourcedeltas.resource | resource / resource type / resource name / resource kind / resource identifier / resource category | varchar(255) | schema / resourcedeltas |
| resourcedeltas.reservation_id | reservation id / reservation identifier / reservation uuid / reservation key / reservation reference | varchar(36) | schema / resourcedeltas |
| resourcedeltas.amount | amount / delta amount / change amount / resource delta / quantity change / usage delta / increment | int | schema / resourcedeltas |

## router_extra_attributes

Stores additional configuration attributes and flags for OpenStack Neutron routers, including distributed mode, service router status, high availability settings, and availability zone hints.

恢复表名: router extra attributes / router_extra_attributes / router attributes / router extra info / router metadata / router properties / router configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| router_extra_attributes.router_id | router id / router identifier / id / router uuid / router unique id | varchar(36) | schema / router_extra_attributes |
| router_extra_attributes.distributed | distributed / is distributed / distributed mode / distributed router / distributed flag | tinyint(1) | schema / router_extra_attributes |
| router_extra_attributes.service_router | service router / is service router / service router flag / service router status | tinyint(1) | schema / router_extra_attributes |
| router_extra_attributes.ha | ha / high availability / is ha / ha enabled / ha flag | tinyint(1) | schema / router_extra_attributes |
| router_extra_attributes.ha_vr_id | ha vr id / ha vr identifier / virtual router id / ha virtual router id / vr id | int | schema / router_extra_attributes |
| router_extra_attributes.availability_zone_hints | availability zone hints / az hints / availability zones / az hints list / zone hints | varchar(255) | schema / router_extra_attributes |

## routerl3agentbindings

Maps OpenStack routers to the L3 agents responsible for handling their traffic, indicating which agent is bound to which router.

恢复表名: routerl3agentbindings / router l3 agent bindings / l3 agent bindings / router agent bindings / l3 agent router mapping / router l3 agent mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| routerl3agentbindings.router_id | router id / router identifier / router uuid / network router id / l3 router id | varchar(36) | schema / routerl3agentbindings |
| routerl3agentbindings.l3_agent_id | l3 agent id / l3 agent identifier / l3 agent uuid / agent id / layer 3 agent id | varchar(36) | schema / routerl3agentbindings |

## routerports

Maps network ports to routers, indicating whether a port is connected as a router interface or a router gateway.

恢复表名: routerports / router ports / router port associations / router interface mappings / router gateway links / network router connections
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| routerports.router_id | router id / router identifier / router uuid / associated router / parent router | varchar(36) | schema / routerports |
| routerports.port_id | port id / port identifier / port uuid / network port / interface id | varchar(36) | schema / routerports |
| routerports.port_type | port type / connection type / interface role / router port role / gateway or interface | varchar(255) | schema / routerports |

## routerroutes

Stores the routing table entries for routers, mapping network destinations to their next hop addresses.

恢复表名: routerroutes / router routes / routing table / network routes / route entries / router route mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| routerroutes.destination | destination / destination address / dest ip / target network / route destination / subnet / network address | varchar(64) | schema / routerroutes |
| routerroutes.nexthop | nexthop / next hop / next hop address / gateway / forwarding address / next router / hop ip | varchar(64) | schema / routerroutes |
| routerroutes.router_id | router id / router identifier / router uuid / device id / router key / network device id / router unique id | varchar(36) | schema / routerroutes |

## routerrules

Stores configuration rules that define how network traffic is routed from a source to a destination, including the specific action to take and the associated router.

恢复表名: routerrules / router rules / routing rules / route rules / network routing configuration / traffic routing rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| routerrules.id | id / identifier / rule id / rule identifier / primary key / unique id | int | schema / routerrules |
| routerrules.source | source / source address / origin / source ip / from address / source location | varchar(64) | schema / routerrules |
| routerrules.destination | destination / destination address / target / destination ip / to address / target location | varchar(64) | schema / routerrules |
| routerrules.action | action / routing action / operation / rule action / traffic action / handling method | varchar(10) | schema / routerrules |
| routerrules.router_id | router id / router identifier / router uuid / associated router / router reference | varchar(36) | schema / routerrules |

## routers

Stores metadata and configuration for virtual routers in the Neutron networking service, including their status, administrative state, and gateway port associations.

恢复表名: routers / router / network routers / virtual routers / neutron routers / routing devices
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| routers.tenant_id | tenant id / tenant identifier / project id / owner id / project identifier / user tenant | varchar(255) | schema / routers |
| routers.id | id / identifier / router id / router identifier / unique id / primary key / router uuid / resource id | varchar(36) | schema / routers |
| routers.name | name / router name / display name / label / router title / name of router / router label | varchar(255) | schema / routers |
| routers.status | status / router status / operational status / state / current status / router state / active status | varchar(16) | schema / routers |
| routers.admin_state_up | admin state up / admin state / administrative state / enabled / admin up / router enabled / management state | tinyint(1) | schema / routers |
| routers.gw_port_id | gw port id / gw port identifier / gateway port id / external port id / gw port / gateway port identifier / external gateway port / internet port id | varchar(36) | schema / routers |
| routers.enable_snat | enable snat / snat enabled / source network address translation / snat flag / nat enabled / snat active / source nat | tinyint(1) | schema / routers |
| routers.standard_attr_id | standard attr id / standard attr identifier / standard attribute id / internal id / row id / system id / standard id / internal identifier | bigint | schema / routers |

## securitygroupportbindings

Junction table mapping network ports to the security groups they are bound to, enabling many-to-many relationships between ports and security groups in the Neutron networking service.

恢复表名: securitygroupportbindings / security group port bindings / sg port bindings / port security group associations / security group memberships / port to security group mapping
SQL表别名: b, s, sg, sgb, sgp, sgpb, sgpb2, sgpb3, spb, spb2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| securitygroupportbindings.port_id | port id / port identifier / network port id / port uuid / bound port id | varchar(36) | neutron_100, neutron_1001, neutron_106, neutron_113, neutron_116, neutron_119, neutron_12, neutron_126 |
| securitygroupportbindings.security_group_id | security group id / security group identifier / sg id / sg uuid / bound security group id | varchar(36) | neutron_100, neutron_1001, neutron_106, neutron_113, neutron_116, neutron_119, neutron_12, neutron_126 |

## securitygrouprules

Stores individual firewall rules defining network traffic permissions (ingress/egress) for security groups, including protocol, port ranges, and remote sources.

恢复表名: securitygrouprules / security group rules / firewall rules / network access rules / security rules / sg rules / ingress egress rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| securitygrouprules.tenant_id | tenant id / tenant identifier / project id / tenant / project / owner id / account id | varchar(255) | schema / securitygrouprules |
| securitygrouprules.id | id / identifier / rule id / security group rule id / sg rule id / primary key / unique identifier | varchar(36) | schema / securitygrouprules |
| securitygrouprules.security_group_id | security group id / security group identifier / sg id / security group / group id / parent security group / associated security group | varchar(36) | schema / securitygrouprules |
| securitygrouprules.remote_group_id | remote group id / remote group identifier / remote security group / source group / destination group / peer group id / remote sg | varchar(36) | schema / securitygrouprules |
| securitygrouprules.direction | direction / traffic direction / inbound outbound / ingress egress / flow direction / rule direction | enum('ingress','egress') | schema / securitygrouprules |
| securitygrouprules.ethertype | ethertype / ip version / address family / ipv4 ipv6 / network type / protocol family | varchar(40) | schema / securitygrouprules |
| securitygrouprules.protocol | protocol / transport protocol / network protocol / tcp udp icmp / protocol type / service protocol | varchar(40) | schema / securitygrouprules |
| securitygrouprules.port_range_min | port range min / port range minimum / start port / minimum port / lower port bound / from port / port start | int | schema / securitygrouprules |
| securitygrouprules.port_range_max | port range max / port range maximum / end port / maximum port / upper port bound / to port / port end | int | schema / securitygrouprules |
| securitygrouprules.remote_ip_prefix | remote ip prefix / source ip / destination ip / cidr block / ip range / remote address / subnet | varchar(255) | schema / securitygrouprules |
| securitygrouprules.standard_attr_id | standard attr id / standard attr identifier / standard attribute id / internal id / system id / attr id / standard identifier | bigint | schema / securitygrouprules |

## securitygroups

Stores definitions of security groups used to control network traffic and access permissions for cloud resources.

恢复表名: securitygroups / security groups / firewall rules / network security groups / sgs / access control lists / network ACLs
SQL表别名: g, sg

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| securitygroups.tenant_id | tenant id / tenant identifier / project id / owner id / account id / customer id / organization id | varchar(255) | schema / securitygroups |
| securitygroups.id | id / identifier / security group id / sg id / group id / unique identifier / primary key | varchar(36) | schema / securitygroups |
| securitygroups.name | name / security group name / group name / sg name / label / title | varchar(255) | schema / securitygroups |
| securitygroups.standard_attr_id | standard attr id / standard attr identifier / standard attribute id / attr id / attribute id / standard id / reference id | bigint | schema / securitygroups |

## serviceprofiles

Stores definitions and configurations for service profiles, including their descriptions, associated drivers, enablement status, and metadata.

恢复表名: serviceprofiles / service profiles / service profile / profiles / service profile definitions / profile configurations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| serviceprofiles.id | id / identifier / profile id / service profile id / unique identifier / profile identifier | varchar(36) | schema / serviceprofiles |
| serviceprofiles.description | description / profile description / service description / description text / profile details | varchar(1024) | schema / serviceprofiles |
| serviceprofiles.driver | driver / service driver / profile driver / driver name / associated driver | varchar(1024) | schema / serviceprofiles |
| serviceprofiles.enabled | enabled / is enabled / profile status / enablement flag / active status | tinyint(1) | schema / serviceprofiles |
| serviceprofiles.metainfo | metainfo / metadata / profile metadata / meta information / additional info | varchar(4096) | schema / serviceprofiles |

## sessionpersistences

Stores the session persistence configuration for Virtual IP (VIP) endpoints, defining how client sessions are maintained across backend servers using methods like source IP or cookies.

恢复表名: sessionpersistences / session persistence / session persistence settings / session persistence configuration / vip session persistence / load balancer session persistence
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| sessionpersistences.vip_id | vip id / vip identifier / virtual ip id / load balancer id / service id / endpoint id | varchar(36) | schema / sessionpersistences |
| sessionpersistences.type | type / persistence type / session method / persistence method / session stickiness type / persistence mode | enum('SOURCE_IP','HTTP_COOKIE','APP_COOKIE') | schema / sessionpersistences |
| sessionpersistences.cookie_name | cookie name / session cookie name / persistence cookie / cookie identifier / http cookie name | varchar(1024) | schema / sessionpersistences |

## standardattributes

Stores standard metadata and timestamps for Neutron network resources such as ports, networks, subnets, and floating IPs.

恢复表名: standardattributes / standard attributes / standard attribute / std attrs / neutron standard attributes / resource standard attributes
SQL表别名: sa, sa2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| standardattributes.id | id / identifier / standard attribute id / standard_attr_id / attribute id / std attr id / primary key | bigint | neutron_1006, neutron_382, neutron_1009, neutron_1014, neutron_104, neutron_111, neutron_115, neutron_121 |
| standardattributes.resource_type | resource type / type of resource / neutron resource type / object type | varchar(255) | neutron_1006, neutron_1009, neutron_1014, neutron_104, neutron_111, neutron_115, neutron_121, neutron_127 |
| standardattributes.created_at | created at / creation date / created timestamp / creation time / date created | datetime | schema / standardattributes |
| standardattributes.updated_at | updated at / update date / updated timestamp / last updated / modification time / earliest standard attribute updated timestamp | datetime | neutron_1006, neutron_382, neutron_1009, neutron_1014, neutron_104, neutron_111, neutron_115, neutron_121 |
| standardattributes.description | description / attribute description / description text / notes / standard attribute description | varchar(255) | neutron_382 |

## subnetpoolprefixes

Stores the CIDR prefixes associated with a specific subnet pool in the Neutron networking service.

恢复表名: subnetpoolprefixes / subnet pool prefixes / subnet pool CIDR ranges / subnet pool address ranges
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| subnetpoolprefixes.cidr | cidr / network prefix / IP range / subnet prefix / address range / network address | varchar(64) | schema / subnetpoolprefixes |
| subnetpoolprefixes.subnetpool_id | subnetpool id / subnetpool identifier / subnet pool ID / pool ID / parent pool ID / subnet pool reference | varchar(36) | schema / subnetpoolprefixes |

## subnetpools

Stores definitions of IP address pools (subnet pools) that define the range of IP addresses and prefix lengths available for creating subnets in a specific tenant or project.

恢复表名: subnetpools / subnet pools / subnet pool / ip pools / address pools / neutron subnet pools
SQL表别名: sp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| subnetpools.tenant_id | tenant id / tenant identifier / project id / project / owner id / owner / tenant / user id | varchar(255) | neutron_767, neutron_968 |
| subnetpools.id | id / identifier / pool id / subnet pool id / uuid / unique identifier | varchar(36) | schema / subnetpools |
| subnetpools.name | name / pool name / subnet pool name / label / title | varchar(255) | neutron_767, neutron_968 |
| subnetpools.ip_version | ip version / protocol version / ipv4 ipv6 / address family | int | neutron_767, neutron_968 |
| subnetpools.default_prefixlen | default prefixlen / default prefix length / default cidr length / default mask / default subnet size | int | schema / subnetpools |
| subnetpools.min_prefixlen | min prefixlen / minimum prefixlen / minimum prefix length / min cidr / smallest subnet size / min mask | int | schema / subnetpools |
| subnetpools.max_prefixlen | max prefixlen / maximum prefixlen / maximum prefix length / max cidr / largest subnet size / max mask | int | schema / subnetpools |
| subnetpools.shared | shared / is shared / shared flag / public pool / visibility | tinyint(1) | schema / subnetpools |
| subnetpools.default_quota | default quota / quota / limit / max subnets | int | schema / subnetpools |
| subnetpools.hash | hash / hash value / checksum / fingerprint | varchar(36) | schema / subnetpools |
| subnetpools.address_scope_id | address scope id / address scope identifier / address scope / scope id / address scope uuid | varchar(36) | schema / subnetpools |
| subnetpools.is_default | is default / default pool / default flag | tinyint(1) | schema / subnetpools |
| subnetpools.standard_attr_id | standard attr id / standard attr identifier / standard attribute id / std attr id / standard attributes uuid | bigint | schema / subnetpools |

## subnetroutes

Stores static route entries for subnets, defining the destination network and the next hop address for traffic forwarding.

恢复表名: subnetroutes / subnet routes / routes / subnet route table / network routes / routing entries
SQL表别名: r, r2, r3, r4, sr, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| subnetroutes.destination | destination / route destination / destination network / dest / target network / destination CIDR / route target | varchar(64) | neutron_1008, neutron_108, neutron_190, neutron_347, neutron_433, neutron_445, neutron_447, neutron_450 |
| subnetroutes.nexthop | nexthop / next hop / next hop address / gateway / router IP / forwarding address / next hop IP | varchar(64) | neutron_1008, neutron_108, neutron_190, neutron_347, neutron_433, neutron_445, neutron_447, neutron_450 |
| subnetroutes.subnet_id | subnet id / subnet identifier / parent subnet / associated subnet / subnet uuid / route subnet | varchar(36) | neutron_1008, neutron_108, neutron_190, neutron_347, neutron_433, neutron_445, neutron_447, neutron_450 |

## subnets

Stores configuration details for IP subnets within OpenStack Neutron networks, including CIDR blocks, gateway IPs, DHCP settings, and IP versioning.

恢复表名: subnets / network subnets / subnet records / IP subnets / OpenStack subnets / Neutron subnets
SQL表别名: s, s2, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| subnets.tenant_id | tenant id / tenant identifier / project ID / owner ID / account ID / project identifier | varchar(255) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.id | id / identifier / subnet ID / subnet identifier / unique subnet ID / primary key / subnet UUID / resource ID | varchar(36) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.name | name / subnet name / subnet label / subnet title / display name / subnet designation / subnet string | varchar(255) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.network_id | network id / network identifier / parent network ID / associated network / network UUID / network reference | varchar(36) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.ip_version | ip version / protocol version / IPv4 or IPv6 / address family / IP type / version number | int | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.cidr | cidr / network address / subnet range / IP range / block size / network prefix | varchar(64) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.gateway_ip | gateway ip / default gateway / router IP / gateway address / exit IP / network gateway | varchar(64) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.enable_dhcp | enable dhcp / DHCP enabled / DHCP flag / dynamic host configuration / DHCP status / auto IP assignment / DHCP active | tinyint(1) | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |
| subnets.ipv6_ra_mode | ipv6 ra mode / router advertisement mode / IPv6 routing mode / RA configuration / IPv6 neighbor discovery / router advertisement type | enum('slaac','dhcpv6-stateful','dhcpv6-stateless') | schema / subnets |
| subnets.ipv6_address_mode | ipv6 address mode / address assignment mode / IPv6 configuration mode / addressing mode / IPv6 client mode / address acquisition method | enum('slaac','dhcpv6-stateful','dhcpv6-stateless') | schema / subnets |
| subnets.subnetpool_id | subnetpool id / subnetpool identifier / subnet pool ID / pool ID / subnet pool identifier / resource pool / IP pool ID / subnet pool reference | varchar(36) | schema / subnets |
| subnets.standard_attr_id | standard attr id / standard attr identifier / standard attribute ID / attribute reference / standard attributes ID / metadata ID / standard config ID | bigint | neutron_1008, neutron_28, neutron_312, neutron_324, neutron_4, neutron_461, neutron_591, neutron_645 |

## tags

Stores specific tag labels associated with standard attributes in the Neutron schema.

恢复表名: tags / tag table / standard attribute tags / attribute tags
SQL表别名: t

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tags.standard_attr_id | standard attr id / standard attr identifier / standard attribute id / attribute id / attr id / standard attribute identifier | bigint | neutron_509 |
| tags.tag | tag / tag name / label / attribute tag / tag value / tag string | varchar(60) | neutron_509 |

## tz_network_bindings

Stores the mapping between logical network identifiers and physical network bindings, including the binding type and VLAN ID for each physical UUID.

恢复表名: tz network bindings / network bindings / network binding table / physical network bindings / network binding configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tz_network_bindings.network_id | network id / network identifier / logical network id / network uuid | varchar(36) | schema / tz_network_bindings |
| tz_network_bindings.binding_type | binding type / network binding type / encapsulation type / binding mode / flat vlan stt gre l3_ext | enum('flat','vlan','stt','gre','l3_ext') | schema / tz_network_bindings |
| tz_network_bindings.phy_uuid | phy uuid / physical uuid / physical network uuid / physical identifier | varchar(36) | schema / tz_network_bindings |
| tz_network_bindings.vlan_id | vlan id / vlan identifier / virtual lan id / vlan number | int | schema / tz_network_bindings |

## vcns_router_bindings

Stores the binding relationships between virtual routers, edge nodes, and logical switches in the Neutron network, including the current status of each binding.

恢复表名: vcns router bindings / router bindings / vrouter bindings / router edge bindings / router switch bindings / vcns router binding table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| vcns_router_bindings.status | status / binding status / router binding state / status code / current status | varchar(16) | schema / vcns_router_bindings |
| vcns_router_bindings.status_description | status description / status message / binding description / error message / status details / reason for status | varchar(255) | schema / vcns_router_bindings |
| vcns_router_bindings.router_id | router id / router identifier / vrouter id / router uuid / network router id | varchar(36) | schema / vcns_router_bindings |
| vcns_router_bindings.edge_id | edge id / edge identifier / edge node id / edge uuid / physical edge id | varchar(16) | schema / vcns_router_bindings |
| vcns_router_bindings.lswitch_id | lswitch id / lswitch identifier / logical switch id / switch uuid / virtual switch id | varchar(36) | schema / vcns_router_bindings |

## vips

Stores configuration details for Virtual IP (VIP) endpoints in a load balancing service, including protocol, port, associated pool, and status.

恢复表名: vips / virtual IP / VIP / load balancer VIP / virtual IP address / load balancer virtual IP / VIP configuration
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| vips.tenant_id | tenant id / tenant identifier / project ID / owner ID / account ID | varchar(255) | schema / vips |
| vips.id | id / identifier / VIP ID / virtual IP ID / VIP identifier / load balancer VIP ID | varchar(36) | schema / vips |
| vips.name | name / VIP name / virtual IP name / VIP label / VIP title | varchar(255) | schema / vips |
| vips.description | description / VIP description / virtual IP description / VIP notes / VIP details | varchar(255) | schema / vips |
| vips.port_id | port id / port identifier / network port ID / associated port ID / VIP port ID | varchar(36) | schema / vips |
| vips.protocol_port | protocol port / VIP port number / service port / listening port | int | schema / vips |
| vips.protocol | protocol / VIP protocol / load balancer protocol / traffic protocol / connection protocol | enum('HTTP','HTTPS','TCP') | schema / vips |
| vips.pool_id | pool id / pool identifier / load balancer pool ID / backend pool ID / associated pool ID | varchar(36) | schema / vips |
| vips.status | status / VIP status / virtual IP status / VIP state / operational status | varchar(16) | schema / vips |
| vips.status_description | status description / VIP status details / status message / status reason | varchar(255) | schema / vips |
| vips.admin_state_up | admin state up / VIP enabled / VIP active flag / administrative state | tinyint(1) | schema / vips |
| vips.connection_limit | connection limit / max connections / VIP connection cap / concurrent connections limit | int | schema / vips |

## vpnservices

Stores metadata and configuration for VPN services in the Neutron networking service, linking them to specific subnets and routers.

恢复表名: vpnservices / vpn services / vpn service / vpn / openstack vpn / neutron vpn
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| vpnservices.tenant_id | tenant id / tenant identifier / project id / project / tenant / owner / account id | varchar(255) | schema / vpnservices |
| vpnservices.id | id / identifier / vpn service id / uuid / service id / primary key | varchar(36) | schema / vpnservices |
| vpnservices.name | name / vpn name / service name / label / title | varchar(255) | schema / vpnservices |
| vpnservices.description | description / vpn description / notes / details / comment | varchar(255) | schema / vpnservices |
| vpnservices.status | status / vpn status / state / operational status / health | varchar(16) | schema / vpnservices |
| vpnservices.admin_state_up | admin state up / admin state / enabled / disabled / up down / administrative state | tinyint(1) | schema / vpnservices |
| vpnservices.subnet_id | subnet id / subnet identifier / subnet / network subnet / local subnet / subnet uuid | varchar(36) | schema / vpnservices |
| vpnservices.router_id | router id / router identifier / router / gateway router / vpn router / router uuid | varchar(36) | schema / vpnservices |

## 表关系与连接依据

- agents.admin_state_up ↔ healthmonitors.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ lbaas_listeners.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ lbaas_loadbalancers.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ lbaas_members.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ lbaas_pools.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- agents.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- allowedaddresspairs.port_id ↔ ports.id; declared_or_materialized_relationship
- dnsnameservers.subnet_id ↔ subnets.id; declared_or_materialized_relationship, target_disjoint_historical_join
- externalnetworks.network_id ↔ networkrbacs.id; declared_or_materialized_relationship, target_disjoint_historical_join
- externalnetworks.network_id ↔ networkrbacs.object_id; declared_or_materialized_relationship
- externalnetworks.network_id ↔ networks.id; declared_or_materialized_relationship, target_disjoint_historical_join
- extradhcpopts.port_id ↔ ports.id; declared_or_materialized_relationship
- floatingips.fixed_port_id ↔ ports.id; declared_or_materialized_relationship, target_disjoint_historical_join
- floatingips.fixed_port_id ↔ portsecuritybindings.port_id; declared_or_materialized_relationship
- floatingips.standard_attr_id ↔ standardattributes.id; declared_or_materialized_relationship
- floatingips.tenant_id ↔ lbaas_listeners.tenant_id; profile_name_value_compatibility
- floatingips.tenant_id ↔ lbaas_loadbalancers.tenant_id; profile_name_value_compatibility
- floatingips.tenant_id ↔ lbaas_members.tenant_id; profile_name_value_compatibility
- floatingips.tenant_id ↔ lbaas_pools.tenant_id; profile_name_value_compatibility
- floatingips.tenant_id ↔ subnets.tenant_id; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ lbaas_listeners.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ lbaas_loadbalancers.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ lbaas_members.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ lbaas_pools.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- healthmonitors.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- healthmonitors.tenant_id ↔ vips.tenant_id; profile_name_value_compatibility
- ipallocationpools.last_ip ↔ subnets.gateway_ip; declared_or_materialized_relationship
- ipallocationpools.subnet_id ↔ subnets.id; declared_or_materialized_relationship, target_disjoint_historical_join
- ipallocations.network_id ↔ networkdhcpagentbindings.network_id; profile_name_value_compatibility
- ipallocations.network_id ↔ networksecuritybindings.network_id; profile_name_value_compatibility
- ipallocations.network_id ↔ ports.network_id; profile_name_value_compatibility
- ipallocations.port_id ↔ ml2_port_binding_levels.port_id; profile_name_value_compatibility
- ipallocations.port_id ↔ ml2_port_bindings.port_id; profile_name_value_compatibility
- ipallocations.port_id ↔ ports.id; declared_or_materialized_relationship, target_disjoint_historical_join
- ipallocations.port_id ↔ portsecuritybindings.port_id; profile_name_value_compatibility
- ipallocations.port_id ↔ securitygroupportbindings.port_id; declared_or_materialized_relationship
- ipallocations.subnet_id ↔ pools.subnet_id; profile_name_value_compatibility
- ipallocations.subnet_id ↔ subnetroutes.subnet_id; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ lbaas_loadbalancers.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ lbaas_members.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ lbaas_pools.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- lbaas_listeners.connection_limit ↔ vips.connection_limit; profile_name_value_compatibility
- lbaas_listeners.loadbalancer_id ↔ lbaas_loadbalancer_statistics.loadbalancer_id; profile_name_value_compatibility
- lbaas_listeners.loadbalancer_id ↔ lbaas_loadbalanceragentbindings.loadbalancer_id; profile_name_value_compatibility
- lbaas_listeners.loadbalancer_id ↔ lbaas_pools.loadbalancer_id; profile_name_value_compatibility
- lbaas_listeners.operating_status ↔ lbaas_loadbalancers.operating_status; profile_name_value_compatibility
- lbaas_listeners.operating_status ↔ lbaas_members.operating_status; profile_name_value_compatibility
- lbaas_listeners.operating_status ↔ lbaas_pools.operating_status; profile_name_value_compatibility
- lbaas_listeners.protocol ↔ lbaas_pools.protocol; profile_name_value_compatibility
- lbaas_listeners.protocol ↔ securitygrouprules.protocol; profile_name_value_compatibility
- lbaas_listeners.protocol_port ↔ vips.protocol_port; profile_name_value_compatibility
- lbaas_listeners.provisioning_status ↔ lbaas_loadbalancers.provisioning_status; profile_name_value_compatibility
- lbaas_listeners.provisioning_status ↔ lbaas_members.provisioning_status; profile_name_value_compatibility
- lbaas_listeners.provisioning_status ↔ lbaas_pools.provisioning_status; profile_name_value_compatibility
- lbaas_listeners.tenant_id ↔ lbaas_loadbalancers.tenant_id; profile_name_value_compatibility
- lbaas_listeners.tenant_id ↔ lbaas_members.tenant_id; profile_name_value_compatibility
- lbaas_listeners.tenant_id ↔ lbaas_pools.tenant_id; profile_name_value_compatibility
- lbaas_listeners.tenant_id ↔ subnets.tenant_id; profile_name_value_compatibility
- lbaas_loadbalancer_statistics.active_connections ↔ poolstatisticss.active_connections; profile_name_value_compatibility
- lbaas_loadbalancer_statistics.bytes_out ↔ poolstatisticss.bytes_out; profile_name_value_compatibility
- lbaas_loadbalancer_statistics.loadbalancer_id ↔ lbaas_loadbalanceragentbindings.loadbalancer_id; profile_name_value_compatibility
- lbaas_loadbalancer_statistics.loadbalancer_id ↔ lbaas_loadbalancers.id; declared_or_materialized_relationship
- lbaas_loadbalancer_statistics.loadbalancer_id ↔ lbaas_pools.loadbalancer_id; profile_name_value_compatibility
- lbaas_loadbalanceragentbindings.loadbalancer_id ↔ lbaas_pools.loadbalancer_id; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ lbaas_members.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ lbaas_pools.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- lbaas_loadbalancers.id ↔ providerresourceassociations.resource_id; declared_or_materialized_relationship, target_disjoint_historical_join
- lbaas_loadbalancers.operating_status ↔ lbaas_members.operating_status; profile_name_value_compatibility
- lbaas_loadbalancers.operating_status ↔ lbaas_pools.operating_status; profile_name_value_compatibility
- lbaas_loadbalancers.provisioning_status ↔ lbaas_members.provisioning_status; profile_name_value_compatibility
- lbaas_loadbalancers.provisioning_status ↔ lbaas_pools.provisioning_status; profile_name_value_compatibility
- lbaas_loadbalancers.tenant_id ↔ lbaas_members.tenant_id; profile_name_value_compatibility
- lbaas_loadbalancers.tenant_id ↔ lbaas_pools.tenant_id; profile_name_value_compatibility
- lbaas_loadbalancers.tenant_id ↔ subnets.tenant_id; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ lbaas_pools.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- lbaas_members.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- lbaas_members.operating_status ↔ lbaas_pools.operating_status; profile_name_value_compatibility
- lbaas_members.provisioning_status ↔ lbaas_pools.provisioning_status; profile_name_value_compatibility
- lbaas_members.tenant_id ↔ lbaas_pools.tenant_id; profile_name_value_compatibility
- lbaas_members.tenant_id ↔ subnets.tenant_id; profile_name_value_compatibility
- lbaas_members.weight ↔ members.weight; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ members.admin_state_up; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- lbaas_pools.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- lbaas_pools.protocol ↔ securitygrouprules.protocol; profile_name_value_compatibility
- lbaas_pools.tenant_id ↔ subnets.tenant_id; profile_name_value_compatibility
- members.admin_state_up ↔ networks.admin_state_up; profile_name_value_compatibility
- members.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- members.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- members.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- members.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- members.pool_id ↔ poolmonitorassociations.pool_id; profile_name_value_compatibility
- members.pool_id ↔ poolstatisticss.pool_id; profile_name_value_compatibility
- members.pool_id ↔ vips.pool_id; profile_name_value_compatibility
- members.protocol_port ↔ vips.protocol_port; profile_name_value_compatibility
- members.tenant_id ↔ pools.tenant_id; profile_name_value_compatibility
- members.tenant_id ↔ vips.tenant_id; profile_name_value_compatibility
- ml2_dvr_port_bindings.port_id ↔ ports.id; declared_or_materialized_relationship
- ml2_gre_allocations.allocated ↔ ml2_vlan_allocations.allocated; profile_name_value_compatibility
- ml2_network_segments.physical_network ↔ ml2_vlan_allocations.physical_network; profile_name_value_compatibility
- ml2_port_binding_levels.host ↔ ml2_port_bindings.host; profile_name_value_compatibility
- ml2_port_binding_levels.port_id ↔ ml2_port_bindings.port_id; profile_name_value_compatibility
- ml2_port_binding_levels.port_id ↔ portsecuritybindings.port_id; profile_name_value_compatibility
- ml2_port_bindings.port_id ↔ ports.id; declared_or_materialized_relationship, target_disjoint_historical_join
- ml2_port_bindings.port_id ↔ portsecuritybindings.port_id; profile_name_value_compatibility
- networkdhcpagentbindings.network_id ↔ networksecuritybindings.network_id; profile_name_value_compatibility
- networkdhcpagentbindings.network_id ↔ ports.network_id; profile_name_value_compatibility
- networkrbacs.id ↔ networksecuritybindings.network_id; declared_or_materialized_relationship, target_disjoint_historical_join
- networkrbacs.id ↔ subnets.network_id; declared_or_materialized_relationship, target_disjoint_historical_join
- networkrbacs.object_id ↔ networks.id; declared_or_materialized_relationship, target_disjoint_historical_join
- networkrbacs.object_id ↔ subnets.network_id; declared_or_materialized_relationship, target_disjoint_historical_join
- networks.admin_state_up ↔ pools.admin_state_up; profile_name_value_compatibility
- networks.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- networks.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- networks.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- networks.availability_zone_hints ↔ router_extra_attributes.availability_zone_hints; profile_name_value_compatibility
- networks.id ↔ networksecuritybindings.network_id; declared_or_materialized_relationship, target_disjoint_historical_join
- networks.id ↔ ports.network_id; declared_or_materialized_relationship
- networks.id ↔ qos_network_policy_bindings.network_id; declared_or_materialized_relationship
- networks.id ↔ subnets.network_id; declared_or_materialized_relationship, target_disjoint_historical_join
- networks.standard_attr_id ↔ standardattributes.id; declared_or_materialized_relationship
- networks.tenant_id ↔ ports.tenant_id; declared_or_materialized_relationship
- networksecuritybindings.network_id ↔ ports.network_id; profile_name_value_compatibility
- networksecuritybindings.port_security_enabled ↔ portsecuritybindings.port_security_enabled; profile_name_value_compatibility
- poolmonitorassociations.pool_id ↔ poolstatisticss.pool_id; profile_name_value_compatibility
- poolmonitorassociations.pool_id ↔ vips.pool_id; profile_name_value_compatibility
- pools.admin_state_up ↔ ports.admin_state_up; profile_name_value_compatibility
- pools.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- pools.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- pools.description ↔ standardattributes.description; profile_name_value_compatibility
- pools.protocol ↔ vips.protocol; profile_name_value_compatibility
- pools.subnet_id ↔ subnetroutes.subnet_id; profile_name_value_compatibility
- pools.tenant_id ↔ vips.tenant_id; profile_name_value_compatibility
- pools.vip_id ↔ sessionpersistences.vip_id; profile_name_value_compatibility
- poolstatisticss.pool_id ↔ vips.pool_id; profile_name_value_compatibility
- portdnses.port_id ↔ ports.id; declared_or_materialized_relationship, target_disjoint_historical_join
- ports.admin_state_up ↔ routers.admin_state_up; profile_name_value_compatibility
- ports.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- ports.id ↔ portsecuritybindings.port_id; declared_or_materialized_relationship, target_disjoint_historical_join
- ports.id ↔ qos_port_policy_bindings.port_id; declared_or_materialized_relationship
- ports.id ↔ securitygroupportbindings.port_id; declared_or_materialized_relationship, target_disjoint_historical_join
- ports.standard_attr_id ↔ standardattributes.id; declared_or_materialized_relationship, target_disjoint_historical_join
- ports.tenant_id ↔ reservations.tenant_id; profile_name_value_compatibility
- quotas.resource ↔ quotausages.resource; profile_name_value_compatibility
- quotas.resource ↔ resourcedeltas.resource; profile_name_value_compatibility
- quotausages.resource ↔ resourcedeltas.resource; profile_name_value_compatibility
- router_extra_attributes.router_id ↔ routerl3agentbindings.router_id; profile_name_value_compatibility
- router_extra_attributes.router_id ↔ routerports.router_id; profile_name_value_compatibility
- routerl3agentbindings.router_id ↔ routerports.router_id; profile_name_value_compatibility
- routers.admin_state_up ↔ vips.admin_state_up; profile_name_value_compatibility
- standardattributes.id ↔ subnets.standard_attr_id; declared_or_materialized_relationship
- standardattributes.id ↔ tags.standard_attr_id; declared_or_materialized_relationship
- subnetroutes.subnet_id ↔ subnets.id; declared_or_materialized_relationship

## 业务口径、总体与粒度

### allowed address pair IP address

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"allowed address pair IP address\", \"allowed address pair IP address 10.232.210.41/8\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4ad2f37cc4fd98edd5f3\", \"physical_identifier\": \"allowedaddresspairs.ip_address\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4ad2f37cc4fd98edd5f3"
  ]
}
```

### allowed address pair MAC address

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"allowed address pair MAC address\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.381d7674ffbe695f2c51\", \"physical_identifier\": \"allowedaddresspairs.mac_address\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.381d7674ffbe695f2c51"
  ]
}
```

### allowed address pairs per port

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"allowed address pairs per port\", \"ports (filtered by allowed address pair)\", \"ports (with at least one allowed address pair)\", \"range of number of allowed address pairs per port\", \"variance of number of allowed address pairs per port\", \"standard deviation of number of allowed address pairs per port\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.69178cd8f8950902ed1a\", \"physical_identifier\": \"allowedaddresspairs.port_id\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.69178cd8f8950902ed1a"
  ]
}
```

### DNS nameserver address

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | Subnet ID \"0807c5b3-aa6c-4108-8884-7b4948a19178\" is predicated by \"subnets.id IN ('0807c5b3-aa6c-4108-8884-7b4948a19178')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.96fe6f136440f1d6e40f"
  ]
}
```

### standard deviation

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.75ade2ffe476e74080d1"
  ]
}
```

### DNS nameserver entry

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.57cd2f7e74476b1407e8"
  ]
}
```

### whether it is default

```json
{
  "kind": "metric",
  "formula": "\"access_as_external\" permission is predicated by \"networkrbacs.action = 'access_as_external'\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.46b5f445866bccbe4c18"
  ]
}
```

### network ID

```json
{
  "kind": "metric",
  "formula": "\"access_as_external\" permission is predicated by \"networkrbacs.action = 'access_as_external'\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.08ff9979af934f61f573"
  ]
}
```

### IPv4

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.73e20f7b7404054e2626"
  ]
}
```

### extra DHCP option

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e34b399749e8eaa551a3"
  ]
}
```

### floating IP records

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4c1aa173d2f1a1869752"
  ]
}
```

### standard attribute association

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8b26f541599ef8ecdcee"
  ]
}
```

### status 'DOWN'

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.906b3f0db9b4fc245c6b"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4fd22f9eda6dda690f27"
  ]
}
```

### allocation pool size

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b1d11311328179caadcc"
  ]
}
```

### IP allocation pools

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"IP allocation pools\", \"number of IP allocation pools per subnet\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.d7cc4243bb4d8c58b88f\", \"physical_identifier\": \"ipallocationpools.subnet_id\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d7cc4243bb4d8c58b88f"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "IP Address \"10.150.64.113/8\" is predicated by \"ipallocations.ip_address IN ('10.150.64.113/8')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c1496b06080450ce6158"
  ]
}
```

### port ID

```json
{
  "kind": "metric",
  "formula": "IP Address \"10.150.64.113/8\" is predicated by \"ipallocations.ip_address IN ('10.150.64.113/8')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a4fa60362ed8d6b0b018"
  ]
}
```

### subnet ID

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | IP Address \"10.150.64.113/8\" is predicated by \"ipallocations.ip_address IN ('10.150.64.113/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a88c119ba2100bd222ee"
  ]
}
```

### bytes in

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c121f5b1fb6896ea04e3"
  ]
}
```

### load balancer ID

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"load balancer ID\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.74466716648f876a1cb8\", \"physical_identifier\": \"lbaas_loadbalancer_statistics.loadbalancer_id\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.74466716648f876a1cb8"
  ]
}
```

### total connections

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f7ca99d5eaaa4a222871"
  ]
}
```

### highest admin_state_up value

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"highest admin_state_up value\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.82739189edac2bc44346\", \"physical_identifier\": \"lbaas_loadbalancers.admin_state_up\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.82739189edac2bc44346"
  ]
}
```

### load balancer

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.278ef0edc36013094939"
  ]
}
```

### name

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9e4257018f3456935565"
  ]
}
```

### currently ONLINE

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2f27e0dea219adf1ad44"
  ]
}
```

### provisioning status

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.632c8d30f5e2530c8471"
  ]
}
```

### tenant

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"tenant\", \"dense rank within each tenant\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4c081bf11f0817d9af4f\", \"physical_identifier\": \"lbaas_loadbalancers.tenant_id\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4c081bf11f0817d9af4f"
  ]
}
```

### VIP address

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a0572ba7a1852ef6153b"
  ]
}
```

### ports

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.695f55e944d40cf43549"
  ]
}
```

### host

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.037779d6bb9f541b5b55"
  ]
}
```

### ports

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.be34183a61459ca9cae6"
  ]
}
```

### VIF type

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4d22d6b1a2272b233291"
  ]
}
```

### VNIC type

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.daf60db2d42debe5a3d6"
  ]
}
```

### action name

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cac218acd2e2b99a5945"
  ]
}
```

### minimum RBAC ID

```json
{
  "kind": "metric",
  "formula": "\"public access\" (wildcard) is predicated by \"networkrbacs.target_tenant = '*'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ee44fcfd1956b8f99aee"
  ]
}
```

### RBAC rule

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7226f2461646d5437e64"
  ]
}
```

### target tenant

```json
{
  "kind": "metric",
  "formula": "Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.fe9f9ce63f8f6e750475"
  ]
}
```

### admin_state_up

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3ad9c8ccda268d397b68"
  ]
}
```

### network

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9be1e18968d815249abf"
  ]
}
```

### MTU

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.85ad98148d7a6d3a1403"
  ]
}
```

### network name

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a04eab279ed3a59f4fea"
  ]
}
```

### standard attribute ID

```json
{
  "kind": "metric",
  "formula": "\"access_as_external\" permission is predicated by \"networkrbacs.action = 'access_as_external'\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.58e13d9586c3d2211cf0"
  ]
}
```

### status

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.03963609813544e18d17"
  ]
}
```

### tenant ID

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.602ff33c9be9fee5cda5"
  ]
}
```

### network

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cee532547a2c5754221a"
  ]
}
```

### variance

```json
{
  "kind": "metric",
  "formula": "\"public access\" (wildcard) is predicated by \"networkrbacs.target_tenant = '*'\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.01bb7df407b58b78b83c"
  ]
}
```

### DNS records associated with the port

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.541aa12beaf2615ac8e4"
  ]
}
```

### admin state

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.931d4b879d834ec11488"
  ]
}
```

### device owner

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.aa1a80dfeb44ca52485d"
  ]
}
```

### port

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7f6af285b32f1abadcb8"
  ]
}
```

### MAC address

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bab839448e65a7f7c884"
  ]
}
```

### port name

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bd1a9638dbd99d3f3c2c"
  ]
}
```

### network

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.528e791740a318fde5f3"
  ]
}
```

### geometric mean

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9dc69bfb61c26b886397"
  ]
}
```

### DOWN

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cad613a244343f6ce88a"
  ]
}
```

### tenant ID

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"ports.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8d9ff8e3590dcb82e3d2"
  ]
}
```

### ports

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | IP Address \"10.150.64.113/8\" is predicated by \"ipallocations.ip_address IN ('10.150.64.113/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8d2c3a2c71165277ea2f"
  ]
}
```

### dense rank

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\" | IP Address \"10.150.64.113/8\" is predicated by \"ipallocations.ip_address IN ('10.150.64.113/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a4633ecce526bbf5183d"
  ]
}
```

### provider name

```json
{
  "kind": "metric",
  "formula": "Fixed IP Address \"10.20.127.222/8\" is predicated by \"floatingips.fixed_ip_address IN ('10.20.127.222/8')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6a7de45ee57e2b4c9802"
  ]
}
```

### associated with provider

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"associated with provider\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.0639c9e2b22273e3e0c9\", \"physical_identifier\": \"providerresourceassociations.resource_id\", \"schema_context\": \"neutron\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0639c9e2b22273e3e0c9"
  ]
}
```

### linked to QoS network policy binding

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.599f65ad35297152cc49"
  ]
}
```

### bound to a QoS port policy

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5ae4e9e6b178c7ee844f"
  ]
}
```

### bound to a security group

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6499aeffb7e2f9d9ac0e"
  ]
}
```

### security group

```json
{
  "kind": "metric",
  "formula": "Network ID \"0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d\" is predicated by \"ports.network_id IN ('0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d')\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f570c67d8bb194c5d215"
  ]
}
```

### standard attribute

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c8ee76c0a11f899a5452"
  ]
}
```

### resource type

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d3f5eb9f9e8852d73764"
  ]
}
```

### standard attribute updated timestamp

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Tenant ID \"17ea94ad74b64b9d92f4888336a598c7\" is predicated by \"ports.tenant_id IN ('17ea94ad74b64b9d92f4888336a598c7')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d6d8d63d04d380f61be9"
  ]
}
```

### route destination

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a7ab0bc9e7354cd92bf8"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a791b688c7cd1e7fb7e5"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5ef5e46a1e3155370bd4"
  ]
}
```

### CIDR

```json
{
  "kind": "metric",
  "formula": "Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ea296d41d4e3e9c88009"
  ]
}
```

### DHCP enabled

```json
{
  "kind": "metric",
  "formula": "\"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.385f6b1b4787c30db6c6"
  ]
}
```

### gateway IP

```json
{
  "kind": "metric",
  "formula": "Tenant ID \"98333a1a28e746fa8c629c83a818ad57\" is predicated by \"networks.tenant_id IN ('98333a1a28e746fa8c629c83a818ad57')\" | \"public access\" (wildcard) is predicated by \"networkrbacs.target_tenant = '*'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7c9f27e7c6e9ef6ce4f6"
  ]
}
```

### subnet

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\" | Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9bcb877f0fd9de5400e4"
  ]
}
```

### IP version

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.db5ae33f9330a673f5cd"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b9dc5368f3a3e49ae703"
  ]
}
```

### subnets

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | \"access_as_shared\" permission is predicated by \"networkrbacs.action = 'access_as_shared'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a29d2b9a5007319d1aa8"
  ]
}
```

### subnets

```json
{
  "kind": "metric",
  "formula": "Target Tenant ID \"1ee6b5b4fe8c45cfa16c3ecdbb8ee02b\" is predicated by \"networkrbacs.target_tenant IN ('1ee6b5b4fe8c45cfa16c3ecdbb8ee02b')\" | \"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.06889b02069293f63a68"
  ]
}
```

### tenant id

```json
{
  "kind": "metric",
  "formula": "Subnet ID \"012993ae-5d73-4aad-834b-e87a31e99d48\" is predicated by \"subnets.id IN ('012993ae-5d73-4aad-834b-e87a31e99d48')\" | Subnet ID \"0807c5b3-aa6c-4108-8884-7b4948a19178\" is predicated by \"subnets.id IN ('0807c5b3-aa6c-4108-8884-7b4948a19178')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5e8469e1dada581005d7"
  ]
}
```

### standard attribute tag relationship

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.69fba49061d916502c8a"
  ]
}
```

### tagged as 'ports'

```json
{
  "kind": "metric",
  "formula": "\"exclusion of shared networks\" is predicated by \"networks.id NOT IN (SELECT networkrbacs.object_id FROM networkrbacs WHERE networkrbacs.action = 'access_as_shared' AND (networkrbacs.target_tenant = '*' OR networkrbacs.target_tenant = '9f13bf11e06e4d81b44c8c3e62d4362b'))\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.3e8856c89f6f34b97116"
  ]
}
```


## 增量维护事件

