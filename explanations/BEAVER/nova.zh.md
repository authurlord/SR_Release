# BEAVER / nova — Schema 与业务口径解释

该数据库的存档目录包含 109 张表、1269 个物理列、811 条关系，以及 265 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。

## agent_builds

Stores metadata for different versions and builds of the agent software, including platform details, download links, and integrity hashes.

恢复表名: agent builds / builds / agent versions / software builds / agent releases / build artifacts
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| agent_builds.created_at | created at / creation date / created / build creation time / timestamp created | datetime | schema / agent_builds |
| agent_builds.updated_at | updated at / update date / last updated / modified time / last modified | datetime | schema / agent_builds |
| agent_builds.deleted_at | deleted at / deletion date / deleted / soft delete time / removal date | datetime | schema / agent_builds |
| agent_builds.id | id / identifier / build id / primary key / build number | int | schema / agent_builds |
| agent_builds.hypervisor | hypervisor / virtualization platform / vm platform / host type / virtual machine type | varchar(255) | schema / agent_builds |
| agent_builds.os | os / operating system / os type / platform os / system | varchar(255) | schema / agent_builds |
| agent_builds.architecture | architecture / cpu architecture / arch / system architecture / bitness | varchar(255) | schema / agent_builds |
| agent_builds.version | version / agent version / software version / release version / build version | varchar(255) | schema / agent_builds |
| agent_builds.url | url / download link / download url / file location / source link | varchar(255) | schema / agent_builds |
| agent_builds.md5hash | md5hash / checksum / md5 / integrity hash / file hash | varchar(255) | schema / agent_builds |
| agent_builds.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / agent_builds |

## aggregate_hosts

Maps individual compute hosts to their respective resource aggregates for grouping and scheduling purposes in the Nova cloud computing environment.

恢复表名: aggregate hosts / host aggregates / compute aggregates / nova aggregates / aggregate membership / host to aggregate mapping
SQL表别名: ah

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aggregate_hosts.created_at | created at / creation date / created timestamp / record created / inserted at | datetime | schema / aggregate_hosts |
| aggregate_hosts.updated_at | updated at / last updated / modification date / updated timestamp / last modified | datetime | schema / aggregate_hosts |
| aggregate_hosts.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / deleted timestamp | datetime | schema / aggregate_hosts |
| aggregate_hosts.id | id / identifier / primary key / record id / aggregate host id / unique identifier | int | schema / aggregate_hosts |
| aggregate_hosts.host | host / hostname / compute node name / server name / node host / host name | varchar(255) | nova_514 |
| aggregate_hosts.aggregate_id | aggregate id / aggregate identifier / resource aggregate id / group id / aggregate number / host aggregate id | int | nova_514 |
| aggregate_hosts.deleted | deleted / is deleted / soft delete flag / deletion status / active status / removed flag | int | schema / aggregate_hosts |

## aggregate_metadata

Stores key-value configuration parameters and metadata for Nova aggregates, including timestamps for creation, updates, and soft deletion.

恢复表名: aggregate metadata / metadata / key value pairs / configuration settings / nova metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aggregate_metadata.created_at | created at / creation date / created timestamp / date created / creation time | datetime | schema / aggregate_metadata |
| aggregate_metadata.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / aggregate_metadata |
| aggregate_metadata.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removal date | datetime | schema / aggregate_metadata |
| aggregate_metadata.id | id / identifier / primary key / record id / metadata id / unique identifier | int | schema / aggregate_metadata |
| aggregate_metadata.aggregate_id | aggregate id / aggregate identifier / host aggregate id / parent aggregate / aggregate reference | int | schema / aggregate_metadata |
| aggregate_metadata.key | key / parameter name / setting name / metadata key / configuration key / attribute name | varchar(255) | schema / aggregate_metadata |
| aggregate_metadata.value | value / parameter value / setting value / metadata value / configuration value / attribute value | varchar(255) | schema / aggregate_metadata |
| aggregate_metadata.deleted | deleted / deletion flag / is deleted / soft delete flag / deleted status | int | schema / aggregate_metadata |

## aggregates

Stores metadata and identifiers for aggregate entities, including creation, update, and deletion timestamps, along with unique identifiers and names.

恢复表名: aggregates / aggregate / aggregate records / aggregate data / aggregation / aggregations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| aggregates.created_at | created at / creation date / created date / creation timestamp / created timestamp / date created / time created | datetime | schema / aggregates |
| aggregates.updated_at | updated at / last updated date / update date / last modified date / updated timestamp / last modified timestamp / date updated | datetime | schema / aggregates |
| aggregates.deleted_at | deleted at / deletion date / deleted date / deletion timestamp / deleted timestamp / date deleted / time deleted | datetime | schema / aggregates |
| aggregates.id | id / identifier / primary key / record id / aggregate id / unique id / row id | int | schema / aggregates |
| aggregates.name | name / aggregate name / label / title / display name / entity name | varchar(255) | schema / aggregates |
| aggregates.deleted | deleted / deletion flag / is deleted / deleted status / soft delete flag / active status / deletion indicator | int | schema / aggregates |
| aggregates.uuid | uuid / unique universal identifier / guid / global id / uuid string / unique identifier / external id | varchar(36) | schema / aggregates |

## allocations

Tracks the specific amount of a resource class allocated to a consumer from a resource provider.

恢复表名: allocations / resource_allocations / allocation_records / resource_usage / allocation_details / resource_assignment
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| allocations.id | id / identifier / allocation_id / allocation_pk / record_id / unique_allocation_id | int | schema / allocations |
| allocations.resource_provider_id | resource provider id / resource provider identifier / provider_id / resource_provider / provider_reference / source_provider_id | int | schema / allocations |
| allocations.consumer_id | consumer id / consumer identifier / consumer / user_id / client_id / allocated_to / consumer_reference | varchar(36) | schema / allocations |
| allocations.resource_class_id | resource class id / resource class identifier / resource_class / resource_type_id / class_id / resource_category_id | int | schema / allocations |
| allocations.used | used / amount_used / allocated_amount / usage_quantity / resource_amount / consumed_units | int | schema / allocations |

## block_device_mapping

Stores the mapping between virtual machine instances and their attached block storage devices (volumes, images, or local disks), including device names, attachment status, and storage source details.

恢复表名: block device mapping / bdm / block device mappings / disk mappings / volume attachments / instance disks / block storage mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| block_device_mapping.created_at | created at / creation time / created date / attach time / mapping created / timestamp created | datetime | schema / block_device_mapping |
| block_device_mapping.updated_at | updated at / update time / last modified / modified date / updated timestamp / last update | datetime | schema / block_device_mapping |
| block_device_mapping.deleted_at | deleted at / deletion time / deleted date / detach time / removed at / soft delete time | datetime | schema / block_device_mapping |
| block_device_mapping.id | id / identifier / primary key / mapping id / bdm id / record id / unique identifier | int | schema / block_device_mapping |
| block_device_mapping.device_name | device name / device path / disk name / mount point / device identifier | varchar(255) | schema / block_device_mapping |
| block_device_mapping.delete_on_termination | delete on termination / delete on stop / ephemeral flag / auto delete / remove on shutdown / delete flag | tinyint(1) | schema / block_device_mapping |
| block_device_mapping.snapshot_id | snapshot id / snapshot identifier / snapshot uuid / source snapshot / snapshot reference | varchar(36) | schema / block_device_mapping |
| block_device_mapping.volume_id | volume id / volume identifier / volume uuid / block storage id / disk id / volume reference / storage id | varchar(36) | schema / block_device_mapping |
| block_device_mapping.volume_size | volume size / disk size / volume capacity / size in gb / storage size / disk capacity | int | schema / block_device_mapping |
| block_device_mapping.no_device | no device / number device / no device flag / unattached flag / device absent / null device | tinyint(1) | schema / block_device_mapping |
| block_device_mapping.connection_info | connection info / connection details / storage connection / mount info / driver info / connection json | text | schema / block_device_mapping |
| block_device_mapping.instance_uuid | instance uuid / instance id / vm id / server id / instance reference / compute instance id | varchar(36) | schema / block_device_mapping |
| block_device_mapping.deleted | deleted / soft delete id / deletion marker / deleted flag / removed id / soft delete | int | schema / block_device_mapping |
| block_device_mapping.source_type | source type / origin type / source kind / data source / from type / source category | varchar(255) | schema / block_device_mapping |
| block_device_mapping.destination_type | destination type / target type / destination kind / storage type / to type / destination category | varchar(255) | schema / block_device_mapping |
| block_device_mapping.guest_format | guest format / filesystem format / disk format / guest fs / file system / format type | varchar(255) | schema / block_device_mapping |
| block_device_mapping.device_type | device type / disk type / device kind / storage device type / type of device / device category | varchar(255) | schema / block_device_mapping |
| block_device_mapping.disk_bus | disk bus / bus type / virtual bus / storage bus / device bus / bus protocol | varchar(255) | schema / block_device_mapping |
| block_device_mapping.boot_index | boot index / boot order / boot priority / startup index / boot rank / boot sequence | int | schema / block_device_mapping |
| block_device_mapping.image_id | image id / image identifier / image uuid / source image / image reference / base image id | varchar(36) | schema / block_device_mapping |

## bw_usage_cache

Stores cached bandwidth usage statistics, including inbound and outbound traffic volumes and counters, associated with specific network interfaces or devices identified by MAC address or UUID.

恢复表名: bw usage cache / bandwidth usage cache / bandwidth cache / network usage cache / traffic usage cache / bw usage
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| bw_usage_cache.created_at | created at / creation time / record created / inserted at / creation date / created timestamp | datetime | schema / bw_usage_cache |
| bw_usage_cache.updated_at | updated at / last updated / modification time / updated timestamp / last modified / update date | datetime | schema / bw_usage_cache |
| bw_usage_cache.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / deleted timestamp / archived at | datetime | schema / bw_usage_cache |
| bw_usage_cache.id | id / identifier / primary key / record id / unique identifier / row id / cache id | int | schema / bw_usage_cache |
| bw_usage_cache.start_period | start period / period start / usage start time / beginning of period / start date / period start timestamp | datetime | schema / bw_usage_cache |
| bw_usage_cache.last_refreshed | last refreshed / last refresh time / data refresh timestamp / last synced / refresh date / last update time | datetime | schema / bw_usage_cache |
| bw_usage_cache.bw_in | bw in / inbound bandwidth / download volume / bytes in / input traffic / received data / bw inbound | bigint | schema / bw_usage_cache |
| bw_usage_cache.bw_out | bw out / outbound bandwidth / upload volume / bytes out / output traffic / sent data / bw outbound | bigint | schema / bw_usage_cache |
| bw_usage_cache.mac | mac / mac address / hardware address / physical address / device mac / network interface mac | varchar(255) | schema / bw_usage_cache |
| bw_usage_cache.uuid | uuid / unique universal identifier / device uuid / interface uuid / guid / unique id | varchar(36) | schema / bw_usage_cache |
| bw_usage_cache.last_ctr_in | last ctr in / last inbound counter / inbound packet counter / last bytes in counter / input counter / received counter | bigint | schema / bw_usage_cache |
| bw_usage_cache.last_ctr_out | last ctr out / last outbound counter / outbound packet counter / last bytes out counter / output counter / sent counter | bigint | schema / bw_usage_cache |
| bw_usage_cache.deleted | deleted / is deleted / soft delete flag / deletion status / active flag / removed flag | int | schema / bw_usage_cache |

## cells

Stores configuration and metadata for individual cells, including API and transport endpoints, weight parameters, and hierarchical status.

恢复表名: cells / cell / cell records / cell data / cell configurations / cell definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| cells.created_at | created at / creation date / created timestamp / date created / record created / initial timestamp | datetime | schema / cells |
| cells.updated_at | updated at / last updated / update timestamp / modified date / last modified / update time | datetime | schema / cells |
| cells.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removed date / archive date | datetime | schema / cells |
| cells.id | id / identifier / cell id / primary key / cell number / unique id | int | schema / cells |
| cells.api_url | api url / api endpoint / api address / api link / service url / api location | varchar(255) | schema / cells |
| cells.weight_offset | weight offset / offset value / weight bias / base weight / offset parameter | float | schema / cells |
| cells.weight_scale | weight scale / scale factor / weight multiplier / scaling factor / weight ratio | float | schema / cells |
| cells.name | name / cell name / label / title / display name / cell identifier | varchar(255) | schema / cells |
| cells.is_parent | is parent / parent flag / parent status / hierarchy level / root indicator | tinyint(1) | schema / cells |
| cells.deleted | deleted / deleted flag / is deleted / active status / removal flag / soft delete indicator | int | schema / cells |
| cells.transport_url | transport url / transport endpoint / transport address / transport link / data transport url / transport location | varchar(255) | schema / cells |

## certificates

Stores metadata for SSL/TLS certificates managed by the Nova service, including file locations, associated users and projects, and lifecycle timestamps.

恢复表名: certificates / certificate / ssl_certificates / tls_certificates / nova_certificates / ca_certificates / security_certificates
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| certificates.created_at | created at / creation_date / created / timestamp_created / date_added / inserted_at | datetime | schema / certificates |
| certificates.updated_at | updated at / last_updated / modified_at / update_timestamp / date_modified / last_change | datetime | schema / certificates |
| certificates.deleted_at | deleted at / deletion_date / deleted / removal_timestamp / date_deleted / soft_delete_time | datetime | schema / certificates |
| certificates.id | id / identifier / certificate_id / cert_id / primary_key / record_id / unique_id | int | schema / certificates |
| certificates.user_id | user id / user identifier / user / owner_id / user_uuid / account_id / tenant_user_id | varchar(255) | schema / certificates |
| certificates.project_id | project id / project identifier / project / tenant_id / project_uuid / account_project_id / service_project_id | varchar(255) | schema / certificates |
| certificates.file_name | file name / file_path / certificate_path / pem_file / cert_file_location / file_location | varchar(255) | schema / certificates |
| certificates.deleted | deleted / is_deleted / deletion_flag / active_status / soft_delete_flag / removed | int | schema / certificates |

## compute_nodes

Stores metadata, resource capacity, usage statistics, and hardware details for compute nodes (hypervisors) in the Nova cloud infrastructure.

恢复表名: compute nodes / compute node / hypervisors / hypervisor / compute hosts / compute host / nova compute nodes
SQL表别名: cn

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| compute_nodes.created_at | created at / creation time / created date / node creation timestamp / when node was created | datetime | schema / compute_nodes |
| compute_nodes.updated_at | updated at / last updated / update time / modification timestamp / last modified date | datetime | schema / compute_nodes |
| compute_nodes.deleted_at | deleted at / deletion time / deleted date / removal timestamp / when node was deleted | datetime | schema / compute_nodes |
| compute_nodes.id | id / identifier / node id / compute node id / primary key / record id | int | schema / compute_nodes |
| compute_nodes.service_id | service id / service identifier / associated service / compute service id / service reference | int | schema / compute_nodes |
| compute_nodes.vcpus | vcpus / total vcpus / cpu count / virtual cpus / total cpu capacity | int | schema / compute_nodes |
| compute_nodes.memory_mb | memory mb / total memory / ram size / memory capacity / total ram in mb | int | schema / compute_nodes |
| compute_nodes.local_gb | local gb / total disk / local storage / disk capacity / total local gb | int | schema / compute_nodes |
| compute_nodes.vcpus_used | vcpus used / used vcpus / cpu usage / allocated vcpus / vcpus in use | int | schema / compute_nodes |
| compute_nodes.memory_mb_used | memory mb used / used memory / ram usage / allocated ram / memory in use | int | schema / compute_nodes |
| compute_nodes.local_gb_used | local gb used / used disk / disk usage / allocated storage / local storage in use | int | schema / compute_nodes |
| compute_nodes.hypervisor_type | hypervisor type / hypervisor / virtualization type / vm type / hypervisor technology | text | nova_514 |
| compute_nodes.hypervisor_version | hypervisor version / hypervisor ver / vm version / hypervisor release / software version | int | schema / compute_nodes |
| compute_nodes.cpu_info | cpu info / cpu details / processor info / cpu model / hardware cpu specs | text | schema / compute_nodes |
| compute_nodes.disk_available_least | disk available least / min free disk / least available disk / minimum disk space / disk threshold | int | schema / compute_nodes |
| compute_nodes.free_ram_mb | free ram mb / available ram / free memory / unused ram / remaining memory | int | schema / compute_nodes |
| compute_nodes.free_disk_gb | free disk gb / available disk / free storage / unused disk / remaining disk space | int | schema / compute_nodes |
| compute_nodes.current_workload | current workload / workload / current load / io workload / node load | int | schema / compute_nodes |
| compute_nodes.running_vms | running vms / active vms / vm count / instances running / number of vms | int | schema / compute_nodes |
| compute_nodes.hypervisor_hostname | hypervisor hostname / hostname / full hostname / fqdn / node name | varchar(255) | schema / compute_nodes |
| compute_nodes.deleted | deleted / is deleted / deletion flag / soft delete / removed status | int | schema / compute_nodes |
| compute_nodes.host_ip | host ip / ip address / node ip / network address / host address | varchar(39) | schema / compute_nodes |
| compute_nodes.supported_instances | supported instances / supported archs / instance types / compatible instances / supported architectures | text | schema / compute_nodes |
| compute_nodes.pci_stats | pci stats / pci devices / pci info / pci device pool / pci statistics | text | schema / compute_nodes |
| compute_nodes.metrics | metrics / performance metrics / cpu metrics / monitoring data / node metrics | text | schema / compute_nodes |
| compute_nodes.extra_resources | extra resources / additional resources / custom resources / extra capacity / resource extensions | text | schema / compute_nodes |
| compute_nodes.stats | stats / node statistics / usage stats / instance stats / project stats | text | schema / compute_nodes |
| compute_nodes.numa_topology | numa topology / numa info / numa nodes / memory topology / numa configuration | text | schema / compute_nodes |
| compute_nodes.host | host / short hostname / node name / compute host / host identifier | varchar(255) | nova_514 |
| compute_nodes.ram_allocation_ratio | ram allocation ratio / ram ratio / memory overcommit / ram overcommit ratio / memory allocation factor | float | schema / compute_nodes |
| compute_nodes.cpu_allocation_ratio | cpu allocation ratio / cpu ratio / cpu overcommit / cpu overcommit ratio / cpu allocation factor | float | schema / compute_nodes |
| compute_nodes.uuid | uuid / node uuid / unique identifier / resource provider uuid / global id | varchar(36) | nova_514 |
| compute_nodes.disk_allocation_ratio | disk allocation ratio | float | schema / compute_nodes |

## console_pools

Stores configuration and connection details for remote console pools (e.g., VNC, SPICE) used to access virtual machine instances, including host addresses, credentials, and type.

恢复表名: console pools / console pool / vnc pools / spice pools / remote console pools / console connection pools
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| console_pools.created_at | created at / creation time / created date / record created / timestamp created | datetime | schema / console_pools |
| console_pools.updated_at | updated at / last updated / modification time / updated date / last modified | datetime | schema / console_pools |
| console_pools.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / removed at | datetime | schema / console_pools |
| console_pools.id | id / identifier / pool id / console pool identifier / primary key / record id | int | schema / console_pools |
| console_pools.address | address / pool address / connection address / ip address / endpoint address | varchar(39) | schema / console_pools |
| console_pools.username | username / user name / login user / console user / account name | varchar(255) | schema / console_pools |
| console_pools.password | password / pass / secret / login password / credential | varchar(255) | schema / console_pools |
| console_pools.console_type | console type / type / protocol / console protocol / vnc or spice | varchar(255) | schema / console_pools |
| console_pools.public_hostname | public hostname / public host / external hostname / public name / dns name | varchar(255) | schema / console_pools |
| console_pools.host | host / server host / internal host / machine host / node host | varchar(255) | schema / console_pools |
| console_pools.compute_host | compute host / compute node / hypervisor / compute server / host node | varchar(255) | schema / console_pools |
| console_pools.deleted | deleted / is deleted / soft delete flag / active status / removed flag | int | schema / console_pools |

## consoles

Stores metadata and connection details for console instances, including network ports, credentials, and pool associations.

恢复表名: consoles / console / console instances / web consoles / console servers / console nodes
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| consoles.created_at | created at / creation date / created / timestamp created / date created / creation time | datetime | schema / consoles |
| consoles.updated_at | updated at / last updated / update date / modified at / last modified / update timestamp | datetime | schema / consoles |
| consoles.deleted_at | deleted at / deletion date / deleted / soft delete time / removal date / archived at | datetime | schema / consoles |
| consoles.id | id / identifier / console id / primary key / record id / unique identifier / console identifier | int | schema / consoles |
| consoles.instance_name | instance name / name / console name / instance label / server name / display name | varchar(255) | schema / consoles |
| consoles.password | password / secret / credential / login password / auth password / access key | varchar(255) | schema / consoles |
| consoles.port | port / network port / connection port / service port / tcp port / port number | int | schema / consoles |
| consoles.pool_id | pool id / pool identifier / resource pool id / group id / cluster id / pool reference | int | schema / consoles |
| consoles.instance_uuid | instance uuid / uuid / unique universal identifier / global id / uuid string | varchar(36) | schema / consoles |
| consoles.deleted | deleted / is deleted / deletion flag / active status / soft delete flag / removed flag | int | schema / consoles |

## dns_domains

Stores metadata and configuration for DNS domains managed by the Nova system, including their scope, availability zone, and ownership.

恢复表名: dns domains / domain records / DNS zone list / domain registry / DNS entries
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| dns_domains.created_at | created at / creation date / created timestamp / date created / domain creation time | datetime | schema / dns_domains |
| dns_domains.updated_at | updated at / last updated / modification date / update timestamp / last modified time | datetime | schema / dns_domains |
| dns_domains.deleted_at | deleted at / deletion date / deleted timestamp / date deleted / removal time | datetime | schema / dns_domains |
| dns_domains.deleted | deleted / is deleted / deletion flag / soft delete status / active status | tinyint(1) | schema / dns_domains |
| dns_domains.domain | domain / domain name / DNS name / zone name / host name | varchar(255) | schema / dns_domains |
| dns_domains.scope | scope / domain scope / visibility scope / access scope / zone scope | varchar(255) | schema / dns_domains |
| dns_domains.availability_zone | availability zone / AZ / zone / availability zone name / region zone | varchar(255) | schema / dns_domains |
| dns_domains.project_id | project id / project identifier / project / tenant id / owner project | varchar(255) | schema / dns_domains |

## fixed_ips

Stores fixed IP address allocations within a network, tracking their status (allocated, leased, reserved), associated host, and instance binding.

恢复表名: fixed ips / fixed_ips / fixed ip / static ip / static ips / ip allocation / ip addresses / network fixed ips
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| fixed_ips.created_at | created at / creation time / created date / timestamp created / when created | datetime | schema / fixed_ips |
| fixed_ips.updated_at | updated at / last updated / modification time / updated date / last modified | datetime | schema / fixed_ips |
| fixed_ips.deleted_at | deleted at / deletion time / deleted date / when deleted / soft delete timestamp | datetime | schema / fixed_ips |
| fixed_ips.id | id / identifier / fixed ip id / ip id / primary key / record id | int | schema / fixed_ips |
| fixed_ips.address | address / ip address / fixed ip address / ip / ipv4 address / cidr | varchar(39) | schema / fixed_ips |
| fixed_ips.network_id | network id / network identifier / network / associated network / subnet network id | int | schema / fixed_ips |
| fixed_ips.allocated | allocated / is allocated / allocation status / allocated flag / ip allocated | tinyint(1) | schema / fixed_ips |
| fixed_ips.leased | leased / is leased / lease status / leased flag / ip leased | tinyint(1) | schema / fixed_ips |
| fixed_ips.reserved | reserved / is reserved / reservation status / reserved flag / ip reserved | tinyint(1) | schema / fixed_ips |
| fixed_ips.virtual_interface_id | virtual interface id / virtual interface identifier / vif id / interface id / virtual interface / port id | int | schema / fixed_ips |
| fixed_ips.host | host / host name / compute host / node / server host | varchar(255) | schema / fixed_ips |
| fixed_ips.instance_uuid | instance uuid / instance id / vm id / server uuid / associated instance | varchar(36) | schema / fixed_ips |
| fixed_ips.deleted | deleted / is deleted / soft delete flag / deletion status / active status | int | schema / fixed_ips |

## floating_ips

Stores metadata for floating IP addresses (public IPs) allocated to instances, including their association with fixed IPs, projects, and physical hosts.

恢复表名: floating ips / floating_ips / floating ip / public ips / external ips / elastic ips / eips / public addresses
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| floating_ips.created_at | created at / created_at / creation time / created date / timestamp created / when created | datetime | schema / floating_ips |
| floating_ips.updated_at | updated at / updated_at / last updated / modification time / last modified / update timestamp | datetime | schema / floating_ips |
| floating_ips.deleted_at | deleted at / deleted_at / deletion time / deleted date / soft delete timestamp / when deleted | datetime | schema / floating_ips |
| floating_ips.id | id / identifier / floating ip id / primary key / record id / unique identifier | int | schema / floating_ips |
| floating_ips.address | address / floating ip address / public ip / external ip / ip address / public address | varchar(39) | schema / floating_ips |
| floating_ips.fixed_ip_id | fixed ip id / fixed ip identifier / fixed_ip_id / private ip id / internal ip id / associated fixed ip / linked private ip | int | schema / floating_ips |
| floating_ips.project_id | project id / project identifier / project_id / tenant id / project / tenant / owner project / account id | varchar(255) | schema / floating_ips |
| floating_ips.host | host / compute host / hypervisor / physical host / node / server host | varchar(255) | schema / floating_ips |
| floating_ips.auto_assigned | auto assigned / auto_assigned / automatic assignment / auto assign / manually assigned / assignment type | tinyint(1) | schema / floating_ips |
| floating_ips.pool | pool / ip pool / address pool / network pool / floating ip pool | varchar(255) | schema / floating_ips |
| floating_ips.interface | interface / network interface / nic / port / ethernet interface | varchar(255) | schema / floating_ips |
| floating_ips.deleted | deleted / is deleted / soft delete flag / deletion status / active status | int | schema / floating_ips |

## instance_actions

Records the lifecycle actions and operations performed on compute instances, including the type of action, associated user and project, and timing details.

恢复表名: instance actions / instance action log / instance operations / instance events / compute instance actions / instance history
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_actions.created_at | created at / creation time / record created / timestamp created / date created | datetime | schema / instance_actions |
| instance_actions.updated_at | updated at / last updated / modification time / update timestamp / date updated | datetime | schema / instance_actions |
| instance_actions.deleted_at | deleted at / deletion time / soft delete timestamp / date deleted / removed at | datetime | schema / instance_actions |
| instance_actions.id | id / identifier / action id / primary key / record id / unique identifier | int | schema / instance_actions |
| instance_actions.action | action / operation type / action type / instance operation / event type | varchar(255) | schema / instance_actions |
| instance_actions.instance_uuid | instance uuid / instance id / server uuid / compute instance identifier / vm id | varchar(36) | schema / instance_actions |
| instance_actions.request_id | request id / request identifier / api request id / trace id / correlation id | varchar(255) | schema / instance_actions |
| instance_actions.user_id | user id / user identifier / actor id / initiating user / user uuid | varchar(255) | schema / instance_actions |
| instance_actions.project_id | project id / project identifier / tenant id / project uuid / account id | varchar(255) | schema / instance_actions |
| instance_actions.start_time | start time / action start / operation start time / begin time / start timestamp | datetime | schema / instance_actions |
| instance_actions.finish_time | finish time / action end / operation finish time / completion time / end timestamp | datetime | schema / instance_actions |
| instance_actions.message | message / action message / description / status message / details | varchar(255) | schema / instance_actions |
| instance_actions.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / instance_actions |

## instance_actions_events

Stores individual event records associated with instance actions, tracking the start, finish, result, and details of operations like scheduling or running instances.

恢复表名: instance actions events / instance action events / instance events / action events / instance action logs / compute instance events / instance operation events
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_actions_events.created_at | created at / creation time / record created / event created / timestamp created / inserted at | datetime | schema / instance_actions_events |
| instance_actions_events.updated_at | updated at / last updated / modification time / event updated / last modified / update timestamp | datetime | schema / instance_actions_events |
| instance_actions_events.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / deleted when / purge time | datetime | schema / instance_actions_events |
| instance_actions_events.id | id / identifier / event id / primary key / unique identifier / record id / event identifier | int | schema / instance_actions_events |
| instance_actions_events.event | event / event type / action name / operation type / event name / action event | varchar(255) | schema / instance_actions_events |
| instance_actions_events.action_id | action id / action identifier / parent action id / related action / instance action id / foreign key to action | int | schema / instance_actions_events |
| instance_actions_events.start_time | start time / event start / begin time / start timestamp / operation start / initiated at | datetime | schema / instance_actions_events |
| instance_actions_events.finish_time | finish time / event end / completion time / end timestamp / finish timestamp / completed at | datetime | schema / instance_actions_events |
| instance_actions_events.result | result / event result / status / outcome / success status / action result | varchar(255) | schema / instance_actions_events |
| instance_actions_events.traceback | traceback / error traceback / stack trace / exception details / error log / failure details | text | schema / instance_actions_events |
| instance_actions_events.deleted | deleted / is deleted / soft delete flag / deletion status / active flag / removed flag | int | schema / instance_actions_events |
| instance_actions_events.host | host / host name / server host / compute host / node name / execution host | varchar(255) | schema / instance_actions_events |
| instance_actions_events.details | details / event details / additional info / metadata / description / event description | text | schema / instance_actions_events |

## instance_extra

Stores extended, serialized, or supplementary attributes for OpenStack Nova compute instances, including flavor details, NUMA topology, PCI requests, and migration context, linked to the main instances table via UUID.

恢复表名: instance extra / instance extras / vm extra / vm extras / instance metadata extra / instance additional info / instance extended attributes
SQL表别名: e, ie, ie2, ie3, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_extra.created_at | created at / creation time / created timestamp / record created date / instance extra created at / creation date | datetime | nova_47, nova_11, nova_100, nova_1049, nova_152 |
| instance_extra.updated_at | updated at / update time / last updated timestamp / modified date / instance extra updated at / last modification time | datetime | schema / instance_extra |
| instance_extra.deleted_at | deleted at / deletion time / deleted timestamp / soft delete date / instance extra deleted at / removal time | datetime | schema / instance_extra |
| instance_extra.deleted | deleted / deletion flag / is deleted / soft delete indicator / deleted status / instance extra deleted flag | int | nova_47, nova_11 |
| instance_extra.id | id / identifier / primary key / instance extra id / record id / unique identifier / instance extra primary key | int | nova_47, nova_11, nova_989, nova_100, nova_1042, nova_1049, nova_125, nova_129 |
| instance_extra.instance_uuid | instance uuid / vm uuid / server uuid / instance identifier / linked instance uuid | varchar(36) | nova_47, nova_286, nova_240, nova_11, nova_989, nova_100, nova_1042, nova_1044 |
| instance_extra.numa_topology | numa topology / numa configuration / numa json / numa layout / instance numa topology | text | nova_47, nova_989, nova_1044 |
| instance_extra.pci_requests | pci requests / pci devices / pci configuration / pci json / instance pci requests | text | nova_240 |
| instance_extra.flavor | flavor / instance flavor / flavor json / flavor details / vm flavor | text | nova_286, nova_989, nova_1042, nova_1044, nova_125, nova_129 |
| instance_extra.vcpu_model | vcpu model / cpu model / virtual cpu model / vcpu json / cpu topology | text | schema / instance_extra |
| instance_extra.migration_context | migration context / migration info / migration json / live migration context / instance migration context | text | nova_286 |

## instance_faults

Stores records of faults or errors encountered by compute instances, including the specific host, error code, and timestamps.

恢复表名: instance faults / faults / instance errors / compute faults / vm faults / instance issues
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_faults.created_at | created at / creation time / fault creation date / when fault occurred / record created / timestamp | datetime | schema / instance_faults |
| instance_faults.updated_at | updated at / last update time / modification date / when updated / last modified / update timestamp | datetime | schema / instance_faults |
| instance_faults.deleted_at | deleted at / deletion time / when deleted / soft delete timestamp / removal date / deleted date | datetime | schema / instance_faults |
| instance_faults.id | id / identifier / fault id / primary key / record id / unique identifier / fault number | int | schema / instance_faults |
| instance_faults.instance_uuid | instance uuid / instance id / vm uuid / server uuid / compute instance identifier / instance unique id | varchar(36) | schema / instance_faults |
| instance_faults.code | code / error code / fault code / status code / http code / error number | int | schema / instance_faults |
| instance_faults.message | message / error message / fault message / description / short description / message text | varchar(255) | schema / instance_faults |
| instance_faults.details | details / fault details / error details / long description / detailed message / full description | text | schema / instance_faults |
| instance_faults.host | host / host name / compute node / server name / physical host / node name | varchar(255) | schema / instance_faults |
| instance_faults.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / instance_faults |

## instance_group_member

Tracks the membership of individual instances within instance groups, including creation, update, and deletion timestamps and status.

恢复表名: instance group member / instance group membership / group member / instance in group / group instance mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_group_member.created_at | created at / creation time / created date / timestamp created / when created / record created | datetime | schema / instance_group_member |
| instance_group_member.updated_at | updated at / last updated / update time / modified date / last modified / record updated | datetime | schema / instance_group_member |
| instance_group_member.deleted_at | deleted at / deletion time / deleted date / removed at / when deleted / soft delete timestamp | datetime | schema / instance_group_member |
| instance_group_member.deleted | deleted / deletion flag / is deleted / soft delete status / deleted status / removal indicator | int | schema / instance_group_member |
| instance_group_member.id | id / identifier / primary key / record id / membership id / unique identifier / row id | int | schema / instance_group_member |
| instance_group_member.instance_id | instance id / instance identifier / instance uuid / vm id / server id / instance reference | varchar(255) | schema / instance_group_member |
| instance_group_member.group_id | group id / group identifier / instance group id / parent group id / group reference / group number | int | schema / instance_group_member |

## instance_group_policy

Stores scheduling policies (such as affinity or anti-affinity) applied to instance groups to control how instances are placed or distributed.

恢复表名: instance group policy / igp / group policy / instance policy / affinity policy / anti-affinity policy / placement policy
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_group_policy.created_at | created at / creation date / created timestamp / policy creation time / date created / when created | datetime | schema / instance_group_policy |
| instance_group_policy.updated_at | updated at / last updated / update timestamp / modification date / last modified / when updated | datetime | schema / instance_group_policy |
| instance_group_policy.deleted_at | deleted at / deletion date / deleted timestamp / removal time / when deleted / soft delete time | datetime | schema / instance_group_policy |
| instance_group_policy.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / instance_group_policy |
| instance_group_policy.id | id / identifier / policy id / policy identifier / primary key / record id / unique id | int | schema / instance_group_policy |
| instance_group_policy.policy | policy / policy type / scheduling policy / affinity type / placement rule / policy name | varchar(255) | schema / instance_group_policy |
| instance_group_policy.group_id | group id / group identifier / instance group id / associated group / ig id / parent group id | int | schema / instance_group_policy |

## instance_groups

Stores metadata for logical groupings of compute instances, including ownership, project association, and lifecycle status.

恢复表名: instance groups / instance group / ig / groups / compute groups / server groups
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_groups.created_at | created at / creation date / created timestamp / start date / creation time / when created | datetime | schema / instance_groups |
| instance_groups.updated_at | updated at / last updated / modification date / update timestamp / last modified / change date | datetime | schema / instance_groups |
| instance_groups.deleted_at | deleted at / deletion date / removed at / soft delete time / archived date / when deleted | datetime | schema / instance_groups |
| instance_groups.deleted | deleted / deletion flag / is deleted / soft delete status / active status / removal indicator | int | schema / instance_groups |
| instance_groups.id | id / identifier / instance group id / primary key / group id / ig id / record id | int | schema / instance_groups |
| instance_groups.user_id | user id / user identifier / owner id / account id / creator id / user uuid | varchar(255) | schema / instance_groups |
| instance_groups.project_id | project id / project identifier / project uuid / associated project / project ref / project key | varchar(255) | schema / instance_groups |
| instance_groups.uuid | uuid / unique identifier / group uuid / external id / universal id / ig uuid | varchar(36) | schema / instance_groups |
| instance_groups.name | name / instance group name / group name / label / title / display name | varchar(255) | schema / instance_groups |

## instance_id_mappings

Stores mappings between internal instance identifiers (IDs) and their corresponding UUIDs, including lifecycle timestamps and deletion status.

恢复表名: instance id mappings / instance identifier mappings / instance mappings / id mappings / instance uuid mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_id_mappings.created_at | created at / creation date / created timestamp / record created / instance creation time / mapping created | datetime | schema / instance_id_mappings |
| instance_id_mappings.updated_at | updated at / update date / last updated / modified timestamp / record updated / instance update time | datetime | schema / instance_id_mappings |
| instance_id_mappings.deleted_at | deleted at / deletion date / deleted timestamp / record deleted / instance deletion time / soft delete time | datetime | schema / instance_id_mappings |
| instance_id_mappings.id | id / identifier / primary key / record id / mapping id / instance mapping identifier / internal id | int | schema / instance_id_mappings |
| instance_id_mappings.uuid | uuid / instance uuid / unique identifier / instance guid / universal unique identifier / instance external id | varchar(36) | schema / instance_id_mappings |
| instance_id_mappings.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / record status | int | schema / instance_id_mappings |

## instance_info_caches

Stores cached network configuration details (JSON) and metadata for OpenStack instances, linked by instance UUID.

恢复表名: instance info caches / instance info cache / info cache / network info cache / instance network cache / nova instance info cache
SQL表别名: c, ic, ic2, iic, iic2, nic, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_info_caches.created_at | created at / creation time / created date / record created / cache creation timestamp | datetime | schema / instance_info_caches |
| instance_info_caches.updated_at | updated at / last updated / update time / modified date / cache update timestamp / last modified | datetime | nova_50, nova_1035, nova_141 |
| instance_info_caches.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / record removed at | datetime | schema / instance_info_caches |
| instance_info_caches.id | id / identifier / cache id / record id / primary key / info cache identifier / cache record id | int | nova_50, nova_6, nova_105, nova_106, nova_131, nova_15, nova_22, nova_266 |
| instance_info_caches.network_info | network info / network configuration / cached network data / network json / instance network details / ovs interface info | text | nova_50, nova_6, nova_0, nova_1035, nova_105, nova_106, nova_131, nova_15 |
| instance_info_caches.instance_uuid | instance uuid / instance id / vm uuid / server uuid / linked instance / instance identifier | varchar(36) | nova_50, nova_6, nova_0, nova_1035, nova_105, nova_106, nova_131, nova_141 |
| instance_info_caches.deleted | deleted / is deleted / deletion flag / soft delete status / active status / deleted flag | int | nova_50, nova_6, nova_0, nova_141, nova_22, nova_31 |

## instance_metadata

Stores key-value pairs of metadata associated with specific instances, including system roles, image versions, and other configuration details.

恢复表名: instance metadata / instance properties / instance attributes / instance config / instance settings / instance key-value store
SQL表别名: im

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_metadata.created_at | created at / creation date / created timestamp / record created / start date / inserted at | datetime | schema / instance_metadata |
| instance_metadata.updated_at | updated at / last updated / modification date / updated timestamp / last modified / change date | datetime | schema / instance_metadata |
| instance_metadata.deleted_at | deleted at / deletion date / removed at / deleted timestamp / soft delete time / archived at | datetime | schema / instance_metadata |
| instance_metadata.id | id / identifier / primary key / record id / metadata id / unique identifier / row id | int | schema / instance_metadata |
| instance_metadata.key | key / metadata key / property name / attribute name / config key / field name / parameter name | varchar(255) | schema / instance_metadata |
| instance_metadata.value | value / metadata value / property value / attribute value / config value / data / content | varchar(255) | schema / instance_metadata |
| instance_metadata.instance_uuid | instance uuid / instance id / instance unique id / instance identifier / uuid / instance guid | varchar(36) | schema / instance_metadata |
| instance_metadata.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / removed flag | int | schema / instance_metadata |

## instance_system_metadata

Stores key-value pairs of system metadata associated with compute instances, such as image properties and instance type details.

恢复表名: instance system metadata / system metadata / instance metadata / vm metadata / metadata / instance properties
SQL表别名: ism, ism2, m, msm, s, sm, t0, t2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_system_metadata.created_at | created at / creation time / created date / timestamp created / record created / metadata created | datetime | schema / instance_system_metadata |
| instance_system_metadata.updated_at | updated at / update time / last updated / modified date / timestamp updated / record updated | datetime | schema / instance_system_metadata |
| instance_system_metadata.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / removed at / record deleted | datetime | schema / instance_system_metadata |
| instance_system_metadata.id | id / identifier / metadata id / primary key / record id / system metadata id / entry id | int | nova_613, nova_121, nova_205 |
| instance_system_metadata.instance_uuid | instance uuid / instance id / vm uuid / server uuid / instance identifier / linked instance | varchar(36) | nova_613, nova_106, nova_121, nova_13, nova_134, nova_167, nova_189, nova_205 |
| instance_system_metadata.key | key / metadata key / property name / attribute key / system metadata key / field name | varchar(255) | nova_613, nova_106, nova_121, nova_13, nova_134, nova_167, nova_189, nova_205 |
| instance_system_metadata.value | value / metadata value / property value / attribute value / system metadata value / field value | varchar(255) | nova_613, nova_106, nova_121, nova_13, nova_134, nova_167, nova_189, nova_205 |
| instance_system_metadata.deleted | deleted / is deleted / soft delete flag / deletion status / active flag / record status | int | nova_613, nova_106, nova_13, nova_134, nova_167, nova_189, nova_213, nova_216 |

## instance_type_extra_specs

Stores additional key-value specifications and attributes associated with specific instance types (flavors) in the Nova cloud computing platform.

恢复表名: instance type extra specs / extra specs / instance type specifications / flavor extra specs / instance type attributes / custom instance type properties
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_type_extra_specs.created_at | created at / creation time / created date / record creation timestamp / when created / inserted at | datetime | schema / instance_type_extra_specs |
| instance_type_extra_specs.updated_at | updated at / update time / last modified date / updated timestamp / last updated / modification time | datetime | schema / instance_type_extra_specs |
| instance_type_extra_specs.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / when deleted / removal time | datetime | schema / instance_type_extra_specs |
| instance_type_extra_specs.id | id / identifier / primary key / spec id / record id / unique identifier / extra spec id | int | schema / instance_type_extra_specs |
| instance_type_extra_specs.instance_type_id | instance type id / instance type identifier / flavor id / linked flavor id / parent instance type | int | schema / instance_type_extra_specs |
| instance_type_extra_specs.key | key / spec key / attribute name / property name / specification key / extra spec name | varchar(255) | schema / instance_type_extra_specs |
| instance_type_extra_specs.value | value / spec value / attribute value / property value / specification value / extra spec data | varchar(255) | schema / instance_type_extra_specs |
| instance_type_extra_specs.deleted | deleted / deleted flag / soft delete flag / is deleted / deletion status / active status | int | schema / instance_type_extra_specs |

## instance_type_projects

Junction table linking instance types to projects, tracking which instance types are available or assigned to specific projects with soft-delete support.

恢复表名: instance type projects / project instance types / instance type project mapping / project instance type associations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_type_projects.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / instance_type_projects |
| instance_type_projects.updated_at | updated at / last updated / modification date / updated timestamp / last modified | datetime | schema / instance_type_projects |
| instance_type_projects.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removal date | datetime | schema / instance_type_projects |
| instance_type_projects.id | id / identifier / primary key / record id / association id / unique identifier | int | schema / instance_type_projects |
| instance_type_projects.instance_type_id | instance type id / instance type identifier / instance type / type id / instance type reference | int | schema / instance_type_projects |
| instance_type_projects.project_id | project id / project identifier / project / project uuid / project reference | varchar(255) | schema / instance_type_projects |
| instance_type_projects.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / instance_type_projects |

## instance_types

Stores the definitions and specifications for different types of virtual machine instances (flavors), including resource allocations like memory, CPUs, and storage, as well as their availability status.

恢复表名: instance types / flavors / vm flavors / instance flavors / compute flavors / server types / instance specifications
SQL表别名: it

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instance_types.created_at | created at / creation date / created timestamp / date created / instance type creation time | datetime | schema / instance_types |
| instance_types.updated_at | updated at / last updated / modification date / update timestamp / last modified time | datetime | schema / instance_types |
| instance_types.deleted_at | deleted at / deletion date / deleted timestamp / date deleted / removal time | datetime | schema / instance_types |
| instance_types.name | name / instance type name / flavor name / type identifier / flavor label | varchar(255) | schema / instance_types |
| instance_types.id | id / identifier / instance type id / flavor id / primary key / type identifier | int | schema / instance_types |
| instance_types.memory_mb | memory mb / memory / ram / memory in mb / ram size / memory allocation | int | schema / instance_types |
| instance_types.vcpus | vcpus / cpu count / virtual cpus / number of cpus / cpu cores / vcpu count | int | schema / instance_types |
| instance_types.swap | swap / swap space / swap size / swap memory / swap allocation | int | schema / instance_types |
| instance_types.vcpu_weight | vcpu weight / cpu weight / vcpu priority / cpu scheduling weight | int | schema / instance_types |
| instance_types.flavorid | flavorid / flavor id / external flavor id / flavor reference / flavor identifier | varchar(255) | schema / instance_types |
| instance_types.rxtx_factor | rxtx factor / rx tx factor / network factor / rxtx multiplier / network bandwidth factor | float | schema / instance_types |
| instance_types.root_gb | root gb / root disk size / root volume / root storage / root disk gb / system disk size | int | schema / instance_types |
| instance_types.ephemeral_gb | ephemeral gb / ephemeral disk / local storage / ephemeral storage / ephemeral volume / local disk size | int | schema / instance_types |
| instance_types.disabled | disabled / is disabled / disabled status / enabled / active status / flavor disabled | tinyint(1) | nova_431 |
| instance_types.is_public | is public / public / public status / visibility / is public flag / publicly available | tinyint(1) | schema / instance_types |
| instance_types.deleted | deleted / is deleted / deleted status / soft delete flag / removed / active status | int | schema / instance_types |

## instances

Stores core metadata, configuration, state, and lifecycle information for virtual machine instances in the Nova compute service.

恢复表名: instances / virtual machines / VMs / servers / compute instances / nova instances / instance records
SQL表别名: i, i2, i3, mi, t0, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| instances.created_at | created at / creation time / created date / instance creation timestamp / start date | datetime | nova_727 |
| instances.updated_at | updated at / last updated / modification time / update timestamp / last modified date | datetime | schema / instances |
| instances.deleted_at | deleted at / deletion time / deleted date / removal timestamp / soft delete time | datetime | schema / instances |
| instances.id | id / identifier / instance ID / primary key / record ID / internal ID | int | nova_857, nova_995, nova_586, nova_15, nova_266, nova_6, nova_613, nova_624 |
| instances.internal_id | internal id / internal identifier / system ID / backend ID | int | schema / instances |
| instances.user_id | user id / user identifier / owner ID / account ID / tenant user ID | varchar(255) | nova_857, nova_15, nova_266, nova_6, nova_613, nova_624, nova_678 |
| instances.project_id | project id / project identifier / tenant ID / project UUID / account project | varchar(255) | nova_857, nova_727, nova_15, nova_266, nova_6, nova_613, nova_624, nova_678 |
| instances.image_ref | image ref / image reference / image ID / base image / source image | varchar(255) | schema / instances |
| instances.kernel_id | kernel id / kernel identifier / kernel reference / boot kernel | varchar(255) | schema / instances |
| instances.ramdisk_id | ramdisk id / ramdisk identifier / ramdisk reference / initramfs ID | varchar(255) | schema / instances |
| instances.launch_index | launch index / launch order / batch index / sequence number | int | schema / instances |
| instances.key_name | key name / SSH key name / key pair name / access key name | varchar(255) | nova_586 |
| instances.key_data | key data / public key data / key fingerprint / SSH public key | text | schema / instances |
| instances.power_state | power state / power status / on/off state / power mode | int | nova_857, nova_995, nova_586, nova_15, nova_266, nova_6, nova_613, nova_624 |
| instances.vm_state | vm state / VM status / instance state / lifecycle state / current state | varchar(255) | nova_857, nova_995, nova_586, nova_15, nova_266, nova_6, nova_613, nova_624 |
| instances.memory_mb | memory mb / RAM size / memory size / memory in MB / virtual memory | int | nova_857, nova_727, nova_995, nova_586, nova_663, nova_757, nova_15, nova_266 |
| instances.vcpus | vcpus / CPU count / virtual CPUs / core count / processor count | int | nova_857, nova_727, nova_995, nova_586, nova_663, nova_15, nova_266, nova_6 |
| instances.hostname | hostname / host name / internal hostname / VM hostname | varchar(255) | nova_857, nova_15, nova_266, nova_6, nova_624, nova_678 |
| instances.host | host / compute host / physical host / hypervisor / node name | varchar(255) | nova_727, nova_995, nova_757 |
| instances.user_data | user data / cloud-init data / user script / bootstrap data | text | schema / instances |
| instances.reservation_id | reservation id / reservation identifier / resource reservation / quota reservation | varchar(255) | schema / instances |
| instances.scheduled_at | scheduled at / scheduling time / schedule timestamp / placement time | datetime | schema / instances |
| instances.launched_at | launched at / launch time / start time / boot time / creation completion time | datetime | nova_727 |
| instances.terminated_at | terminated at / termination time / stop time / end time / shutdown time | datetime | schema / instances |
| instances.display_name | display name / instance name / VM name / server name / label | varchar(255) | nova_857, nova_727, nova_995, nova_586, nova_663, nova_757, nova_15, nova_266 |
| instances.display_description | display description / instance description / VM description / notes / details | varchar(255) | schema / instances |
| instances.availability_zone | availability zone / AZ / zone / availability region / data center zone | varchar(255) | nova_857, nova_995, nova_586, nova_663, nova_15, nova_266, nova_6, nova_613 |
| instances.locked | locked / lock status / is locked / maintenance lock | tinyint(1) | schema / instances |
| instances.os_type | os type / operating system / OS / guest OS / platform | varchar(255) | schema / instances |
| instances.launched_on | launched on / launch host / initial host / origin host | text | schema / instances |
| instances.instance_type_id | instance type id / instance type identifier / flavor ID / instance type / specification ID / size ID | int | nova_757 |
| instances.vm_mode | vm mode / virtualization mode / VM type / execution mode | varchar(255) | schema / instances |
| instances.uuid | uuid / instance UUID / unique identifier / global ID / API ID | varchar(36) | nova_857, nova_727, nova_995, nova_586, nova_663, nova_757, nova_15, nova_266 |
| instances.architecture | architecture / CPU architecture / arch / hardware architecture | varchar(255) | schema / instances |
| instances.root_device_name | root device name / root disk device / boot device / root partition | varchar(255) | schema / instances |
| instances.access_ip_v4 | access ip v4 | varchar(39) | schema / instances |
| instances.access_ip_v6 | access ip v6 | varchar(39) | schema / instances |
| instances.config_drive | config drive | varchar(255) | nova_663 |
| instances.task_state | task state | varchar(255) | schema / instances |
| instances.default_ephemeral_device | default ephemeral device | varchar(255) | schema / instances |
| instances.default_swap_device | default swap device | varchar(255) | schema / instances |
| instances.progress | progress | int | schema / instances |
| instances.auto_disk_config | auto disk config | tinyint(1) | schema / instances |
| instances.shutdown_terminate | shutdown terminate | tinyint(1) | schema / instances |
| instances.disable_terminate | disable terminate | tinyint(1) | schema / instances |
| instances.root_gb | root gb | int | nova_995 |
| instances.ephemeral_gb | ephemeral gb | int | schema / instances |
| instances.cell_name | cell name | varchar(255) | schema / instances |
| instances.node | node | varchar(255) | schema / instances |
| instances.deleted | deleted | int | nova_857, nova_727, nova_995, nova_586, nova_663, nova_613 |
| instances.locked_by | locked by | enum('owner','admin') | schema / instances |
| instances.cleaned | cleaned | int | schema / instances |
| instances.ephemeral_key_uuid | ephemeral key uuid | varchar(36) | schema / instances |

## inventories

Tracks the available, reserved, and total capacity of specific resource classes provided by resource providers, including allocation constraints and step sizes.

恢复表名: inventories / inventory / resource_inventory / resource_pool / capacity_inventory / resource_allocation / stock / resource_stock
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| inventories.id | id / identifier / inventory_id / record_id / primary_key / inventory_record | int | schema / inventories |
| inventories.resource_provider_id | resource provider id / resource provider identifier / provider_id / resource_provider / provider / host_id / node_id / supplier_id | int | schema / inventories |
| inventories.resource_class_id | resource class id / resource class identifier / resource_class / class_id / resource_type / resource_category / flavor_id / resource_kind | int | schema / inventories |
| inventories.total | total / total_capacity / total_amount / total_units / max_capacity / full_capacity / total_stock | int | schema / inventories |
| inventories.reserved | reserved / reserved_amount / reserved_units / allocated / used_capacity / reserved_stock / committed | int | schema / inventories |
| inventories.min_unit | min unit / minimum unit / minimum_unit / min_capacity / minimum_allocation / lower_bound / min_size | int | schema / inventories |
| inventories.max_unit | max unit / maximum unit / maximum_unit / max_capacity / maximum_allocation / upper_bound / max_size | int | schema / inventories |
| inventories.step_size | step size / increment / step / allocation_step / granularity / step_increment | int | schema / inventories |
| inventories.allocation_ratio | allocation ratio / ratio / allocation_factor / overcommit_ratio / commit_ratio / allocation_percentage | float | schema / inventories |

## key_pairs

Stores SSH and X.509 key pair records associated with users, including public key data, fingerprints, and lifecycle timestamps.

恢复表名: key pairs / ssh_keys / public_keys / key_pair_records / user_keys / authentication_keys / crypto_keys
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| key_pairs.created_at | created at / creation_date / created / start_date / key_creation_time / timestamp_created | datetime | schema / key_pairs |
| key_pairs.updated_at | updated at / last_updated / modified_at / update_time / last_modified / revision_date | datetime | schema / key_pairs |
| key_pairs.deleted_at | deleted at / deletion_date / removed_at / deleted / expiration_date / removal_time | datetime | schema / key_pairs |
| key_pairs.id | id / identifier / key_id / primary_key / record_id / key_pair_id | int | schema / key_pairs |
| key_pairs.name | name / key_name / label / title / key_alias / display_name | varchar(255) | schema / key_pairs |
| key_pairs.user_id | user id / user identifier / owner_id / account_id / user_identifier / parent_user / associated_user | varchar(255) | schema / key_pairs |
| key_pairs.fingerprint | fingerprint / key_fingerprint / hash / digest / key_hash / fingerprint_hash | varchar(255) | schema / key_pairs |
| key_pairs.public_key | public key / pub_key / key_data / public_key_data / key_content / ssh_public_key | text | schema / key_pairs |
| key_pairs.deleted | deleted / is_deleted / deletion_flag / status / active_status / soft_delete_flag | int | schema / key_pairs |
| key_pairs.type | type / key_type / protocol / key_protocol / algorithm_type / key_category | enum('ssh','x509') | schema / key_pairs |

## migrate_version

Tracks the current version of the database schema migrations applied to the Nova database.

恢复表名: migrate version / database migration version / schema version / migration state / alembic version / db migration history
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| migrate_version.repository_id | repository id / repository identifier / migration repository id / repo id / schema repository identifier / migration source id | varchar(250) | schema / migrate_version |
| migrate_version.repository_path | repository path / migration path / schema directory / migration file location / alembic directory / db migration folder | text | schema / migrate_version |
| migrate_version.version | version / schema version number / migration version / current db version / alembic version / revision number | int | schema / migrate_version |

## migrations

Tracks the history and details of virtual machine instance migrations, including source/destination hosts, memory/disk transfer statistics, and migration status.

恢复表名: migrations / migration records / instance migrations / vm migrations / live migration logs / compute migrations
SQL表别名: m, m2, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| migrations.created_at | created at / migration created date / start time / creation timestamp / when migration started | datetime | nova_170 |
| migrations.updated_at | updated at / migration updated date / last modified time / update timestamp / when migration was last changed | datetime | schema / migrations |
| migrations.deleted_at | deleted at / migration deleted date / deletion timestamp / when migration was deleted | datetime | schema / migrations |
| migrations.id | id / identifier / migration id / migration identifier / record id / primary key | int | nova_127, nova_10, nova_170, nova_848, nova_1042, nova_1043 |
| migrations.source_compute | source compute / source host / origin compute / from host / source compute node / initial host | varchar(255) | nova_127, nova_10, nova_370, nova_564, nova_588, nova_835, nova_978, nova_1042 |
| migrations.dest_compute | dest compute / destination host / target compute / to host / destination compute node / final host | varchar(255) | nova_127, nova_10, nova_370, nova_564, nova_588, nova_835, nova_978, nova_1042 |
| migrations.dest_host | dest host / destination ip / target ip address / dest host ip / destination network address | varchar(255) | nova_127, nova_370, nova_564, nova_588, nova_835, nova_978, nova_1042, nova_1043 |
| migrations.status | status / migration status / state / current status / migration state | varchar(255) | nova_127, nova_10, nova_170, nova_848, nova_370, nova_564, nova_588, nova_835 |
| migrations.instance_uuid | instance uuid / instance id / vm uuid / virtual machine id / instance identifier / server uuid | varchar(36) | nova_127, nova_10, nova_170, nova_848, nova_794, nova_370, nova_564, nova_588 |
| migrations.old_instance_type_id | old instance type id / old instance type identifier / original flavor id / previous instance type / source flavor id / old vm type | int | schema / migrations |
| migrations.new_instance_type_id | new instance type id / new instance type identifier / new flavor id / target instance type / destination flavor id / new vm type | int | schema / migrations |
| migrations.source_node | source node / source hostname / origin node name / from node / source compute hostname | varchar(255) | schema / migrations |
| migrations.dest_node | dest node / destination hostname / target node name / to node / destination compute hostname | varchar(255) | schema / migrations |
| migrations.deleted | deleted / is deleted / deletion flag / soft delete flag / active flag | int | nova_10 |
| migrations.migration_type | migration type / type of migration / migration category / migration kind / live migration vs cold | enum('migration','resize','live-migration','evacuation') | nova_127, nova_370, nova_564, nova_588, nova_835, nova_978, nova_1042, nova_1043 |
| migrations.hidden | hidden / is hidden / visibility flag / hidden flag / display flag | tinyint(1) | nova_848 |
| migrations.memory_total | memory total / total memory migrated / total ram / memory size / total memory in bytes | bigint | nova_127, nova_10, nova_170, nova_848, nova_794, nova_370, nova_564, nova_588 |
| migrations.memory_processed | memory processed / memory transferred / processed ram / memory copied / memory sent | bigint | nova_127, nova_370, nova_564, nova_588, nova_835, nova_978 |
| migrations.memory_remaining | memory remaining / remaining memory / unprocessed memory / memory left / memory to transfer | bigint | nova_127, nova_370, nova_564, nova_588, nova_835, nova_978 |
| migrations.disk_total | disk total / total disk size / total disk migrated / disk capacity / total disk in bytes | bigint | nova_794 |
| migrations.disk_processed | disk processed / disk transferred / processed disk / disk copied / disk sent | bigint | schema / migrations |
| migrations.disk_remaining | disk remaining / remaining disk / unprocessed disk / disk left / disk to transfer | bigint | schema / migrations |

## networks

Stores configuration details for network segments, including IP addressing, routing, DHCP, and bridge settings.

恢复表名: networks / network / network configuration / network settings / subnet / subnets / ip network / network definition
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| networks.created_at | created at / creation date / created / creation timestamp / date created / network creation time | datetime | schema / networks |
| networks.updated_at | updated at / last updated / update date / modified date / last modified / update timestamp | datetime | schema / networks |
| networks.deleted_at | deleted at / deletion date / deleted / removal date / soft delete time / date deleted | datetime | schema / networks |
| networks.id | id / identifier / network id / primary key / network identifier / record id | int | schema / networks |
| networks.injected | injected / injection status / is injected / injected flag / injection state / auto injected | tinyint(1) | schema / networks |
| networks.cidr | cidr / cidr block / ip range / network address / subnet cidr / ipv4 cidr / network prefix | varchar(43) | schema / networks |
| networks.netmask | netmask / subnet mask / network mask / ipv4 netmask / mask / subnet mask ipv4 | varchar(39) | schema / networks |
| networks.bridge | bridge / bridge name / bridge device / linux bridge / network bridge / bridge interface name | varchar(255) | schema / networks |
| networks.gateway | gateway / default gateway / ipv4 gateway / gateway ip / router address / network gateway | varchar(39) | schema / networks |
| networks.broadcast | broadcast / broadcast address / ipv4 broadcast / broadcast ip / network broadcast | varchar(39) | schema / networks |
| networks.dns1 | dns1 / primary dns / dns server 1 / first dns / main dns / dns1 address | varchar(39) | schema / networks |
| networks.vlan | vlan / vlan id / vlan number / virtual lan / vlan tag / network vlan | int | schema / networks |
| networks.vpn_public_address | vpn public address / vpn public ip / public vpn address / vpn external ip / vpn public endpoint / public vpn cidr | varchar(39) | schema / networks |
| networks.vpn_public_port | vpn public port / public vpn port / vpn external port / vpn port / public vpn port number | int | schema / networks |
| networks.vpn_private_address | vpn private address / vpn private ip / private vpn address / vpn internal ip / vpn private endpoint / internal vpn address | varchar(39) | schema / networks |
| networks.dhcp_start | dhcp start / dhcp start address / dhcp range start / first dhcp ip / dhcp pool start / dhcp start ip | varchar(39) | schema / networks |
| networks.project_id | project id / project identifier / project / associated project / project uuid / project reference | varchar(255) | schema / networks |
| networks.host | host / host name / server name / compute host / node name / host identifier | varchar(255) | schema / networks |
| networks.cidr_v6 | cidr v6 / ipv6 cidr / ipv6 range / ipv6 network / ipv6 prefix / ipv6 subnet | varchar(43) | schema / networks |
| networks.gateway_v6 | gateway v6 / ipv6 gateway / gateway ipv6 / ipv6 default gateway / router ipv6 / ipv6 gateway address | varchar(39) | schema / networks |
| networks.label | label / network label / name / display name / network name / label name | varchar(255) | schema / networks |
| networks.netmask_v6 | netmask v6 / ipv6 netmask / ipv6 prefix length / ipv6 mask / subnet mask ipv6 / ipv6 network mask | varchar(39) | schema / networks |
| networks.bridge_interface | bridge interface / physical interface / bridge port / network interface / ethernet interface / bridge member | varchar(255) | schema / networks |
| networks.multi_host | multi host / multi host flag / is multi host / multi-host enabled / shared network / multi host status | tinyint(1) | schema / networks |
| networks.dns2 | dns2 / secondary dns / dns server 2 / second dns / backup dns / dns2 address | varchar(39) | schema / networks |
| networks.uuid | uuid / network uuid / unique identifier / network guid / universal unique identifier | varchar(36) | schema / networks |
| networks.priority | priority / network priority / priority level / routing priority / priority rank / network order | int | schema / networks |
| networks.rxtx_base | rxtx base / rxtx base address / receive transmit base / base address for rxtx / rxtx start | int | schema / networks |
| networks.deleted | deleted / deleted flag / is deleted / soft delete flag / deletion status / active status | int | schema / networks |
| networks.mtu | mtu / maximum transmission unit / mtu size / packet size / max packet size / network mtu | int | schema / networks |
| networks.dhcp_server | dhcp server / dhcp server ip / dhcp address / dhcp server address / dhcp host | varchar(39) | schema / networks |
| networks.enable_dhcp | enable dhcp / dhcp enabled / is dhcp on / dhcp status / dhcp flag / dhcp active | tinyint(1) | schema / networks |
| networks.share_address | share address / share address flag / is shared address / address sharing / shared ip / share address status | tinyint(1) | schema / networks |

## pci_devices

Stores inventory and status of PCI devices (such as GPUs) attached to compute nodes, including their hardware identifiers, addresses, and allocation status.

恢复表名: pci devices / PCI device inventory / hardware devices / compute node devices / GPU devices / accelerator devices
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| pci_devices.created_at | created at / creation time / created date / record created / timestamp created | datetime | schema / pci_devices |
| pci_devices.updated_at | updated at / last updated / update time / modified date / last modified | datetime | schema / pci_devices |
| pci_devices.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp | datetime | schema / pci_devices |
| pci_devices.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / pci_devices |
| pci_devices.id | id / identifier / device id / primary key / record id / pci device id | int | schema / pci_devices |
| pci_devices.compute_node_id | compute node id / compute node identifier / node id / host id / compute node / server id | int | schema / pci_devices |
| pci_devices.address | address / pci address / bus address / device address / slot address | varchar(12) | schema / pci_devices |
| pci_devices.product_id | product id / product identifier / product code / device product id / pci product id | varchar(4) | schema / pci_devices |
| pci_devices.vendor_id | vendor id / vendor identifier / vendor code / manufacturer id / pci vendor id | varchar(4) | schema / pci_devices |
| pci_devices.dev_type | dev type / device type / type / pci type | varchar(8) | schema / pci_devices |
| pci_devices.dev_id | dev id / dev identifier / device identifier / unique device name / pci dev id | varchar(255) | schema / pci_devices |
| pci_devices.label | label / device label / name / tag | varchar(255) | schema / pci_devices |
| pci_devices.status | status / device status / state / availability | varchar(36) | schema / pci_devices |
| pci_devices.extra_info | extra info / additional info / metadata / extra details | text | schema / pci_devices |
| pci_devices.instance_uuid | instance uuid / instance id / vm id / virtual machine id | varchar(36) | schema / pci_devices |
| pci_devices.request_id | request id / request identifier / request uuid / allocation request id | varchar(36) | schema / pci_devices |
| pci_devices.numa_node | numa node / numa id / numa node id / numa affinity | int | schema / pci_devices |
| pci_devices.parent_addr | parent addr / parent address / upstream port address / bridge address | varchar(12) | schema / pci_devices |

## project_user_quotas

Stores resource usage limits and quotas assigned to specific users within specific projects.

恢复表名: project user quotas / user project limits / resource quotas / project resource limits / user resource caps / quota settings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| project_user_quotas.id | id / identifier / quota id / record id / primary key / unique identifier | int | schema / project_user_quotas |
| project_user_quotas.created_at | created at / creation date / created timestamp / start date / when created | datetime | schema / project_user_quotas |
| project_user_quotas.updated_at | updated at / update date / last modified / modified timestamp / when updated | datetime | schema / project_user_quotas |
| project_user_quotas.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / when deleted | datetime | schema / project_user_quotas |
| project_user_quotas.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / project_user_quotas |
| project_user_quotas.user_id | user id / user identifier / user / account id / member id | varchar(255) | schema / project_user_quotas |
| project_user_quotas.project_id | project id / project identifier / project / workspace id / project code | varchar(255) | schema / project_user_quotas |
| project_user_quotas.resource | resource / resource type / resource name / quota resource / limit type | varchar(255) | schema / project_user_quotas |
| project_user_quotas.hard_limit | hard limit / maximum limit / cap / max value / upper bound | int | schema / project_user_quotas |

## provider_fw_rules

Stores firewall rule definitions for providers, specifying allowed network traffic based on protocol, port ranges, and CIDR blocks.

恢复表名: provider fw rules / provider firewall rules / firewall rules / fw rules / network firewall configuration / provider network rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| provider_fw_rules.created_at | created at / creation date / created timestamp / rule creation time / when created | datetime | schema / provider_fw_rules |
| provider_fw_rules.updated_at | updated at / update date / last modified / updated timestamp / modification time | datetime | schema / provider_fw_rules |
| provider_fw_rules.deleted_at | deleted at / deletion date / deleted timestamp / removal time / when deleted | datetime | schema / provider_fw_rules |
| provider_fw_rules.id | id / identifier / rule id / firewall rule identifier / primary key / rule number | int | schema / provider_fw_rules |
| provider_fw_rules.protocol | protocol / network protocol / traffic protocol / ip protocol / protocol type | varchar(5) | schema / provider_fw_rules |
| provider_fw_rules.from_port | from port / start port / source port / minimum port / port range start | int | schema / provider_fw_rules |
| provider_fw_rules.to_port | to port / end port / destination port / maximum port / port range end | int | schema / provider_fw_rules |
| provider_fw_rules.cidr | cidr / ip range / network address / source ip / cidr block / ip address range | varchar(43) | schema / provider_fw_rules |
| provider_fw_rules.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / provider_fw_rules |

## quota_classes

Defines the maximum allowed limits (hard limits) for various cloud resources (such as instances, RAM, and cores) for different user classes or projects.

恢复表名: quota classes / quota_classes / quotas / resource_quotas / quota_definitions / limit_classes / resource_limits
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| quota_classes.created_at | created at / creation_date / created / timestamp_created / date_created / record_created | datetime | schema / quota_classes |
| quota_classes.updated_at | updated at / last_updated / modified_date / update_timestamp / date_modified / last_change | datetime | schema / quota_classes |
| quota_classes.deleted_at | deleted at / deletion_date / deleted / removal_timestamp / date_deleted / soft_delete_time | datetime | schema / quota_classes |
| quota_classes.id | id / identifier / quota_id / primary_key / record_id / class_id | int | schema / quota_classes |
| quota_classes.class_name | class name / quota_class / user_class / project_type / tenant_class / class / category | varchar(255) | schema / quota_classes |
| quota_classes.resource | resource / resource_type / limit_resource / quota_resource / resource_name / metric / cloud_resource | varchar(255) | schema / quota_classes |
| quota_classes.hard_limit | hard limit / max_limit / maximum_value / quota_limit / upper_bound / max_allowed / limit_value | int | schema / quota_classes |
| quota_classes.deleted | deleted / is_deleted / deletion_flag / active_status / soft_delete_flag / removed | int | schema / quota_classes |

## quota_usages

Tracks the current usage and reservation of specific resources (like cores, instances, volumes) against defined quotas for each project and user in the Nova compute service.

恢复表名: quota usages / quota_usages / quota usage / resource quotas / project quotas / nova quotas / usage quotas
SQL表别名: q, q2, qu, qu2, t0

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| quota_usages.created_at | created at / created_at / creation date / created date / record created / timestamp created | datetime | schema / quota_usages |
| quota_usages.updated_at | updated at / updated_at / last updated / update date / modified date / last modified | datetime | schema / quota_usages |
| quota_usages.deleted_at | deleted at / deleted_at / deletion date / deleted date / soft delete time | datetime | schema / quota_usages |
| quota_usages.id | id / identifier / quota usage id / usage id / primary key / record id | int | nova_280, nova_728, nova_743, nova_781, nova_250, nova_290, nova_320, nova_347 |
| quota_usages.project_id | project id / project identifier / project_id / tenant id / project uuid / tenant uuid | varchar(255) | nova_280, nova_728, nova_743, nova_781, nova_290 |
| quota_usages.resource | resource / resource type / quota resource / resource name / quota type | varchar(255) | nova_280, nova_728, nova_743, nova_781, nova_250, nova_290, nova_320, nova_347 |
| quota_usages.in_use | in use / in_use / current usage / used amount / active usage | int | nova_280, nova_728, nova_743, nova_781, nova_250, nova_290, nova_366 |
| quota_usages.reserved | reserved / reserved amount / reserved count / pending usage | int | nova_280, nova_366 |
| quota_usages.until_refresh | until refresh / until_refresh / refresh time / time until refresh / refresh interval | int | schema / quota_usages |
| quota_usages.deleted | deleted / is deleted / soft delete flag / deletion status | int | nova_280, nova_728, nova_743, nova_781, nova_250, nova_320, nova_347, nova_354 |
| quota_usages.user_id | user id / user identifier / user_id / owner id / user uuid | varchar(255) | schema / quota_usages |

## quotas

Stores resource usage limits and quotas for specific projects, defining the maximum allowed amount for various resources like instances, cores, RAM, and IPs.

恢复表名: quotas / quota / resource_quotas / project_quotas / limits / resource_limits / quota_definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| quotas.id | id / identifier / quota_id / primary_key / record_id | int | schema / quotas |
| quotas.created_at | created at / creation_date / created / start_date / timestamp_created / date_added | datetime | schema / quotas |
| quotas.updated_at | updated at / last_modified / modified_date / updated / last_update / change_date | datetime | schema / quotas |
| quotas.deleted_at | deleted at / deletion_date / removed_at / soft_delete_time / archived_at | datetime | schema / quotas |
| quotas.project_id | project id / project identifier / project / project_identifier / tenant_id / account_id / associated_project | varchar(255) | schema / quotas |
| quotas.resource | resource / resource_type / quota_type / metric / resource_name / limit_category | varchar(255) | schema / quotas |
| quotas.hard_limit | hard limit / max_limit / maximum / cap / upper_bound / limit_value / max_allowed | int | schema / quotas |
| quotas.deleted | deleted / is_deleted / active_status / soft_delete_flag / status / removed | int | schema / quotas |

## reservations

Stores records of reserved quota amounts for specific resources (like cores, RAM, instances) associated with projects and users, linked to quota usage records.

恢复表名: reservations / reservation / quota reservations / resource reservations / nova reservations
SQL表别名: r, r2, t1

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| reservations.created_at | created at / creation date / reservation created / timestamp created / date created | datetime | schema / reservations |
| reservations.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / reservations |
| reservations.deleted_at | deleted at / deletion date / soft delete time / removed at / archived at | datetime | schema / reservations |
| reservations.id | id / identifier / reservation id / primary key / record id / unique id | int | nova_280, nova_728, nova_743, nova_781, nova_290 |
| reservations.uuid | uuid / reservation uuid / unique universal identifier / global id / guid | varchar(36) | nova_366, nova_280, nova_453 |
| reservations.usage_id | usage id / usage identifier / quota usage id / foreign key to quota usages / linked usage / usage reference | int | nova_366, nova_280, nova_453, nova_728, nova_743, nova_781, nova_290, nova_320 |
| reservations.project_id | project id / project identifier / tenant project / project uuid / project reference | varchar(255) | nova_366, nova_453 |
| reservations.resource | resource / resource type / quota resource / resource name / type of resource | varchar(255) | nova_366, nova_453, nova_320 |
| reservations.delta | delta / reserved amount / reservation quantity / amount reserved / quota delta | int | nova_366, nova_280, nova_728, nova_743, nova_781, nova_290, nova_320, nova_354 |
| reservations.expire | expire / expiration date / expiry time / reservation end date / valid until | datetime | nova_366, nova_453, nova_728, nova_743, nova_781, nova_354, nova_562 |
| reservations.deleted | deleted / deleted id / soft delete flag / is deleted / deletion marker | int | schema / reservations |
| reservations.user_id | user id / user identifier / owner id / tenant user / user reference | varchar(255) | schema / reservations |

## resource_provider_aggregates

Stores aggregated metrics or summary data for resource providers, linking provider identifiers to specific aggregate records.

恢复表名: resource provider aggregates / provider aggregates / aggregated resource providers / resource provider summary / provider stats
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| resource_provider_aggregates.resource_provider_id | resource provider id / resource provider identifier / provider id / provider key / rp id / provider number | int | schema / resource_provider_aggregates |
| resource_provider_aggregates.aggregate_id | aggregate id / aggregate identifier / summary id / aggregation identifier / agg id / summary key | int | schema / resource_provider_aggregates |

## resource_providers

Stores metadata for resource providers, which represent physical or virtual resources (like compute nodes) that can be allocated, identified by UUID and linked to compute nodes.

恢复表名: resource providers / resource provider / rp / provider / providers
SQL表别名: rp

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| resource_providers.id | id / identifier / primary key / row id | int | schema / resource_providers |
| resource_providers.uuid | uuid / unique identifier / provider uuid / resource provider uuid / node uuid | varchar(36) | nova_514 |
| resource_providers.name | name / provider name / resource provider name / display name | varchar(200) | schema / resource_providers |
| resource_providers.generation | generation / gen / version / resource generation | int | schema / resource_providers |
| resource_providers.can_host | can host / hosting capability / is host / host flag | int | schema / resource_providers |

## s3_images

Stores metadata and lifecycle status for images hosted on S3, including creation, update, and deletion timestamps.

恢复表名: s3 images / images / image records / S3 image table / image metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| s3_images.created_at | created at / creation date / created date / image creation time / timestamp created / date added | datetime | schema / s3_images |
| s3_images.updated_at | updated at / last updated / update date / modification time / last modified / updated timestamp | datetime | schema / s3_images |
| s3_images.deleted_at | deleted at / deletion date / deleted date / removal time / soft delete timestamp / date deleted | datetime | schema / s3_images |
| s3_images.id | id / identifier / image id / primary key / record id / image identifier / internal id | int | schema / s3_images |
| s3_images.uuid | uuid / image uuid / unique identifier / guid / universal id / image guid | varchar(36) | schema / s3_images |
| s3_images.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / s3_images |

## security_group_default_rules

Stores the default inbound and outbound access control rules associated with security groups, defining allowed network traffic by protocol, port range, and source/destination CIDR blocks.

恢复表名: security group default rules / default security group rules / sg default rules / security group rule defaults / default firewall rules / security group access rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| security_group_default_rules.created_at | created at / creation time / created date / rule creation timestamp / when created / creation timestamp | datetime | schema / security_group_default_rules |
| security_group_default_rules.updated_at | updated at / last updated time / modification date / update timestamp / when modified / last change time | datetime | schema / security_group_default_rules |
| security_group_default_rules.deleted_at | deleted at / deletion time / deleted date / removal timestamp / when deleted / soft delete time | datetime | schema / security_group_default_rules |
| security_group_default_rules.deleted | deleted / is deleted / deletion flag / soft delete status / active status / record status | int | schema / security_group_default_rules |
| security_group_default_rules.id | id / identifier / rule id / rule identifier / primary key / unique id / rule number | int | schema / security_group_default_rules |
| security_group_default_rules.protocol | protocol / network protocol / traffic protocol / ip protocol / protocol type / communication protocol | varchar(5) | schema / security_group_default_rules |
| security_group_default_rules.from_port | from port / start port / source port / port range start / minimum port / initial port | int | schema / security_group_default_rules |
| security_group_default_rules.to_port | to port / end port / destination port / port range end / maximum port / final port | int | schema / security_group_default_rules |
| security_group_default_rules.cidr | cidr / ip range / source ip / destination ip / network address / ip address block / subnet range | varchar(43) | schema / security_group_default_rules |

## security_group_instance_association

Tracks the many-to-many relationship between security groups and compute instances, recording which security groups are applied to which instances.

恢复表名: security group instance association / sg instance mapping / security group to instance link / instance security group join / sg instance relation
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| security_group_instance_association.created_at | created at / creation time / created date / association start time / timestamp created | datetime | schema / security_group_instance_association |
| security_group_instance_association.updated_at | updated at / last modified time / update timestamp / last changed date / modification time | datetime | schema / security_group_instance_association |
| security_group_instance_association.deleted_at | deleted at / deletion time / removed date / soft delete timestamp / disassociation time | datetime | schema / security_group_instance_association |
| security_group_instance_association.id | id / identifier / primary key / association id / record id / unique identifier | int | schema / security_group_instance_association |
| security_group_instance_association.security_group_id | security group id / security group identifier / sg id / group identifier / firewall group id | int | schema / security_group_instance_association |
| security_group_instance_association.instance_uuid | instance uuid / vm uuid / server uuid / compute instance id / virtual machine identifier | varchar(36) | schema / security_group_instance_association |
| security_group_instance_association.deleted | deleted / is deleted / soft delete flag / active status / deletion flag | int | schema / security_group_instance_association |

## security_group_rules

Stores individual firewall rules defining network access permissions (protocol, port range, CIDR) for specific security groups in the Nova cloud infrastructure.

恢复表名: security group rules / firewall rules / network access rules / sg rules / port rules / access control rules
SQL表别名: r, sgr, sgr2

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| security_group_rules.created_at | created at / creation time / created date / rule creation timestamp / when rule was created | datetime | schema / security_group_rules |
| security_group_rules.updated_at | updated at / last updated time / modification date / rule update timestamp / when rule was last modified | datetime | schema / security_group_rules |
| security_group_rules.deleted_at | deleted at / deletion time / deleted date / rule deletion timestamp / when rule was deleted | datetime | schema / security_group_rules |
| security_group_rules.id | id / identifier / rule id / rule identifier / primary key / unique rule id | int | nova_255, nova_95, nova_284, nova_885, nova_922, nova_390 |
| security_group_rules.parent_group_id | parent group id / parent group identifier / security group id / group id / parent group / associated security group / sg id | int | nova_255, nova_95, nova_284, nova_62, nova_885, nova_922, nova_935, nova_236 |
| security_group_rules.protocol | protocol / network protocol / ip protocol / traffic type / protocol type | varchar(255) | nova_255, nova_95, nova_284, nova_62, nova_885, nova_922, nova_935, nova_236 |
| security_group_rules.from_port | from port / start port / source port / minimum port / port range start / lower port bound | int | nova_255, nova_95, nova_62, nova_885, nova_922, nova_935, nova_236, nova_431 |
| security_group_rules.to_port | to port / end port / destination port / maximum port / port range end / upper port bound | int | nova_255, nova_95, nova_284, nova_62, nova_922, nova_935, nova_236, nova_431 |
| security_group_rules.cidr | cidr / ip address range / source ip / network address / ip block / subnet | varchar(43) | nova_255, nova_95, nova_284, nova_62, nova_935, nova_241, nova_390 |
| security_group_rules.group_id | group id / group identifier / group reference / security group ref / legacy group id | int | schema / security_group_rules |
| security_group_rules.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | nova_255, nova_95, nova_885, nova_241, nova_431 |

## security_groups

Stores metadata for OpenStack Nova security groups, which define firewall rules for instances, including ownership, project association, and soft-delete status.

恢复表名: security groups / security group / firewall group / firewall groups / network security group / nova security group
SQL表别名: sg, sg2, sg3

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| security_groups.created_at | created at / creation date / created timestamp / start date / date created / creation time | datetime | schema / security_groups |
| security_groups.updated_at | updated at / update date / last modified / modified timestamp / last updated / change date | datetime | schema / security_groups |
| security_groups.deleted_at | deleted at / deletion date / deleted timestamp / removal date / date deleted / soft delete time | datetime | schema / security_groups |
| security_groups.id | id / identifier / security group id / group id / sg id / primary key | int | nova_255, nova_62, nova_284, nova_431, nova_664, nova_675, nova_885, nova_922 |
| security_groups.name | name / security group name / group name / sg name / firewall name / label | varchar(255) | nova_255, nova_62, nova_284, nova_431, nova_664, nova_675, nova_885, nova_922 |
| security_groups.description | description / security group description / group description / sg description / notes / details | varchar(255) | nova_255, nova_62, nova_284, nova_922 |
| security_groups.user_id | user id / user identifier / owner id / creator id / account id / tenant user id | varchar(255) | nova_62 |
| security_groups.project_id | project id / project identifier / tenant id / tenant identifier / org id | varchar(255) | nova_255, nova_62 |
| security_groups.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / removed flag | int | nova_255, nova_431, nova_664, nova_675, nova_885, nova_95 |

## services

Stores metadata and status information for OpenStack Nova services running on various hosts, including their binary type, topic, availability status, and timestamps.

恢复表名: services / nova services / compute services / service registry / openstack services / service nodes / service instances
SQL表别名: s

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| services.created_at | created at / creation date / created timestamp / service creation time / date created / initial registration time | datetime | schema / services |
| services.updated_at | updated at / last update time / modified date / update timestamp / last modified / record update time | datetime | schema / services |
| services.deleted_at | deleted at / deletion date / deleted timestamp / removal time / date deleted / soft delete time | datetime | schema / services |
| services.id | id / identifier / service id / service identifier / primary key / unique service id / service number | int | schema / services |
| services.host | host / hostname / server name / node name / physical host / compute node / machine name | varchar(255) | schema / services |
| services.binary | binary / service binary / executable name / service type / process name / daemon name / nova binary | varchar(255) | nova_390 |
| services.topic | topic / service topic / message topic / amqp topic / service category / functional area | varchar(255) | schema / services |
| services.report_count | report count / heartbeat count / report counter / status report count / ping count / liveness count | int | schema / services |
| services.disabled | disabled / is disabled / disabled status / service disabled flag / inactive flag / enabled status | tinyint(1) | schema / services |
| services.deleted | deleted / deleted flag / is deleted / soft delete flag / removal status / active status | int | schema / services |
| services.disabled_reason | disabled reason / reason for disabling / disable reason / error message / failure reason / status message | varchar(255) | schema / services |
| services.last_seen_up | last seen up / last heartbeat / last up time / last alive timestamp / last status check / last ping time | datetime | schema / services |
| services.forced_down | forced down / is forced down / forced down flag / manual down status / admin down flag / forced offline | tinyint(1) | schema / services |
| services.version | version / service version / software version / binary version / nova version / release version | int | schema / services |

## shadow_agent_builds

Stores metadata for different builds or versions of the Shadow Agent software, including hypervisor compatibility, OS, architecture, and download details.

恢复表名: shadow agent builds / agent builds / shadow builds / agent versions / build artifacts / agent releases
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_agent_builds.created_at | created at / creation date / created timestamp / build creation time / when created | datetime | schema / shadow_agent_builds |
| shadow_agent_builds.updated_at | updated at / update date / last modified / updated timestamp / last update time | datetime | schema / shadow_agent_builds |
| shadow_agent_builds.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / when deleted | datetime | schema / shadow_agent_builds |
| shadow_agent_builds.id | id / identifier / build id / primary key / record id / agent build identifier | int | schema / shadow_agent_builds |
| shadow_agent_builds.hypervisor | hypervisor / virtualization platform / vm platform / hypervisor type / host platform | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.os | os / operating system / os type / guest os / system platform | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.architecture | architecture / cpu architecture / arch / system architecture / processor type | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.version | version / agent version / software version / build version / release version | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.url | url / download link / download url / file location / artifact url | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.md5hash | md5hash / checksum / md5 / file hash / integrity hash | varchar(255) | schema / shadow_agent_builds |
| shadow_agent_builds.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / shadow_agent_builds |

## shadow_aggregate_hosts

Maps individual hosts to aggregate groups, tracking creation, update, and deletion timestamps for each association.

恢复表名: shadow aggregate hosts / aggregate host mapping / host aggregation table / shadow hosts
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_aggregate_hosts.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.deleted_at | deleted at / deletion date / removed at / soft delete time / archived date | datetime | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.id | id / identifier / primary key / record id / unique identifier / row id | int | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.host | host / hostname / server name / machine name / node name | varchar(255) | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.aggregate_id | aggregate id / aggregate identifier / group id / cluster id / pool id | int | schema / shadow_aggregate_hosts |
| shadow_aggregate_hosts.deleted | deleted / deletion flag / is deleted / soft delete flag / status deleted | int | schema / shadow_aggregate_hosts |

## shadow_aggregate_metadata

Stores key-value metadata pairs associated with shadow aggregates, including allocation ratios and configuration switches, with soft-delete tracking.

恢复表名: shadow aggregate metadata / aggregate metadata / shadow metadata / aggregate key value store / shadow aggregate config
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_aggregate_metadata.created_at | created at / creation date / created timestamp / record created / inserted at / creation time | datetime | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.updated_at | updated at / last updated / modification date / updated timestamp / last modified / change time | datetime | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removed at / archived at | datetime | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.id | id / identifier / primary key / record id / metadata id / unique identifier / row id | int | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.aggregate_id | aggregate id / aggregate identifier / parent aggregate id / shadow aggregate id / related aggregate / aggregate reference | int | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.key | key / metadata key / attribute name / property name / config key / field name | varchar(255) | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.value | value / metadata value / attribute value / property value / config value / data value | varchar(255) | schema / shadow_aggregate_metadata |
| shadow_aggregate_metadata.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / removed flag | int | schema / shadow_aggregate_metadata |

## shadow_aggregates

Stores metadata and identifiers for shadow aggregate entities, including creation, update, and deletion timestamps.

恢复表名: shadow aggregates / aggregate shadows / shadow aggregate records / aggregated shadow data
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_aggregates.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / shadow_aggregates |
| shadow_aggregates.updated_at | updated at / last updated / modification date / updated timestamp / last modified | datetime | schema / shadow_aggregates |
| shadow_aggregates.deleted_at | deleted at / deletion date / deleted timestamp / removed at / soft delete time | datetime | schema / shadow_aggregates |
| shadow_aggregates.id | id / identifier / primary key / record id / aggregate id / unique identifier | int | schema / shadow_aggregates |
| shadow_aggregates.name | name / aggregate name / label / title / display name | varchar(255) | schema / shadow_aggregates |
| shadow_aggregates.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / shadow_aggregates |
| shadow_aggregates.uuid | uuid / universal unique identifier / guid / external id / unique string id | varchar(36) | schema / shadow_aggregates |

## shadow_block_device_mapping

Stores the mapping between virtual block devices (disks/volumes) and compute instances, including attachment details, device names, and connection information.

恢复表名: shadow block device mapping / shadow_bdm / block_device_mapping / bdm / block device mapping / shadow block device / volume attachment / disk mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_block_device_mapping.created_at | created at / creation time / created date / timestamp created / when created / creation timestamp | datetime | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.updated_at | updated at / update time / last updated / modified date / last modified / update timestamp | datetime | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.deleted_at | deleted at / deletion time / deleted date / removed at / soft delete time / deletion timestamp | datetime | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.id | id / identifier / primary key / bdm id / mapping id / record id / unique identifier | int | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.device_name | device name / device / disk name / volume name / block device / device path / mount point | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.delete_on_termination | delete on termination / delete on stop / remove on terminate / ephemeral flag / auto delete / delete with instance | tinyint(1) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.snapshot_id | snapshot id / snapshot identifier / snapshot / source snapshot / snapshot uuid / image snapshot | varchar(36) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.volume_id | volume id / volume identifier / volume / disk id / block storage id / volume uuid / storage id | varchar(36) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.volume_size | volume size / size / disk size / capacity / volume capacity / gb size | int | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.no_device | no device / number device / no device flag / hidden device / not visible / device hidden | tinyint(1) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.connection_info | connection info / connection / attach info / driver info / iscsi info / mount details | text | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.instance_uuid | instance uuid / instance / server id / vm id / compute instance / instance id | varchar(36) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.deleted | deleted / is deleted / soft delete / removed / active flag / deletion status | int | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.source_type | source type / source / origin type / from type | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.destination_type | destination type / destination / target type / to type | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.guest_format | guest format / format / file system / guest fs / disk format | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.device_type | device type / type / disk type / block type / storage type | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.disk_bus | disk bus / bus / controller bus / storage bus | varchar(255) | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.boot_index | boot index / boot order / boot priority / boot rank / startup index | int | schema / shadow_block_device_mapping |
| shadow_block_device_mapping.image_id | image id / image identifier / image / image uuid / source image / base image | varchar(36) | schema / shadow_block_device_mapping |

## shadow_bw_usage_cache

Caches periodic bandwidth usage statistics (inbound/outbound bytes and counters) for network interfaces identified by MAC address or UUID.

恢复表名: shadow bw usage cache / bandwidth usage cache / shadow bandwidth cache / bw usage cache / network traffic cache / bandwidth statistics cache
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_bw_usage_cache.created_at | created at / creation time / record created / inserted at / start date | datetime | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.updated_at | updated at / last updated / modification time / record updated / change timestamp | datetime | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / archived at | datetime | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.id | id / identifier / record id / primary key / cache entry id / row id | int | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.start_period | start period / period start / usage period start / interval start / window start | datetime | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.last_refreshed | last refreshed / last refresh time / data refreshed at / cache updated at / sync time | datetime | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.bw_in | bw in / inbound bandwidth / bytes in / download bytes / traffic in / input bytes | bigint | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.bw_out | bw out / outbound bandwidth / bytes out / upload bytes / traffic out / output bytes | bigint | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.mac | mac / mac address / hardware address / physical address / device mac | varchar(255) | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.uuid | uuid / unique identifier / device uuid / interface uuid / universal unique identifier | varchar(36) | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.last_ctr_in | last ctr in / last input counter / inbound counter / bytes in counter / input packet counter | bigint | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.last_ctr_out | last ctr out / last output counter / outbound counter / bytes out counter / output packet counter | bigint | schema / shadow_bw_usage_cache |
| shadow_bw_usage_cache.deleted | deleted / is deleted / soft delete flag / deleted status / active flag | int | schema / shadow_bw_usage_cache |

## shadow_cells

Stores configuration and metadata for shadow cells, including API and transport endpoints, weight adjustments, and hierarchical status.

恢复表名: shadow cells / shadow cell / cell shadows / shadow cell configurations / cell shadow settings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_cells.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / shadow_cells |
| shadow_cells.updated_at | updated at / last updated / modification date / updated timestamp / last modified | datetime | schema / shadow_cells |
| shadow_cells.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removal date | datetime | schema / shadow_cells |
| shadow_cells.id | id / identifier / primary key / cell id / shadow cell id / record id / unique identifier | int | schema / shadow_cells |
| shadow_cells.api_url | api url / api endpoint / api address / api link / service url / api location | varchar(255) | schema / shadow_cells |
| shadow_cells.weight_offset | weight offset / offset value / weight adjustment / base weight offset | float | schema / shadow_cells |
| shadow_cells.weight_scale | weight scale / scale factor / weight multiplier / scaling factor | float | schema / shadow_cells |
| shadow_cells.name | name / cell name / shadow cell name / display name / label | varchar(255) | schema / shadow_cells |
| shadow_cells.is_parent | is parent / parent flag / is parent cell / parent status / hierarchy parent | tinyint(1) | schema / shadow_cells |
| shadow_cells.deleted | deleted / deleted flag / is deleted / soft delete flag / deletion status | int | schema / shadow_cells |
| shadow_cells.transport_url | transport url / transport endpoint / transport address / transport link / data transport url | varchar(255) | schema / shadow_cells |

## shadow_certificates

Stores metadata for shadow certificate files associated with users and projects, including file names and soft-delete status.

恢复表名: shadow certificates / certificates / shadow certificate records / certificate files / user certificates / project certificates
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_certificates.created_at | created at / creation date / created timestamp / date created / record created / inserted at | datetime | schema / shadow_certificates |
| shadow_certificates.updated_at | updated at / update date / last updated / modified at / last modified timestamp / change date | datetime | schema / shadow_certificates |
| shadow_certificates.deleted_at | deleted at / deletion date / deleted timestamp / date deleted / soft delete time / removed at | datetime | schema / shadow_certificates |
| shadow_certificates.id | id / identifier / certificate id / primary key / record id / unique identifier / shadow certificate id | int | schema / shadow_certificates |
| shadow_certificates.user_id | user id / user identifier / owner id / associated user / user reference / account id | varchar(255) | schema / shadow_certificates |
| shadow_certificates.project_id | project id / project identifier / associated project / project reference / project code / project key | varchar(255) | schema / shadow_certificates |
| shadow_certificates.file_name | file name / certificate file name / filename / file path / document name / certificate name | varchar(255) | schema / shadow_certificates |
| shadow_certificates.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / shadow_certificates |

## shadow_compute_nodes

Stores metadata and resource capacity/usage statistics for compute nodes (hypervisors) in the Nova cloud infrastructure, including CPU, memory, disk, and hypervisor details.

恢复表名: shadow compute nodes / compute nodes / hypervisors / compute hosts / nova compute nodes / shadow compute / compute resources
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_compute_nodes.created_at | created at / creation time / created date / record created / node creation timestamp | datetime | schema / shadow_compute_nodes |
| shadow_compute_nodes.updated_at | updated at / last updated / update time / modified date / last modification timestamp | datetime | schema / shadow_compute_nodes |
| shadow_compute_nodes.deleted_at | deleted at / deletion time / deleted date / removal timestamp / soft delete time | datetime | schema / shadow_compute_nodes |
| shadow_compute_nodes.id | id / identifier / node id / compute node id / primary key / record id | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.service_id | service id / service identifier / associated service / compute service id / service reference | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.vcpus | vcpus / total vcpus / cpu count / virtual cpus / total cpu capacity | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.memory_mb | memory mb / total memory / ram size / memory capacity / total ram in mb | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.local_gb | local gb / local disk / disk capacity / local storage / total local gb | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.vcpus_used | vcpus used / used vcpus / cpu usage / allocated vcpus / consumed cpus | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.memory_mb_used | memory mb used / used memory / ram usage / allocated memory / consumed ram | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.local_gb_used | local gb used / used disk / disk usage / allocated disk / consumed storage | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.hypervisor_type | hypervisor type / hypervisor / virtualization type / vm platform / hypervisor name | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.hypervisor_version | hypervisor version / hypervisor ver / vm version / hypervisor build / software version | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.cpu_info | cpu info / cpu details / processor info / cpu model / hardware cpu specs | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.disk_available_least | disk available least / min free disk / least available disk / minimum disk space / disk threshold | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.free_ram_mb | free ram mb / available ram / free memory / unused ram / remaining memory | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.free_disk_gb | free disk gb / available disk / free storage / unused disk / remaining disk space | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.current_workload | current workload / workload / current load / node load / active workload | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.running_vms | running vms / active vms / vm count / instances running / number of vms | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.hypervisor_hostname | hypervisor hostname / hostname / node name / server name / compute host name | varchar(255) | schema / shadow_compute_nodes |
| shadow_compute_nodes.deleted | deleted / is deleted / deletion flag / soft delete flag / removed status | int | schema / shadow_compute_nodes |
| shadow_compute_nodes.host_ip | host ip / ip address / server ip / network address | varchar(39) | schema / shadow_compute_nodes |
| shadow_compute_nodes.supported_instances | supported instances / instance types / supported flavors / allowed instances / instance capabilities | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.pci_stats | pci stats / pci devices / pci information / pci hardware stats / pci device list | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.metrics | metrics / performance metrics / node metrics / monitoring data / metric values | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.extra_resources | extra resources / additional resources / extra capacity / supplementary resources / other resources | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.stats | stats / statistics / node stats / statistical data / general stats | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.numa_topology | numa topology / numa info / numa configuration / memory topology / numa nodes | text | schema / shadow_compute_nodes |
| shadow_compute_nodes.host | host / host name / server host / compute host / physical host | varchar(255) | schema / shadow_compute_nodes |
| shadow_compute_nodes.ram_allocation_ratio | ram allocation ratio / ram overcommit ratio / memory allocation ratio / ram overcommit / memory overcommit factor | float | schema / shadow_compute_nodes |
| shadow_compute_nodes.cpu_allocation_ratio | cpu allocation ratio / cpu overcommit ratio / cpu overcommit / cpu overcommit factor | float | schema / shadow_compute_nodes |
| shadow_compute_nodes.uuid | uuid / unique id / node uuid / universal unique identifier / global id | varchar(36) | schema / shadow_compute_nodes |
| shadow_compute_nodes.disk_allocation_ratio | disk allocation ratio / disk overcommit ratio / disk overcommit / storage overcommit factor | float | schema / shadow_compute_nodes |

## shadow_console_pools

Stores configuration and connection details for shadow console pools, including host addresses, credentials, and console types.

恢复表名: shadow console pools / console pools / shadow pools / console pool records / shadow console pool table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_console_pools.created_at | created at / creation date / created timestamp / record created / pool creation time | datetime | schema / shadow_console_pools |
| shadow_console_pools.updated_at | updated at / last updated / update timestamp / modified date / last modification time | datetime | schema / shadow_console_pools |
| shadow_console_pools.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removal date | datetime | schema / shadow_console_pools |
| shadow_console_pools.id | id / identifier / pool id / primary key / record id / console pool identifier | int | schema / shadow_console_pools |
| shadow_console_pools.address | address / ip address / network address / pool address / connection address | varchar(39) | schema / shadow_console_pools |
| shadow_console_pools.username | username / user name / login name / account name / pool username | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.password | password / pass phrase / secret / credential / pool password | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.console_type | console type / type of console / console category / pool type / console kind | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.public_hostname | public hostname / public host / external hostname / public name / internet hostname | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.host | host / internal host / server host / pool host / machine host | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.compute_host | compute host / compute node / compute server / processing host / compute machine | varchar(255) | schema / shadow_console_pools |
| shadow_console_pools.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / shadow_console_pools |

## shadow_consoles

Stores metadata and connection details for shadow console instances, including their association with resource pools and lifecycle status.

恢复表名: shadow consoles / console instances / shadow console records / console pool members / virtual consoles
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_consoles.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / shadow_consoles |
| shadow_consoles.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / shadow_consoles |
| shadow_consoles.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / archived date | datetime | schema / shadow_consoles |
| shadow_consoles.id | id / identifier / console id / primary key / record id / unique identifier | int | schema / shadow_consoles |
| shadow_consoles.instance_name | instance name / console name / instance label / display name / node name | varchar(255) | schema / shadow_consoles |
| shadow_consoles.password | password / console password / access password / login credential / secret | varchar(255) | schema / shadow_consoles |
| shadow_consoles.port | port / connection port / network port / service port / port number | int | schema / shadow_consoles |
| shadow_consoles.pool_id | pool id / pool identifier / resource pool id / group id / pool reference | int | schema / shadow_consoles |
| shadow_consoles.instance_uuid | instance uuid / uuid / unique universal identifier / global id | varchar(36) | schema / shadow_consoles |
| shadow_consoles.deleted | deleted / is deleted / deletion flag / active status / removed flag | int | schema / shadow_consoles |

## shadow_dns_domains

Stores metadata and configuration for DNS domains managed by the shadow DNS service, including scope, availability zone, and project ownership.

恢复表名: shadow dns domains / dns domains / domain records / shadow domain table / dns domain metadata
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_dns_domains.created_at | created at / creation time / created date / timestamp created / record creation date | datetime | schema / shadow_dns_domains |
| shadow_dns_domains.updated_at | updated at / last updated / modification time / updated date / last modified timestamp | datetime | schema / shadow_dns_domains |
| shadow_dns_domains.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / removal date | datetime | schema / shadow_dns_domains |
| shadow_dns_domains.deleted | deleted / is deleted / deletion flag / soft delete status / active status | tinyint(1) | schema / shadow_dns_domains |
| shadow_dns_domains.domain | domain / domain name / dns name / zone name / host name | varchar(255) | schema / shadow_dns_domains |
| shadow_dns_domains.scope | scope / dns scope / domain scope / visibility scope / scope type | varchar(255) | schema / shadow_dns_domains |
| shadow_dns_domains.availability_zone | availability zone / az / zone / availability zone name / region zone | varchar(255) | schema / shadow_dns_domains |
| shadow_dns_domains.project_id | project id / project identifier / project / tenant id / owner project | varchar(255) | schema / shadow_dns_domains |

## shadow_fixed_ips

Stores fixed IP address assignments within the Nova network, tracking allocation, lease status, and association with virtual interfaces and instances.

恢复表名: shadow fixed ips / fixed_ips / fixed ip / fixed ips / ip addresses / ip address / network ips / static ips
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_fixed_ips.created_at | created at / creation time / created date / record created / timestamp created / when created | datetime | schema / shadow_fixed_ips |
| shadow_fixed_ips.updated_at | updated at / update time / last updated / modified date / record updated / when updated | datetime | schema / shadow_fixed_ips |
| shadow_fixed_ips.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / when deleted | datetime | schema / shadow_fixed_ips |
| shadow_fixed_ips.id | id / identifier / fixed ip id / ip id / primary key / record id | int | schema / shadow_fixed_ips |
| shadow_fixed_ips.address | address / ip address / ip / fixed ip address / network address / ipv4 address | varchar(39) | schema / shadow_fixed_ips |
| shadow_fixed_ips.network_id | network id / network identifier / associated network / subnet network id | int | schema / shadow_fixed_ips |
| shadow_fixed_ips.allocated | allocated / is allocated / allocation status / allocated flag / ip allocated | tinyint(1) | schema / shadow_fixed_ips |
| shadow_fixed_ips.leased | leased / is leased / lease status / leased flag / ip leased | tinyint(1) | schema / shadow_fixed_ips |
| shadow_fixed_ips.reserved | reserved / is reserved / reservation status / reserved flag / ip reserved | tinyint(1) | schema / shadow_fixed_ips |
| shadow_fixed_ips.virtual_interface_id | virtual interface id / virtual interface identifier / vif id / interface identifier / associated vif | int | schema / shadow_fixed_ips |
| shadow_fixed_ips.host | host / compute host / host name / server host / physical host | varchar(255) | schema / shadow_fixed_ips |
| shadow_fixed_ips.instance_uuid | instance uuid / instance id / server uuid / associated instance | varchar(36) | schema / shadow_fixed_ips |
| shadow_fixed_ips.deleted | deleted / is deleted / deletion flag / soft delete flag / deleted status | int | schema / shadow_fixed_ips |

## shadow_floating_ips

Stores shadow or backup records of floating IP addresses, including their association with fixed IPs, projects, hosts, and network interfaces.

恢复表名: shadow floating ips / floating ip shadow / shadow public ips / shadow external ips / floating ip records / public ip shadow table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_floating_ips.created_at | created at / creation time / created date / timestamp created / record creation date | datetime | schema / shadow_floating_ips |
| shadow_floating_ips.updated_at | updated at / last updated / update time / modified date / last modification timestamp | datetime | schema / shadow_floating_ips |
| shadow_floating_ips.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / removal date | datetime | schema / shadow_floating_ips |
| shadow_floating_ips.id | id / identifier / primary key / record id / floating ip id / unique identifier | int | schema / shadow_floating_ips |
| shadow_floating_ips.address | address / ip address / public ip / floating ip address / external ip / ip addr | varchar(39) | schema / shadow_floating_ips |
| shadow_floating_ips.fixed_ip_id | fixed ip id / fixed ip identifier / private ip id / internal ip id / associated fixed ip | int | schema / shadow_floating_ips |
| shadow_floating_ips.project_id | project id / project identifier / tenant id / project uuid / owner project | varchar(255) | schema / shadow_floating_ips |
| shadow_floating_ips.host | host / compute host / server host / host name / physical host | varchar(255) | schema / shadow_floating_ips |
| shadow_floating_ips.auto_assigned | auto assigned / automatic assignment / auto assign flag / is auto assigned / auto allocation | tinyint(1) | schema / shadow_floating_ips |
| shadow_floating_ips.pool | pool / ip pool / address pool / floating ip pool / network pool | varchar(255) | schema / shadow_floating_ips |
| shadow_floating_ips.interface | interface / network interface / port interface / interface name / nic | varchar(255) | schema / shadow_floating_ips |
| shadow_floating_ips.deleted | deleted / is deleted / deletion flag / soft delete status / active status | int | schema / shadow_floating_ips |

## shadow_instance_actions

Records the history of actions performed on shadow instances, including creation, resizing, and other lifecycle events, along with associated user, project, and request details.

恢复表名: shadow instance actions / instance actions / instance operation logs / instance activity history / compute instance events / instance lifecycle actions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_actions.created_at | created at / creation time / record created / timestamp created / date created / inserted at | datetime | schema / shadow_instance_actions |
| shadow_instance_actions.updated_at | updated at / last updated / modification time / record updated / date updated / last modified | datetime | schema / shadow_instance_actions |
| shadow_instance_actions.deleted_at | deleted at / deletion time / soft delete timestamp / record deleted / date deleted / removed at | datetime | schema / shadow_instance_actions |
| shadow_instance_actions.id | id / identifier / action id / primary key / record id / unique identifier / action identifier | int | schema / shadow_instance_actions |
| shadow_instance_actions.action | action / operation type / action type / event type / instance operation / lifecycle event | varchar(255) | schema / shadow_instance_actions |
| shadow_instance_actions.instance_uuid | instance uuid / instance id / compute instance identifier / server uuid / instance unique id | varchar(36) | schema / shadow_instance_actions |
| shadow_instance_actions.request_id | request id / request identifier / api request id / transaction id / request uuid / correlation id | varchar(255) | schema / shadow_instance_actions |
| shadow_instance_actions.user_id | user id / user identifier / account id / owner id / user uuid / performer id | varchar(255) | schema / shadow_instance_actions |
| shadow_instance_actions.project_id | project id / project identifier / tenant id / project uuid / organization id / project owner id | varchar(255) | schema / shadow_instance_actions |
| shadow_instance_actions.start_time | start time / action start / operation start time / begin time / start timestamp / initiation time | datetime | schema / shadow_instance_actions |
| shadow_instance_actions.finish_time | finish time / action end / operation finish time / completion time / end timestamp / stop time | datetime | schema / shadow_instance_actions |
| shadow_instance_actions.message | message / error message / status message / action description / result message / log message | varchar(255) | schema / shadow_instance_actions |
| shadow_instance_actions.deleted | deleted / deleted flag / soft delete flag / is deleted / deletion status / removed flag | int | schema / shadow_instance_actions |

## shadow_instance_actions_events

Records individual events associated with instance actions, such as scheduling or compute runs, including timing, results, and error details.

恢复表名: shadow instance actions events / instance action events / shadow instance events / action event log / instance action history / compute run events / schedule events
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_actions_events.created_at | created at / creation time / record created / event creation date / timestamp created | datetime | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.updated_at | updated at / last updated / modification time / update timestamp / last modified date | datetime | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / archived date | datetime | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.id | id / identifier / event id / primary key / record id / unique identifier | int | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.event | event / event type / action type / event name / operation type | varchar(255) | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.action_id | action id / action identifier / parent action id / related action / action reference | int | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.start_time | start time / event start / begin time / start timestamp / initiation time | datetime | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.finish_time | finish time / event end / completion time / end timestamp / finish date | datetime | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.result | result / event result / status / outcome / success flag | varchar(255) | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.traceback | traceback / error traceback / stack trace / exception details / error log | text | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.deleted | deleted / deleted flag / soft delete id / deletion marker / is deleted | int | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.host | host / hostname / server name / machine host / execution host | varchar(255) | schema / shadow_instance_actions_events |
| shadow_instance_actions_events.details | details / event details / description / additional info / metadata | text | schema / shadow_instance_actions_events |

## shadow_instance_extra

Stores additional metadata and configuration details for Nova shadow instances, including hardware topology, flavor, and lifecycle timestamps.

恢复表名: shadow instance extra / instance extra / shadow instance metadata / instance additional info / nova shadow instance
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_extra.created_at | created at / creation time / created date / record created / instance creation timestamp | datetime | schema / shadow_instance_extra |
| shadow_instance_extra.updated_at | updated at / last updated / modification time / update timestamp / last modified date | datetime | schema / shadow_instance_extra |
| shadow_instance_extra.deleted_at | deleted at / deletion time / deleted date / removal timestamp / instance deleted when | datetime | schema / shadow_instance_extra |
| shadow_instance_extra.deleted | deleted / deletion flag / is deleted / soft delete status / deleted indicator | int | schema / shadow_instance_extra |
| shadow_instance_extra.id | id / identifier / primary key / record id / instance extra id / unique identifier | int | schema / shadow_instance_extra |
| shadow_instance_extra.instance_uuid | instance uuid / instance unique id / vm uuid / instance identifier | varchar(36) | schema / shadow_instance_extra |
| shadow_instance_extra.numa_topology | numa topology / numa configuration / node topology / numa layout | text | schema / shadow_instance_extra |
| shadow_instance_extra.pci_requests | pci requests / pci devices / pci configuration / pci passthrough | text | schema / shadow_instance_extra |
| shadow_instance_extra.flavor | flavor / instance flavor / vm flavor / flavor id | text | schema / shadow_instance_extra |
| shadow_instance_extra.vcpu_model | vcpu model / cpu model / virtual cpu model / cpu architecture | text | schema / shadow_instance_extra |
| shadow_instance_extra.migration_context | migration context / migration data / live migration info / migration state | text | schema / shadow_instance_extra |

## shadow_instance_faults

Stores records of faults, errors, or exceptions associated with specific virtual machine instances, including error codes, messages, and timestamps.

恢复表名: shadow instance faults / instance faults / shadow faults / virtual machine errors / instance error logs / fault records / instance exceptions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_faults.created_at | created at / creation time / fault start time / record created / timestamp / when fault occurred | datetime | schema / shadow_instance_faults |
| shadow_instance_faults.updated_at | updated at / last modified / update time / last updated / modification timestamp | datetime | schema / shadow_instance_faults |
| shadow_instance_faults.deleted_at | deleted at / deletion time / removed at / soft delete timestamp / archived at | datetime | schema / shadow_instance_faults |
| shadow_instance_faults.id | id / identifier / fault id / record id / primary key / unique identifier | int | schema / shadow_instance_faults |
| shadow_instance_faults.instance_uuid | instance uuid / instance id / vm uuid / virtual machine id / instance identifier / server uuid | varchar(36) | schema / shadow_instance_faults |
| shadow_instance_faults.code | code / error code / fault code / status code / http code / exception code | int | schema / shadow_instance_faults |
| shadow_instance_faults.message | message / error message / fault message / exception message / description / error text | varchar(255) | schema / shadow_instance_faults |
| shadow_instance_faults.details | details / fault details / error details / stack trace / exception details / full description | text | schema / shadow_instance_faults |
| shadow_instance_faults.host | host / hostname / server name / host name / machine name | varchar(255) | schema / shadow_instance_faults |
| shadow_instance_faults.deleted | deleted / deletion flag / is deleted / soft delete flag / status code / deletion status | int | schema / shadow_instance_faults |

## shadow_instance_group_member

Tracks the membership relationship between shadow instances and their associated groups, including creation, update, and deletion timestamps.

恢复表名: shadow instance group member / instance group membership / shadow group member / instance group association / shadow instance group
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_group_member.created_at | created at / creation time / created date / timestamp created / record created / start time | datetime | schema / shadow_instance_group_member |
| shadow_instance_group_member.updated_at | updated at / last updated / modification time / updated date / last modified / change timestamp | datetime | schema / shadow_instance_group_member |
| shadow_instance_group_member.deleted_at | deleted at / deletion time / deleted date / removal timestamp / soft delete time / archived at | datetime | schema / shadow_instance_group_member |
| shadow_instance_group_member.deleted | deleted / deletion flag / is deleted / soft delete indicator / removed status / deleted marker | int | schema / shadow_instance_group_member |
| shadow_instance_group_member.id | id / identifier / primary key / record id / membership id / unique identifier / row id | int | schema / shadow_instance_group_member |
| shadow_instance_group_member.instance_id | instance id / instance identifier / instance uuid / shadow instance id / virtual machine id / instance guid | varchar(255) | schema / shadow_instance_group_member |
| shadow_instance_group_member.group_id | group id / group identifier / instance group id / shadow group id / group number / associated group | int | schema / shadow_instance_group_member |

## shadow_instance_group_policy

Stores policy configurations (such as anti-affinity) applied to specific instance groups in the shadow environment.

恢复表名: shadow instance group policy / instance group policy / group policy / instance group rules / placement policy
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_group_policy.created_at | created at / creation date / created timestamp / policy creation time / when created | datetime | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.updated_at | updated at / last updated / modification time / update timestamp / when modified | datetime | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / when deleted | datetime | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.deleted | deleted / deletion flag / is deleted / soft delete status / deleted status | int | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.id | id / identifier / policy id / record id / primary key / unique identifier | int | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.policy | policy / policy type / placement rule / affinity setting / policy name | varchar(255) | schema / shadow_instance_group_policy |
| shadow_instance_group_policy.group_id | group id / group identifier / instance group id / associated group / group reference | int | schema / shadow_instance_group_policy |

## shadow_instance_groups

Stores metadata and lifecycle information for shadow instance groups, including ownership, project association, and soft-delete status.

恢复表名: shadow instance groups / instance groups / shadow groups / instance group records / shadow instance group table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_groups.created_at | created at / creation time / created date / creation timestamp / when created / record created | datetime | schema / shadow_instance_groups |
| shadow_instance_groups.updated_at | updated at / last updated / update time / modification date / last modified / update timestamp | datetime | schema / shadow_instance_groups |
| shadow_instance_groups.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / when deleted / removal time | datetime | schema / shadow_instance_groups |
| shadow_instance_groups.deleted | deleted / is deleted / deletion flag / soft delete status / deleted status / active status | int | schema / shadow_instance_groups |
| shadow_instance_groups.id | id / identifier / primary key / record id / group id / instance group id / unique identifier | int | schema / shadow_instance_groups |
| shadow_instance_groups.user_id | user id / user identifier / owner id / created by / account id / user reference | varchar(255) | schema / shadow_instance_groups |
| shadow_instance_groups.project_id | project id / project identifier / associated project / project reference / project uuid / project key | varchar(255) | schema / shadow_instance_groups |
| shadow_instance_groups.uuid | uuid / universal unique identifier / group uuid / external id / api id / unique string id | varchar(36) | schema / shadow_instance_groups |
| shadow_instance_groups.name | name / group name / instance group name / label / display name / title | varchar(255) | schema / shadow_instance_groups |

## shadow_instance_id_mappings

Stores mappings and metadata for shadow instances, including creation, update, and deletion timestamps and status flags.

恢复表名: shadow instance id mappings / shadow instance identifier mappings / shadow instance mappings / instance id mappings / shadow instance records / instance mapping table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_id_mappings.created_at | created at / creation date / created timestamp / record created / start date / inserted at | datetime | schema / shadow_instance_id_mappings |
| shadow_instance_id_mappings.updated_at | updated at / update date / last modified / updated timestamp / modification time / last updated | datetime | schema / shadow_instance_id_mappings |
| shadow_instance_id_mappings.deleted_at | deleted at / deletion date / deleted timestamp / removal date / soft delete time / archived at | datetime | schema / shadow_instance_id_mappings |
| shadow_instance_id_mappings.id | id / identifier / primary key / record id / mapping id / instance id / unique identifier | int | schema / shadow_instance_id_mappings |
| shadow_instance_id_mappings.uuid | uuid / universal unique identifier / guid / instance uuid / mapping uuid / unique string id | varchar(36) | schema / shadow_instance_id_mappings |
| shadow_instance_id_mappings.deleted | deleted / is deleted / deletion flag / active status / soft delete flag / removed status | int | schema / shadow_instance_id_mappings |

## shadow_instance_info_caches

Stores cached network and instance metadata for shadow instances in the Nova compute service, including creation, update, and deletion timestamps.

恢复表名: shadow instance info caches / instance info cache / shadow instance cache / instance network cache / nova shadow instance info
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_info_caches.created_at | created at / creation time / created date / record created / timestamp created / instance cache created | datetime | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.updated_at | updated at / update time / last updated / modified date / record updated / timestamp updated | datetime | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / record deleted / time deleted | datetime | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.id | id / identifier / primary key / record id / cache id / unique identifier / row id | int | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.network_info | network info / network details / instance network / network configuration / ip address info / bridge and subnet data / network json | text | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.instance_uuid | instance uuid / instance id / vm uuid / server uuid / instance identifier / virtual machine id | varchar(36) | schema / shadow_instance_info_caches |
| shadow_instance_info_caches.deleted | deleted / deleted flag / is deleted / soft delete flag / deletion status / record status | int | schema / shadow_instance_info_caches |

## shadow_instance_metadata

Stores key-value metadata pairs associated with specific shadow instances, including creation, update, and deletion timestamps and soft-delete status.

恢复表名: shadow instance metadata / instance metadata / shadow metadata / instance key value store / shadow instance attributes
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_metadata.created_at | created at / creation time / created date / record created / timestamp created / inserted at | datetime | schema / shadow_instance_metadata |
| shadow_instance_metadata.updated_at | updated at / last updated / modification time / updated date / last modified / change timestamp | datetime | schema / shadow_instance_metadata |
| shadow_instance_metadata.deleted_at | deleted at / deletion time / deleted date / removal timestamp / soft delete time / archived at | datetime | schema / shadow_instance_metadata |
| shadow_instance_metadata.id | id / identifier / primary key / record id / metadata id / row id / unique identifier | int | schema / shadow_instance_metadata |
| shadow_instance_metadata.key | key / metadata key / attribute name / property name / field name / label | varchar(255) | schema / shadow_instance_metadata |
| shadow_instance_metadata.value | value / metadata value / attribute value / property value / data value / content | varchar(255) | schema / shadow_instance_metadata |
| shadow_instance_metadata.instance_uuid | instance uuid / instance id / uuid / instance identifier / shadow instance id / unique instance id | varchar(36) | schema / shadow_instance_metadata |
| shadow_instance_metadata.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / removed | int | schema / shadow_instance_metadata |

## shadow_instance_system_metadata

Stores key-value pairs of system-level metadata and configuration attributes for shadow instances, such as instance type, memory, and CPU weights.

恢复表名: shadow instance system metadata / instance system metadata / shadow instance metadata / instance metadata / system metadata / instance properties / instance attributes
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_system_metadata.created_at | created at / creation date / created timestamp / record created / inserted at / creation time | datetime | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.updated_at | updated at / last updated / update timestamp / modified at / last modified / update date | datetime | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.deleted_at | deleted at / deletion date / deleted timestamp / removed at / soft delete time / deletion time | datetime | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.id | id / identifier / primary key / record id / metadata id / unique identifier / row id | int | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.instance_uuid | instance uuid / instance id / virtual machine id / vm uuid / instance identifier | varchar(36) | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.key | key / metadata key / attribute name / property name / field name / config key | varchar(255) | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.value | value / metadata value / attribute value / property value / data value / config value | varchar(255) | schema / shadow_instance_system_metadata |
| shadow_instance_system_metadata.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / shadow_instance_system_metadata |

## shadow_instance_type_extra_specs

Stores additional key-value specifications and attributes associated with instance types (flavors) in the Nova cloud computing platform.

恢复表名: shadow instance type extra specs / instance type extra specs / extra specs / instance type specifications / flavor extra specs / instance type attributes
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_type_extra_specs.created_at | created at / creation time / created date / record created / timestamp created / inserted at | datetime | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.updated_at | updated at / update time / last modified / modified date / updated timestamp / last updated | datetime | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / removed at / deletion timestamp | datetime | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.id | id / identifier / primary key / spec id / record id / unique identifier / extra spec id | int | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.instance_type_id | instance type id / instance type identifier / flavor id / flavor identifier / linked instance type | int | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.key | key / spec key / attribute name / property name / specification key / extra spec name | varchar(255) | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.value | value / spec value / attribute value / property value / specification value / extra spec data | varchar(255) | schema / shadow_instance_type_extra_specs |
| shadow_instance_type_extra_specs.deleted | deleted / deleted flag / is deleted / soft delete flag / deletion status / removed flag | int | schema / shadow_instance_type_extra_specs |

## shadow_instance_type_projects

Junction table linking instance types to projects, tracking the association status and timestamps for each relationship.

恢复表名: shadow instance type projects / instance type projects / instance project mapping / project instance types / instance type project associations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_type_projects.created_at | created at / creation date / created timestamp / start date / association start / when added | datetime | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.updated_at | updated at / last updated / modification date / update timestamp / last change / when modified | datetime | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / when deleted / removal time | datetime | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.id | id / identifier / primary key / record id / association id / link id / unique identifier | int | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.instance_type_id | instance type id / instance type identifier / instance type / type id / foreign key to instance types / type reference | int | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.project_id | project id / project identifier / project / project uuid / project reference / project hash | varchar(255) | schema / shadow_instance_type_projects |
| shadow_instance_type_projects.deleted | deleted / is deleted / deletion flag / soft delete status / active status / removed flag | int | schema / shadow_instance_type_projects |

## shadow_instance_types

Stores definitions and specifications for virtual machine instance types (flavors), including resource allocations like CPU, memory, and storage, as well as visibility and status flags.

恢复表名: shadow instance types / instance types / flavors / vm flavors / instance flavors / shadow flavors / compute flavors / instance type definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instance_types.created_at | created at / creation date / created timestamp / date created / record created | datetime | schema / shadow_instance_types |
| shadow_instance_types.updated_at | updated at / last updated / update timestamp / modified date / last modified | datetime | schema / shadow_instance_types |
| shadow_instance_types.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removed date | datetime | schema / shadow_instance_types |
| shadow_instance_types.name | name / flavor name / instance type name / type label / flavor identifier | varchar(255) | schema / shadow_instance_types |
| shadow_instance_types.id | id / identifier / instance type id / flavor id / primary key / type identifier | int | schema / shadow_instance_types |
| shadow_instance_types.memory_mb | memory mb / memory / ram / memory in mb / ram size / memory allocation | int | schema / shadow_instance_types |
| shadow_instance_types.vcpus | vcpus / cpu count / virtual cpus / number of cpus / cpu cores / vcpu count | int | schema / shadow_instance_types |
| shadow_instance_types.swap | swap / swap space / swap size / swap mb / virtual memory | int | schema / shadow_instance_types |
| shadow_instance_types.vcpu_weight | vcpu weight / cpu weight / vcpu priority / cpu scheduling weight / weight | int | schema / shadow_instance_types |
| shadow_instance_types.flavorid | flavorid / flavor uuid / external flavor id / nova flavor id / flavor reference | varchar(255) | schema / shadow_instance_types |
| shadow_instance_types.rxtx_factor | rxtx factor / rx tx factor / network factor / rxtx multiplier / network bandwidth factor | float | schema / shadow_instance_types |
| shadow_instance_types.root_gb | root gb / root disk size / root volume / root storage / root disk gb | int | schema / shadow_instance_types |
| shadow_instance_types.ephemeral_gb | ephemeral gb / ephemeral disk / local storage / ephemeral storage / ephemeral volume | int | schema / shadow_instance_types |
| shadow_instance_types.disabled | disabled / is disabled / disabled flag / active status / enabled | tinyint(1) | schema / shadow_instance_types |
| shadow_instance_types.is_public | is public / public flag / visibility / publicly available | tinyint(1) | schema / shadow_instance_types |
| shadow_instance_types.deleted | deleted / deleted flag / is deleted / soft delete flag / removed | int | schema / shadow_instance_types |

## shadow_instances

Stores metadata and lifecycle state for virtual machine instances in a cloud computing environment, including hardware specs, network details, and timestamps.

恢复表名: shadow instances / instances / virtual_machines / vm_instances / compute_instances / server_instances / nova_instances
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_instances.created_at | created at / creation_time / instance_created / start_date / creation_timestamp | datetime | schema / shadow_instances |
| shadow_instances.updated_at | updated at / last_modified / modification_time / update_timestamp / last_update | datetime | schema / shadow_instances |
| shadow_instances.deleted_at | deleted at / deletion_time / removed_at / soft_delete_time / termination_date | datetime | schema / shadow_instances |
| shadow_instances.id | id / identifier / instance_id / primary_key / record_id / vm_id | int | schema / shadow_instances |
| shadow_instances.internal_id | internal id / internal identifier / internal_identifier / sys_id / internal_ref / backend_id | int | schema / shadow_instances |
| shadow_instances.user_id | user id / user identifier / owner_id / tenant_id / account_id / customer_id | varchar(255) | schema / shadow_instances |
| shadow_instances.project_id | project id / project identifier / project_identifier / workspace_id / project_ref / org_id | varchar(255) | schema / shadow_instances |
| shadow_instances.image_ref | image ref / image reference / image_id / base_image / os_image_ref / template_id | varchar(255) | schema / shadow_instances |
| shadow_instances.kernel_id | kernel id / kernel identifier / kernel_ref / os_kernel_id / boot_kernel / kernel_identifier | varchar(255) | schema / shadow_instances |
| shadow_instances.ramdisk_id | ramdisk id / ramdisk identifier / ramdisk_ref / initramfs_id / boot_ramdisk / ramdisk_identifier | varchar(255) | schema / shadow_instances |
| shadow_instances.launch_index | launch index / launch_order / sequence_number / launch_seq / instance_index | int | schema / shadow_instances |
| shadow_instances.key_name | key name / ssh_key_name / access_key_name / keypair_name / credential_name | varchar(255) | schema / shadow_instances |
| shadow_instances.key_data | key data / public_key / key_material / ssh_public_key / credential_data | text | schema / shadow_instances |
| shadow_instances.power_state | power state / power_status / on_off_state / power_flag / running_state | int | schema / shadow_instances |
| shadow_instances.vm_state | vm state / instance_status / state / lifecycle_state / vm_status | varchar(255) | schema / shadow_instances |
| shadow_instances.memory_mb | memory mb / ram_mb / memory_size / ram_size / memory_allocation | int | schema / shadow_instances |
| shadow_instances.vcpus | vcpus / cpu_count / virtual_cpus / processor_count / cpu_cores | int | schema / shadow_instances |
| shadow_instances.hostname | hostname / instance_name / host_name / vm_name / server_name | varchar(255) | schema / shadow_instances |
| shadow_instances.host | host / compute_node / physical_host / hypervisor / host_server | varchar(255) | schema / shadow_instances |
| shadow_instances.user_data | user data / metadata / custom_data / user_script / instance_metadata | text | schema / shadow_instances |
| shadow_instances.reservation_id | reservation id / reservation identifier / reservation_ref / booking_id / resource_reservation / reservation_number | varchar(255) | schema / shadow_instances |
| shadow_instances.scheduled_at | scheduled at / schedule_time / planned_start / scheduling_timestamp / scheduled_date | datetime | schema / shadow_instances |
| shadow_instances.launched_at | launched at / start_time / launch_time / boot_time / instance_start | datetime | schema / shadow_instances |
| shadow_instances.terminated_at | terminated at / end_time / shutdown_time / stop_time / instance_end | datetime | schema / shadow_instances |
| shadow_instances.display_name | display name / name / instance_label / display_label / vm_label | varchar(255) | schema / shadow_instances |
| shadow_instances.display_description | display description / description / instance_notes / vm_description / notes | varchar(255) | schema / shadow_instances |
| shadow_instances.availability_zone | availability zone / az / zone / region_zone / datacenter_zone | varchar(255) | schema / shadow_instances |
| shadow_instances.locked | locked / is_locked / lock_status / locked_flag / access_locked | tinyint(1) | schema / shadow_instances |
| shadow_instances.os_type | os type / operating_system / os / guest_os / system_type | varchar(255) | schema / shadow_instances |
| shadow_instances.launched_on | launched on / launch_host / boot_node / initial_host / start_server | text | schema / shadow_instances |
| shadow_instances.instance_type_id | instance type id / instance type identifier / flavor_id / size_id / instance_size / type_ref | int | schema / shadow_instances |
| shadow_instances.vm_mode | vm mode / virtualization_mode / vm_type / mode / hypervisor_mode | varchar(255) | schema / shadow_instances |
| shadow_instances.uuid | uuid / unique_id / instance_uuid / global_id / uuid_ref | varchar(36) | schema / shadow_instances |
| shadow_instances.architecture | architecture / arch / cpu_architecture / system_arch / hardware_arch | varchar(255) | schema / shadow_instances |
| shadow_instances.root_device_name | root device name / root_disk / boot_device / root_partition / system_disk | varchar(255) | schema / shadow_instances |
| shadow_instances.access_ip_v4 | access ip v4 / ipv4 / ip_address / public_ip / v4_address | varchar(39) | schema / shadow_instances |
| shadow_instances.access_ip_v6 | access ip v6 | varchar(39) | schema / shadow_instances |
| shadow_instances.config_drive | config drive | varchar(255) | schema / shadow_instances |
| shadow_instances.task_state | task state | varchar(255) | schema / shadow_instances |
| shadow_instances.default_ephemeral_device | default ephemeral device | varchar(255) | schema / shadow_instances |
| shadow_instances.default_swap_device | default swap device | varchar(255) | schema / shadow_instances |
| shadow_instances.progress | progress | int | schema / shadow_instances |
| shadow_instances.auto_disk_config | auto disk config | tinyint(1) | schema / shadow_instances |
| shadow_instances.shutdown_terminate | shutdown terminate | tinyint(1) | schema / shadow_instances |
| shadow_instances.disable_terminate | disable terminate | tinyint(1) | schema / shadow_instances |
| shadow_instances.root_gb | root gb | int | schema / shadow_instances |
| shadow_instances.ephemeral_gb | ephemeral gb | int | schema / shadow_instances |
| shadow_instances.cell_name | cell name | varchar(255) | schema / shadow_instances |
| shadow_instances.node | node | varchar(255) | schema / shadow_instances |
| shadow_instances.deleted | deleted | int | schema / shadow_instances |
| shadow_instances.locked_by | locked by | enum('owner','admin') | schema / shadow_instances |
| shadow_instances.cleaned | cleaned | int | schema / shadow_instances |
| shadow_instances.ephemeral_key_uuid | ephemeral key uuid | varchar(36) | schema / shadow_instances |

## shadow_key_pairs

Stores user-specific cryptographic key pairs (SSH or X509) including their public keys, fingerprints, and lifecycle status.

恢复表名: shadow key pairs / key pairs / ssh keys / public keys / user keys / authentication keys / shadow keys
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_key_pairs.created_at | created at / creation date / created timestamp / key creation time / date created | datetime | schema / shadow_key_pairs |
| shadow_key_pairs.updated_at | updated at / last updated / modification date / update timestamp / last modified time | datetime | schema / shadow_key_pairs |
| shadow_key_pairs.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / date deleted | datetime | schema / shadow_key_pairs |
| shadow_key_pairs.id | id / identifier / key id / primary key / record id / key pair id | int | schema / shadow_key_pairs |
| shadow_key_pairs.name | name / key name / label / key title / display name | varchar(255) | schema / shadow_key_pairs |
| shadow_key_pairs.user_id | user id / user identifier / owner id / account id / user hash | varchar(255) | schema / shadow_key_pairs |
| shadow_key_pairs.fingerprint | fingerprint / key fingerprint / hash / md5 fingerprint / key hash | varchar(255) | schema / shadow_key_pairs |
| shadow_key_pairs.public_key | public key / public key data / key material / public key hash / key value | text | schema / shadow_key_pairs |
| shadow_key_pairs.deleted | deleted / is deleted / deletion flag / status / active status | int | schema / shadow_key_pairs |
| shadow_key_pairs.type | type / key type / protocol / algorithm / key format | enum('ssh','x509') | schema / shadow_key_pairs |

## shadow_migrate_version

Tracks the current migration version and repository path for shadow database migrations.

恢复表名: shadow migrate version / shadow migration version / migration version tracking / schema migration history / database migration state
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_migrate_version.repository_id | repository id / repository identifier / repo id / migration repo id / source repository id | varchar(250) | schema / shadow_migrate_version |
| shadow_migrate_version.repository_path | repository path / repo path / repository location / migration path / source path | text | schema / shadow_migrate_version |
| shadow_migrate_version.version | version / migration version / schema version / current version / version number | int | schema / shadow_migrate_version |

## shadow_migrations

Tracks the lifecycle, status, and progress of virtual machine instance migrations, resizes, and evacuations between compute nodes, including source/destination details and data transfer metrics.

恢复表名: shadow migrations / shadow_migrations / migration_records / instance_migrations / live_migrations / evacuation_records / resize_operations / compute_migrations
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_migrations.created_at | created at / creation_time / start_time / migration_start / record_created / initiated_at | datetime | schema / shadow_migrations |
| shadow_migrations.updated_at | updated at / last_update / modification_time / last_modified / status_update_time / recent_change | datetime | schema / shadow_migrations |
| shadow_migrations.deleted_at | deleted at / deletion_time / removed_at / soft_delete_time / archived_at / purge_time | datetime | schema / shadow_migrations |
| shadow_migrations.id | id / identifier / migration_id / record_id / primary_key / unique_identifier / migration_pk | int | schema / shadow_migrations |
| shadow_migrations.source_compute | source compute / source_host / origin_compute / from_compute / source_node_name / starting_compute | varchar(255) | schema / shadow_migrations |
| shadow_migrations.dest_compute | dest compute / destination_compute / target_compute / to_compute / destination_node_name / ending_compute | varchar(255) | schema / shadow_migrations |
| shadow_migrations.dest_host | dest host / destination_ip / target_ip / dest_address / destination_network / target_host_ip | varchar(255) | schema / shadow_migrations |
| shadow_migrations.status | status / migration_status / current_state / progress_state / operation_status / phase | varchar(255) | schema / shadow_migrations |
| shadow_migrations.instance_uuid | instance uuid / vm_uuid / instance_id / virtual_machine_id / server_uuid / guest_id | varchar(36) | schema / shadow_migrations |
| shadow_migrations.old_instance_type_id | old instance type id / old instance type identifier / previous_flavor_id / source_flavor_id / old_flavor / original_type_id / pre_resize_type | int | schema / shadow_migrations |
| shadow_migrations.new_instance_type_id | new instance type id / new instance type identifier / new_flavor_id / target_flavor_id / new_flavor / destination_type_id / post_resize_type | int | schema / shadow_migrations |
| shadow_migrations.source_node | source node / source_fqdn / origin_node / from_node / source_hostname / starting_node | varchar(255) | schema / shadow_migrations |
| shadow_migrations.dest_node | dest node / destination_fqdn / target_node / to_node / destination_hostname / ending_node | varchar(255) | schema / shadow_migrations |
| shadow_migrations.deleted | deleted / is_deleted / soft_delete_flag / removed_flag / deletion_indicator / active_flag | int | schema / shadow_migrations |
| shadow_migrations.migration_type | migration type / operation_type / migration_kind / action_type / move_type / resize_type | enum('migration','resize','live-migration','evacuation') | schema / shadow_migrations |
| shadow_migrations.hidden | hidden / is_hidden / visibility_flag / hidden_flag / display_status / visible | tinyint(1) | schema / shadow_migrations |
| shadow_migrations.memory_total | memory total / total_memory / mem_total / memory_size / total_ram / memory_capacity | bigint | schema / shadow_migrations |
| shadow_migrations.memory_processed | memory processed / memory_migrated / mem_processed / memory_transferred / memory_done / memory_complete | bigint | schema / shadow_migrations |
| shadow_migrations.memory_remaining | memory remaining / memory_left / mem_remaining / memory_pending / memory_to_go / memory_outstanding | bigint | schema / shadow_migrations |
| shadow_migrations.disk_total | disk total / total_disk / disk_size / total_storage / disk_capacity / total_block | bigint | schema / shadow_migrations |
| shadow_migrations.disk_processed | disk processed / disk_migrated / disk_processed / disk_transferred / disk_done / disk_complete | bigint | schema / shadow_migrations |
| shadow_migrations.disk_remaining | disk remaining / disk_left / disk_remaining / disk_pending / disk_to_go / disk_outstanding | bigint | schema / shadow_migrations |

## shadow_networks

Stores configuration details for virtual or shadow networks, including IP addressing, VLANs, DHCP settings, and VPN parameters.

恢复表名: shadow networks / networks / virtual networks / network configurations / subnet definitions / network settings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_networks.created_at | created at / creation date / created timestamp / date created / record created | datetime | schema / shadow_networks |
| shadow_networks.updated_at | updated at / update date / last modified / modified timestamp / date updated | datetime | schema / shadow_networks |
| shadow_networks.deleted_at | deleted at / deletion date / deleted timestamp / date deleted / removal time | datetime | schema / shadow_networks |
| shadow_networks.id | id / identifier / network id / primary key / record id / unique identifier | int | schema / shadow_networks |
| shadow_networks.injected | injected / injection flag / is injected / injected status / injection boolean | tinyint(1) | schema / shadow_networks |
| shadow_networks.cidr | cidr / ipv4 cidr / network cidr / subnet cidr / ip range | varchar(43) | schema / shadow_networks |
| shadow_networks.netmask | netmask / ipv4 netmask / subnet mask / network mask / mask | varchar(39) | schema / shadow_networks |
| shadow_networks.bridge | bridge / bridge name / network bridge / bridge device / br name | varchar(255) | schema / shadow_networks |
| shadow_networks.gateway | gateway / ipv4 gateway / default gateway / gateway ip / router ip | varchar(39) | schema / shadow_networks |
| shadow_networks.broadcast | broadcast / broadcast address / ipv4 broadcast / bcast ip / broadcast ip | varchar(39) | schema / shadow_networks |
| shadow_networks.dns1 | dns1 / primary dns / dns server 1 / first dns / main dns | varchar(39) | schema / shadow_networks |
| shadow_networks.vlan | vlan / vlan id / vlan number / virtual lan / vlan tag | int | schema / shadow_networks |
| shadow_networks.vpn_public_address | vpn public address / vpn public ip / public vpn address / vpn external ip / vpn public endpoint | varchar(39) | schema / shadow_networks |
| shadow_networks.vpn_public_port | vpn public port / vpn port / public vpn port / vpn external port | int | schema / shadow_networks |
| shadow_networks.vpn_private_address | vpn private address / vpn private ip / private vpn address / vpn internal ip / vpn private endpoint | varchar(39) | schema / shadow_networks |
| shadow_networks.dhcp_start | dhcp start / dhcp start ip / dhcp range start / first dhcp ip / dhcp pool start | varchar(39) | schema / shadow_networks |
| shadow_networks.project_id | project id / project identifier / project uuid / associated project / project ref | varchar(255) | schema / shadow_networks |
| shadow_networks.host | host / host name / server host / compute host / node host | varchar(255) | schema / shadow_networks |
| shadow_networks.cidr_v6 | cidr v6 / ipv6 cidr / ipv6 network / subnet v6 / ipv6 range | varchar(43) | schema / shadow_networks |
| shadow_networks.gateway_v6 | gateway v6 / ipv6 gateway / ipv6 router / v6 gateway ip | varchar(39) | schema / shadow_networks |
| shadow_networks.label | label / network label / display name / network name / label name | varchar(255) | schema / shadow_networks |
| shadow_networks.netmask_v6 | netmask v6 / ipv6 netmask / subnet mask v6 / network mask v6 / v6 mask | varchar(39) | schema / shadow_networks |
| shadow_networks.bridge_interface | bridge interface / bridge if / network interface / bridge dev / physical interface | varchar(255) | schema / shadow_networks |
| shadow_networks.multi_host | multi host / multi host flag / is multi host / multi host status / multi host boolean | tinyint(1) | schema / shadow_networks |
| shadow_networks.dns2 | dns2 / secondary dns / dns server 2 / second dns / backup dns | varchar(39) | schema / shadow_networks |
| shadow_networks.uuid | uuid / network uuid / unique id / universal id / uuid string | varchar(36) | schema / shadow_networks |
| shadow_networks.priority | priority / network priority / priority level / rank / order | int | schema / shadow_networks |
| shadow_networks.rxtx_base | rxtx base / rx tx base / base port / rxtx offset | int | schema / shadow_networks |
| shadow_networks.deleted | deleted / deleted flag / is deleted / deletion status / soft delete | int | schema / shadow_networks |
| shadow_networks.mtu | mtu / mtu size / max transmission unit / packet size / mtu value | int | schema / shadow_networks |
| shadow_networks.dhcp_server | dhcp server / dhcp server ip / dhcp host / dhcp address | varchar(39) | schema / shadow_networks |
| shadow_networks.enable_dhcp | enable dhcp / dhcp enabled / is dhcp on / dhcp flag / dhcp status | tinyint(1) | schema / shadow_networks |
| shadow_networks.share_address | share address / share address flag / is shared / address sharing / share ip | tinyint(1) | schema / shadow_networks |

## shadow_pci_devices

Stores shadow records for PCI devices, tracking their allocation status, physical addresses, vendor/product IDs, and association with compute nodes and instances.

恢复表名: shadow pci devices / pci_devices / pci_device / pci_device_shadow / pci_device_shadow_table
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_pci_devices.created_at | created at / creation_time / created_date / record_created / creation_timestamp / created | datetime | schema / shadow_pci_devices |
| shadow_pci_devices.updated_at | updated at / last_updated / update_time / modified_at / last_modified / updated | datetime | schema / shadow_pci_devices |
| shadow_pci_devices.deleted_at | deleted at / deletion_time / deleted_date / soft_delete_time / removed_at / deleted | datetime | schema / shadow_pci_devices |
| shadow_pci_devices.deleted | deleted / is_deleted / deletion_flag / soft_delete_flag / deleted_status | int | schema / shadow_pci_devices |
| shadow_pci_devices.id | id / identifier / device_id / primary_key / record_id / pci_id | int | schema / shadow_pci_devices |
| shadow_pci_devices.compute_node_id | compute node id / compute node identifier / node_id / compute_node / host_id / server_id | int | schema / shadow_pci_devices |
| shadow_pci_devices.address | address / pci_address / device_address / bus_address / pci_addr | varchar(12) | schema / shadow_pci_devices |
| shadow_pci_devices.product_id | product id / product identifier / product_code / device_product_id / product / product_id | varchar(4) | schema / shadow_pci_devices |
| shadow_pci_devices.vendor_id | vendor id / vendor identifier / vendor_code / device_vendor_id / vendor / vendor_id | varchar(4) | schema / shadow_pci_devices |
| shadow_pci_devices.dev_type | dev type / device_type / type / pci_type / dev_type | varchar(8) | schema / shadow_pci_devices |
| shadow_pci_devices.dev_id | dev id / dev identifier / device_identifier / unique_device_id / dev_id / device_id_string | varchar(255) | schema / shadow_pci_devices |
| shadow_pci_devices.label | label / device_label / name / label_name | varchar(255) | schema / shadow_pci_devices |
| shadow_pci_devices.status | status / device_status / allocation_status / state | varchar(36) | schema / shadow_pci_devices |
| shadow_pci_devices.extra_info | extra info / additional_info / metadata / extra_data / extra_info | text | schema / shadow_pci_devices |
| shadow_pci_devices.instance_uuid | instance uuid / instance_id / vm_id / server_uuid / instance / instance_uuid | varchar(36) | schema / shadow_pci_devices |
| shadow_pci_devices.request_id | request id / request identifier / request_uuid / api_request_id / request / request_id | varchar(36) | schema / shadow_pci_devices |
| shadow_pci_devices.numa_node | numa node / numa_id / numa_index / numa / numa_node | int | schema / shadow_pci_devices |
| shadow_pci_devices.parent_addr | parent addr / parent address / parent_address / parent_pci_address / parent / parent_addr | varchar(12) | schema / shadow_pci_devices |

## shadow_project_user_quotas

Stores resource usage limits and quotas assigned to specific users within specific projects in the Shadow system.

恢复表名: shadow project user quotas / project user quotas / user project limits / resource quotas / shadow quotas / project resource limits / user resource caps
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_project_user_quotas.id | id / identifier / quota id / record id / primary key / unique identifier | int | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.created_at | created at / creation date / created timestamp / start date / record created | datetime | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.deleted_at | deleted at / deletion date / removed at / soft delete timestamp / archived at | datetime | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.user_id | user id / user identifier / user / account id / owner id | varchar(255) | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.project_id | project id / project identifier / project / project code / workspace id | varchar(255) | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.resource | resource / resource type / resource name / quota resource / limit category | varchar(25) | schema / shadow_project_user_quotas |
| shadow_project_user_quotas.hard_limit | hard limit / maximum limit / cap / max value / upper bound / quota amount | int | schema / shadow_project_user_quotas |

## shadow_provider_fw_rules

Stores firewall rule definitions for shadow providers, specifying allowed network traffic based on protocol, port ranges, and CIDR blocks.

恢复表名: shadow provider fw rules / shadow provider firewall rules / provider firewall rules / shadow fw rules / firewall rules / network access rules / shadow provider network rules
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_provider_fw_rules.created_at | created at / creation date / created timestamp / rule creation time / when created | datetime | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.updated_at | updated at / update date / last modified / updated timestamp / modification time | datetime | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.deleted_at | deleted at / deletion date / deleted timestamp / removal time / when deleted | datetime | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.id | id / identifier / rule id / firewall rule id / primary key / rule identifier | int | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.protocol | protocol / network protocol / traffic protocol / ip protocol / protocol type | varchar(5) | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.from_port | from port / start port / source port / minimum port / port range start | int | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.to_port | to port / end port / destination port / maximum port / port range end | int | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.cidr | cidr / ip range / network address / source ip / cidr block | varchar(43) | schema / shadow_provider_fw_rules |
| shadow_provider_fw_rules.deleted | deleted / is deleted / deletion flag / soft delete / active status | int | schema / shadow_provider_fw_rules |

## shadow_quota_classes

Defines quota classes for shadow resources, specifying the resource type, class name, and hard limit constraints.

恢复表名: shadow quota classes / quota classes / shadow quota definitions / resource quota categories / quota class registry / shadow quota limits
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_quota_classes.created_at | created at / creation date / created timestamp / record created / start date | datetime | schema / shadow_quota_classes |
| shadow_quota_classes.updated_at | updated at / last modified date / update timestamp / last updated / modification time | datetime | schema / shadow_quota_classes |
| shadow_quota_classes.deleted_at | deleted at / deletion date / soft delete timestamp / removed at / archived date | datetime | schema / shadow_quota_classes |
| shadow_quota_classes.id | id / identifier / quota class id / primary key / record id / unique identifier | int | schema / shadow_quota_classes |
| shadow_quota_classes.class_name | class name / quota class name / class label / quota category name / name | varchar(255) | schema / shadow_quota_classes |
| shadow_quota_classes.resource | resource / resource type / resource name / quota resource / target resource | varchar(255) | schema / shadow_quota_classes |
| shadow_quota_classes.hard_limit | hard limit / maximum limit / quota cap / hard cap / max allowed value | int | schema / shadow_quota_classes |
| shadow_quota_classes.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / shadow_quota_classes |

## shadow_quota_usages

Tracks the consumption and reservation of specific resources (quotas) for projects and users, including current usage, reserved amounts, and refresh status.

恢复表名: shadow quota usages / quota usage records / resource quota tracking / shadow quota consumption / project quota usage / resource usage log
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_quota_usages.created_at | created at / creation time / record created / start date / timestamp created / when created | datetime | schema / shadow_quota_usages |
| shadow_quota_usages.updated_at | updated at / last updated / modification time / update timestamp / last modified / when updated | datetime | schema / shadow_quota_usages |
| shadow_quota_usages.deleted_at | deleted at / deletion time / soft delete timestamp / when deleted / removal date / archived at | datetime | schema / shadow_quota_usages |
| shadow_quota_usages.id | id / identifier / primary key / record id / usage id / unique identifier / row id | int | schema / shadow_quota_usages |
| shadow_quota_usages.project_id | project id / project identifier / project / associated project / project code / project ref | varchar(255) | schema / shadow_quota_usages |
| shadow_quota_usages.resource | resource / resource type / quota resource / resource name / resource kind / resource category | varchar(255) | schema / shadow_quota_usages |
| shadow_quota_usages.in_use | in use / current usage / used amount / active usage / consumed quantity / usage count | int | schema / shadow_quota_usages |
| shadow_quota_usages.reserved | reserved / reserved amount / held quantity / reserved quota / pending usage / reserved count | int | schema / shadow_quota_usages |
| shadow_quota_usages.until_refresh | until refresh / time to refresh / refresh interval / duration until reset / cooldown time / refresh countdown | int | schema / shadow_quota_usages |
| shadow_quota_usages.deleted | deleted / is deleted / deletion flag / soft delete status / removed flag / active status | int | schema / shadow_quota_usages |
| shadow_quota_usages.user_id | user id / user identifier / user / associated user / user code / user ref | varchar(255) | schema / shadow_quota_usages |

## shadow_quotas

Stores resource usage limits and quota configurations for specific projects, including hard limits and soft deletion status.

恢复表名: shadow quotas / quota limits / resource quotas / project quotas / shadow quota records
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_quotas.id | id / identifier / quota id / record id / primary key | int | schema / shadow_quotas |
| shadow_quotas.created_at | created at / creation date / created timestamp / start date / record created | datetime | schema / shadow_quotas |
| shadow_quotas.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / shadow_quotas |
| shadow_quotas.deleted_at | deleted at / deletion date / soft delete timestamp / removed at / deleted timestamp | datetime | schema / shadow_quotas |
| shadow_quotas.project_id | project id / project identifier / project reference / associated project / project key | varchar(255) | schema / shadow_quotas |
| shadow_quotas.resource | resource / resource type / quota resource / resource name / limited resource | varchar(255) | schema / shadow_quotas |
| shadow_quotas.hard_limit | hard limit / maximum limit / hard cap / quota value / max allowed / limit amount | int | schema / shadow_quotas |
| shadow_quotas.deleted | deleted / is deleted / deletion flag / active status / soft delete flag | int | schema / shadow_quotas |

## shadow_reservations

Tracks the creation, modification, and expiration of temporary resource reservations (quotas) for specific projects and users, including the type of resource and the quantity change.

恢复表名: shadow reservations / reservation logs / resource reservations / quota reservations / shadow quota / reservation history
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_reservations.created_at | created at / creation time / created date / reservation start time / timestamp created / when created | datetime | schema / shadow_reservations |
| shadow_reservations.updated_at | updated at / last updated / modification time / updated date / last modified / change timestamp | datetime | schema / shadow_reservations |
| shadow_reservations.deleted_at | deleted at / deletion time / deleted date / removal timestamp / when deleted / soft delete time | datetime | schema / shadow_reservations |
| shadow_reservations.id | id / identifier / reservation id / primary key / record id / unique id / row id | int | schema / shadow_reservations |
| shadow_reservations.uuid | uuid / universal unique identifier / reservation uuid / guid / unique string id / external id | varchar(36) | schema / shadow_reservations |
| shadow_reservations.usage_id | usage id / usage identifier / usage reference / usage record id / associated usage / usage link | int | schema / shadow_reservations |
| shadow_reservations.project_id | project id / project identifier / project uuid / project reference / associated project / project key | varchar(255) | schema / shadow_reservations |
| shadow_reservations.resource | resource / resource type / resource name / quota type / resource category / resource kind | varchar(255) | schema / shadow_reservations |
| shadow_reservations.delta | delta / quantity change / amount / delta value / reservation amount / change in quantity / units | int | schema / shadow_reservations |
| shadow_reservations.expire | expire / expiration time / expiry date / end time / valid until / expiration timestamp | datetime | schema / shadow_reservations |
| shadow_reservations.deleted | deleted / deletion flag / is deleted / soft delete flag / deleted status / active status | int | schema / shadow_reservations |
| shadow_reservations.user_id | user id / user identifier / user uuid / owner id / associated user / user reference | varchar(255) | schema / shadow_reservations |

## shadow_s3_images

Stores metadata and lifecycle status for S3 image objects, including creation, update, and deletion timestamps and soft-delete flags.

恢复表名: shadow s3 images / s3 image records / shadow storage images / s3 image metadata / image storage logs
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_s3_images.created_at | created at / creation date / created timestamp / image creation time / date created / record created | datetime | schema / shadow_s3_images |
| shadow_s3_images.updated_at | updated at / last updated / update timestamp / modification time / date updated / last modified | datetime | schema / shadow_s3_images |
| shadow_s3_images.deleted_at | deleted at / deletion date / deleted timestamp / removal time / date deleted / soft delete time | datetime | schema / shadow_s3_images |
| shadow_s3_images.id | id / identifier / primary key / record id / image id / internal id / row id | int | schema / shadow_s3_images |
| shadow_s3_images.uuid | uuid / unique identifier / universal unique identifier / image uuid / global id / external id | varchar(36) | schema / shadow_s3_images |
| shadow_s3_images.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / removed | int | schema / shadow_s3_images |

## shadow_security_group_default_rules

Stores the default inbound and outbound rule definitions for security groups, including protocol, port ranges, and CIDR blocks, with soft-delete tracking.

恢复表名: shadow security group default rules / security group default rules / default security group rules / shadow security group rules / sg default rules / default firewall rules / security group rule definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_security_group_default_rules.created_at | created at / creation time / created date / rule creation timestamp / when created / creation timestamp | datetime | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.updated_at | updated at / update time / last modified / modified date / last updated / update timestamp | datetime | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / when deleted / removal time | datetime | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.deleted | deleted / is deleted / deletion flag / soft delete status / active status / deleted indicator | int | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.id | id / identifier / rule id / primary key / rule identifier / unique id / record id | int | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.protocol | protocol / network protocol / ip protocol / traffic protocol / protocol type / communication protocol | varchar(5) | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.from_port | from port / start port / source port / minimum port / port range start / lower port bound | int | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.to_port | to port / end port / destination port / maximum port / port range end / upper port bound | int | schema / shadow_security_group_default_rules |
| shadow_security_group_default_rules.cidr | cidr / ip range / cidr block / source ip / destination ip / network address / ip address range | varchar(43) | schema / shadow_security_group_default_rules |

## shadow_security_group_instance_association

Tracks the many-to-many association between security groups and compute instances, including soft-delete status and audit timestamps.

恢复表名: shadow security group instance association / security group instance association / sg instance mapping / instance security group link / shadow sg instance join / security group to instance / instance to security group
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_security_group_instance_association.created_at | created at / creation time / created date / association start time / record created / timestamp created | datetime | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.updated_at | updated at / last modified time / update timestamp / last updated / modification date / record updated | datetime | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / disassociation time / deleted date | datetime | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.id | id / identifier / primary key / association id / record id / unique identifier / link id | int | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.security_group_id | security group id / security group identifier / sg id / group id / firewall group id / security group reference | int | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.instance_uuid | instance uuid / instance id / vm uuid / server uuid / compute instance identifier / instance unique id | varchar(36) | schema / shadow_security_group_instance_association |
| shadow_security_group_instance_association.deleted | deleted / is deleted / soft delete flag / active status / deletion status / removed flag | int | schema / shadow_security_group_instance_association |

## shadow_security_group_rules

Stores the specific network access control rules (protocol, port range, CIDR) associated with security groups, including their lifecycle timestamps and deletion status.

恢复表名: shadow security group rules / security group rules / firewall rules / network access rules / sg rules / security group rule definitions
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_security_group_rules.created_at | created at / creation date / created timestamp / rule creation time / when created / creation datetime | datetime | schema / shadow_security_group_rules |
| shadow_security_group_rules.updated_at | updated at / last updated / modification date / update timestamp / last modified time / update datetime | datetime | schema / shadow_security_group_rules |
| shadow_security_group_rules.deleted_at | deleted at / deletion date / deleted timestamp / removal time / when deleted / deletion datetime | datetime | schema / shadow_security_group_rules |
| shadow_security_group_rules.id | id / identifier / rule id / primary key / rule identifier / unique id / record id | int | schema / shadow_security_group_rules |
| shadow_security_group_rules.parent_group_id | parent group id / parent group identifier / parent security group id / group id / associated group / security group reference / parent group | int | schema / shadow_security_group_rules |
| shadow_security_group_rules.protocol | protocol / network protocol / ip protocol / traffic type / protocol type / communication protocol | varchar(255) | schema / shadow_security_group_rules |
| shadow_security_group_rules.from_port | from port / start port / source port / minimum port / port range start / lower port bound | int | schema / shadow_security_group_rules |
| shadow_security_group_rules.to_port | to port / end port / destination port / maximum port / port range end / upper port bound | int | schema / shadow_security_group_rules |
| shadow_security_group_rules.cidr | cidr / ip range / cidr block / source ip / network address / ip address range | varchar(43) | schema / shadow_security_group_rules |
| shadow_security_group_rules.group_id | group id / group identifier / security group id / sg id / associated group id / group reference | int | schema / shadow_security_group_rules |
| shadow_security_group_rules.deleted | deleted / is deleted / deletion flag / soft delete / active status / deleted status | int | schema / shadow_security_group_rules |

## shadow_security_groups

Stores metadata and lifecycle information for security groups, including ownership, project association, and soft-delete status.

恢复表名: shadow security groups / security groups / security group records / SG table / network security groups
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_security_groups.created_at | created at / creation date / created timestamp / date created / creation time | datetime | schema / shadow_security_groups |
| shadow_security_groups.updated_at | updated at / last updated / modification date / update timestamp / last modified | datetime | schema / shadow_security_groups |
| shadow_security_groups.deleted_at | deleted at / deletion date / deleted timestamp / date deleted / removal time | datetime | schema / shadow_security_groups |
| shadow_security_groups.id | id / identifier / security group id / primary key / record id / sg id | int | schema / shadow_security_groups |
| shadow_security_groups.name | name / security group name / group name / sg name / label | varchar(255) | schema / shadow_security_groups |
| shadow_security_groups.description | description / security group description / notes / details / group description | varchar(255) | schema / shadow_security_groups |
| shadow_security_groups.user_id | user id / user identifier / owner id / created by / account id | varchar(255) | schema / shadow_security_groups |
| shadow_security_groups.project_id | project id / project identifier / associated project / project code / project ref | varchar(255) | schema / shadow_security_groups |
| shadow_security_groups.deleted | deleted / is deleted / deletion flag / soft delete status / active status | int | schema / shadow_security_groups |

## shadow_services

Tracks the status, health, and lifecycle of OpenStack Nova services (such as scheduler, network, volume) across various hosts, including metrics like report counts and disabled states.

恢复表名: shadow services / service status / nova services / service health / service monitoring / service registry
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_services.created_at | created at / creation date / created timestamp / record created / service creation time | datetime | schema / shadow_services |
| shadow_services.updated_at | updated at / last updated / update timestamp / modified date / last modified | datetime | schema / shadow_services |
| shadow_services.deleted_at | deleted at / deletion date / deleted timestamp / removal time / soft delete time | datetime | schema / shadow_services |
| shadow_services.id | id / identifier / service id / primary key / record id / unique identifier | int | schema / shadow_services |
| shadow_services.host | host / hostname / server name / machine name / node / compute node | varchar(255) | schema / shadow_services |
| shadow_services.binary | binary / service binary / executable name / process name / service type / nova component | varchar(255) | schema / shadow_services |
| shadow_services.topic | topic / service topic / service category / component name / service short name | varchar(255) | schema / shadow_services |
| shadow_services.report_count | report count / number of reports / report total / heartbeat count / status reports | int | schema / shadow_services |
| shadow_services.disabled | disabled / is disabled / disabled flag / service disabled / enabled status | tinyint(1) | schema / shadow_services |
| shadow_services.deleted | deleted / is deleted / deleted flag / soft delete flag / removal status | int | schema / shadow_services |
| shadow_services.disabled_reason | disabled reason / reason for disabling / disable reason / deactivation reason / status reason | varchar(255) | schema / shadow_services |
| shadow_services.last_seen_up | last seen up / last up time / last heartbeat / last active time / last status check | datetime | schema / shadow_services |
| shadow_services.forced_down | forced down / is forced down / forced down flag / manually stopped / forced offline | tinyint(1) | schema / shadow_services |
| shadow_services.version | version / record version / data version / optimistic lock version / revision | int | schema / shadow_services |

## shadow_snapshot_id_mappings

Stores mappings between shadow snapshot identifiers and their corresponding system IDs, including metadata for creation, updates, and soft deletion.

恢复表名: shadow snapshot id mappings / shadow snapshot identifier mappings / snapshot id mapping / shadow snapshot mapping / id mapping table / snapshot identifier mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_snapshot_id_mappings.created_at | created at / creation date / created timestamp / record created / inserted at / creation time | datetime | schema / shadow_snapshot_id_mappings |
| shadow_snapshot_id_mappings.updated_at | updated at / update date / last updated / modified at / update timestamp / last modified time | datetime | schema / shadow_snapshot_id_mappings |
| shadow_snapshot_id_mappings.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / removed at / deletion time | datetime | schema / shadow_snapshot_id_mappings |
| shadow_snapshot_id_mappings.id | id / identifier / primary key / record id / mapping id / internal id / unique identifier | int | schema / shadow_snapshot_id_mappings |
| shadow_snapshot_id_mappings.uuid | uuid / universal unique identifier / guid / snapshot uuid / external id / unique string id | varchar(36) | schema / shadow_snapshot_id_mappings |
| shadow_snapshot_id_mappings.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / shadow_snapshot_id_mappings |

## shadow_snapshots

Stores metadata for shadow snapshots of storage volumes, including status, progress, ownership, and lifecycle timestamps.

恢复表名: shadow snapshots / snapshot table / volume snapshots / backup snapshots / shadow copies
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_snapshots.created_at | created at / creation time / created date / snapshot creation timestamp / when created | datetime | schema / shadow_snapshots |
| shadow_snapshots.updated_at | updated at / last updated / update time / modification timestamp / last modified | datetime | schema / shadow_snapshots |
| shadow_snapshots.deleted_at | deleted at / deletion time / deleted date / removal timestamp / when deleted | datetime | schema / shadow_snapshots |
| shadow_snapshots.id | id / identifier / snapshot id / unique identifier / primary key / snapshot uuid | varchar(36) | schema / shadow_snapshots |
| shadow_snapshots.volume_id | volume id / volume identifier / source volume id / parent volume / volume uuid | varchar(36) | schema / shadow_snapshots |
| shadow_snapshots.user_id | user id / user identifier / owner id / created by user / user uuid | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.project_id | project id / project identifier / tenant id / project uuid / associated project | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.status | status / snapshot state / current status / lifecycle state / progress state | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.progress | progress / completion percentage / progress percent / snapshot progress / percent complete | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.volume_size | volume size / size in gb / snapshot size / storage size / volume capacity | int | schema / shadow_snapshots |
| shadow_snapshots.scheduled_at | scheduled at / scheduled time / planned date / future schedule / scheduled timestamp | datetime | schema / shadow_snapshots |
| shadow_snapshots.display_name | display name / snapshot name / name / label / display label | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.display_description | display description / description / notes / snapshot description / details | varchar(255) | schema / shadow_snapshots |
| shadow_snapshots.deleted | deleted / deletion flag / is deleted / soft delete marker / deleted status | varchar(36) | schema / shadow_snapshots |

## shadow_task_log

Stores historical records of shadow task executions, including task status, host information, time periods, and error counts.

恢复表名: shadow task log / task log / shadow task history / task execution log / shadow job log / task audit trail
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_task_log.created_at | created at / creation time / created date / record created / timestamp created / log entry created | datetime | schema / shadow_task_log |
| shadow_task_log.updated_at | updated at / update time / last updated / modified date / record updated / timestamp updated | datetime | schema / shadow_task_log |
| shadow_task_log.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / record deleted / removal time | datetime | schema / shadow_task_log |
| shadow_task_log.id | id / identifier / primary key / log id / task log id / record id / unique identifier | int | schema / shadow_task_log |
| shadow_task_log.task_name | task name / name of task / task title / job name / shadow task name / task label | varchar(255) | schema / shadow_task_log |
| shadow_task_log.state | state / task status / execution state / current state / task condition / status | varchar(255) | schema / shadow_task_log |
| shadow_task_log.host | host / server name / machine host / execution host / node name / computer host | varchar(255) | schema / shadow_task_log |
| shadow_task_log.period_beginning | period beginning / start time / period start / task start date / beginning of period / execution start | datetime | schema / shadow_task_log |
| shadow_task_log.period_ending | period ending / end time / period end / task end date / end of period / execution end | datetime | schema / shadow_task_log |
| shadow_task_log.message | message / log message / status message / description / notes / task message | varchar(255) | schema / shadow_task_log |
| shadow_task_log.task_items | task items / number of items / item count / task item total / count of tasks / items processed | int | schema / shadow_task_log |
| shadow_task_log.errors | errors / error count / number of errors / failure count / error total / exceptions | int | schema / shadow_task_log |
| shadow_task_log.deleted | deleted / is deleted / deletion flag / soft delete flag / removed status / active status | int | schema / shadow_task_log |

## shadow_virtual_interfaces

Stores metadata for virtual network interfaces (VIFs) associated with compute instances, including their MAC addresses, network associations, and lifecycle timestamps.

恢复表名: shadow virtual interfaces / shadow_vifs / virtual_interfaces / vifs / network_interfaces / shadow_network_interfaces / instance_interfaces
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_virtual_interfaces.created_at | created at / creation_time / created_date / timestamp_created / vif_creation_time / interface_created | datetime | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.updated_at | updated at / last_updated / modification_time / updated_date / last_modified / vif_update_time | datetime | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.deleted_at | deleted at / deletion_time / deleted_date / removal_timestamp / vif_deleted_time / interface_removed_at | datetime | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.id | id / identifier / vif_id / interface_id / primary_key / record_id / shadow_vif_id | int | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.address | address / mac_address / mac / hardware_address / physical_address / vif_mac | varchar(255) | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.network_id | network id / network identifier / network / net_id / associated_network / vif_network / network_identifier | int | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.uuid | uuid / vif_uuid / interface_uuid / unique_id / global_id / vif_guid | varchar(36) | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.instance_uuid | instance uuid / instance_id / vm_uuid / server_uuid / associated_instance / vif_instance | varchar(36) | schema / shadow_virtual_interfaces |
| shadow_virtual_interfaces.deleted | deleted / is_deleted / deletion_flag / soft_delete / status_deleted / vif_deleted | int | schema / shadow_virtual_interfaces |

## shadow_volume_id_mappings

Stores mappings between shadow volume identifiers and their associated UUIDs, tracking creation, update, and deletion timestamps for audit and synchronization purposes.

恢复表名: shadow volume id mappings / shadow volume identifier mappings / shadow volume mappings / volume id mapping / shadow volume identifier mapping / volume uuid mapping
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_volume_id_mappings.created_at | created at / creation time / created date / record created / timestamp created / initial creation timestamp | datetime | schema / shadow_volume_id_mappings |
| shadow_volume_id_mappings.updated_at | updated at / last updated / update time / modified date / last modification timestamp / record updated | datetime | schema / shadow_volume_id_mappings |
| shadow_volume_id_mappings.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / record deleted / removal time | datetime | schema / shadow_volume_id_mappings |
| shadow_volume_id_mappings.id | id / identifier / primary key / record id / mapping id / internal id / unique identifier | int | schema / shadow_volume_id_mappings |
| shadow_volume_id_mappings.uuid | uuid / universal unique identifier / volume uuid / shadow volume uuid / guid / unique string id | varchar(36) | schema / shadow_volume_id_mappings |
| shadow_volume_id_mappings.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / record status | int | schema / shadow_volume_id_mappings |

## shadow_volume_usage_cache

Stores cached I/O usage statistics (reads, writes, bytes) for shadow volumes, tracking both total and current period metrics along with ownership and location details.

恢复表名: shadow volume usage cache / shadow volume usage / volume usage cache / shadow volume stats / volume I/O metrics / cached volume usage
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| shadow_volume_usage_cache.created_at | created at / creation time / record created / timestamp created / inserted at | datetime | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.updated_at | updated at / last updated / modification time / record updated / last modified | datetime | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.deleted_at | deleted at / deletion time / soft delete timestamp / removed at / archived at | datetime | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.id | id / identifier / primary key / record id / usage id / cache entry id | int | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.volume_id | volume id / volume identifier / volume uuid / storage volume id / block volume id | varchar(36) | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.tot_last_refreshed | tot last refreshed / total last refreshed / total last refresh / total stats updated / cumulative refresh time / total metrics timestamp | datetime | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.tot_reads | tot reads / total reads / total read count / cumulative reads / total I/O reads / lifetime read operations | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.tot_read_bytes | tot read bytes / total read bytes / total bytes read / cumulative read size / total read volume / lifetime read bytes | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.tot_writes | tot writes / total writes / total write count / cumulative writes / total I/O writes / lifetime write operations | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.tot_write_bytes | tot write bytes / total write bytes / total bytes written / cumulative write size / total write volume / lifetime write bytes | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.curr_last_refreshed | curr last refreshed / current last refresh / current stats updated / period refresh time / current metrics timestamp | datetime | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.curr_reads | curr reads / current read count / period reads / recent read operations / current I/O reads | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.curr_read_bytes | curr read bytes / current bytes read / period read size / recent read volume / current read data | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.curr_writes | curr writes / current write count / period writes / recent write operations / current I/O writes | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.curr_write_bytes | curr write bytes / current bytes written / period write size / recent write volume / current write data | bigint | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.deleted | deleted / is deleted / soft delete flag / deletion status / active status | int | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.instance_uuid | instance uuid / instance id / server uuid / compute instance id / vm id | varchar(36) | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.project_id | project id / project identifier / project uuid / tenant id / account id | varchar(36) | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.user_id | user id / user identifier / user uuid / owner id / account user id | varchar(36) | schema / shadow_volume_usage_cache |
| shadow_volume_usage_cache.availability_zone | availability zone / az / zone / data center zone / location zone | varchar(255) | schema / shadow_volume_usage_cache |

## snapshot_id_mappings

Stores mappings between internal snapshot identifiers and UUIDs, tracking creation, update, and deletion timestamps for soft-delete support.

恢复表名: snapshot id mappings / snapshot identifier mappings / snapshot mappings / id mappings / snapshot uuid mappings
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| snapshot_id_mappings.created_at | created at / creation date / created timestamp / record created / snapshot created / creation time | datetime | schema / snapshot_id_mappings |
| snapshot_id_mappings.updated_at | updated at / update date / last updated / modified timestamp / record updated / last modified | datetime | schema / snapshot_id_mappings |
| snapshot_id_mappings.deleted_at | deleted at / deletion date / deleted timestamp / soft delete time / record deleted / removal date | datetime | schema / snapshot_id_mappings |
| snapshot_id_mappings.id | id / identifier / primary key / record id / mapping id / internal id / snapshot mapping id | int | schema / snapshot_id_mappings |
| snapshot_id_mappings.uuid | uuid / universal unique identifier / snapshot uuid / mapping uuid / external id / guid | varchar(36) | schema / snapshot_id_mappings |
| snapshot_id_mappings.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / record status | int | schema / snapshot_id_mappings |

## snapshots

Stores metadata for point-in-time copies (snapshots) of block storage volumes in the Nova/Neutron cloud infrastructure.

恢复表名: snapshots / snapshot / volume snapshots / snapshot records / nova snapshots
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| snapshots.created_at | created at / creation time / created date / snapshot creation timestamp / when created / creation date | datetime | schema / snapshots |
| snapshots.updated_at | updated at / update time / last updated / modification time / updated date / last modified | datetime | schema / snapshots |
| snapshots.deleted_at | deleted at / deletion time / deleted date / removal time / when deleted / soft delete timestamp | datetime | schema / snapshots |
| snapshots.id | id / identifier / snapshot id / uuid / unique identifier / snapshot uuid / primary key | varchar(36) | schema / snapshots |
| snapshots.volume_id | volume id / volume identifier / volume uuid / source volume id / parent volume / associated volume / volume reference | varchar(36) | schema / snapshots |
| snapshots.user_id | user id / user identifier / owner id / user uuid / account id / created by / user reference | varchar(255) | schema / snapshots |
| snapshots.project_id | project id / project identifier / tenant id / project uuid / organization id / account project / project reference | varchar(255) | schema / snapshots |
| snapshots.status | status / snapshot state / current status / availability / state / snapshot condition | varchar(255) | schema / snapshots |
| snapshots.progress | progress / completion percentage / progress percent / snapshot progress / percent complete / progress status | varchar(255) | schema / snapshots |
| snapshots.volume_size | volume size / size in gb / snapshot size / capacity / volume capacity / size | int | schema / snapshots |
| snapshots.scheduled_at | scheduled at / scheduled time / planned date / future schedule / scheduled for / appointment time | datetime | schema / snapshots |
| snapshots.display_name | display name / name / snapshot name / label / title / display label | varchar(255) | schema / snapshots |
| snapshots.display_description | display description / description / notes / snapshot description / details / comment | varchar(255) | schema / snapshots |
| snapshots.deleted | deleted / is deleted / deletion flag / soft delete flag / removed / active status | varchar(36) | schema / snapshots |

## tags

Stores the association between resources and their assigned tags or labels.

恢复表名: tags / tagging / resource_tags / labels / metadata_tags
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| tags.resource_id | resource id / resource identifier / resource_id / resource / entity_id / object_id / linked_resource | varchar(36) | schema / tags |
| tags.tag | tag / label / tag_name / category / keyword / marker | varchar(80) | schema / tags |

## task_log

Stores historical records of scheduled task executions, including status, host, time periods, and error counts.

恢复表名: task log / task_log / task logs / task history / job log / job logs / scheduled task records / task execution log
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| task_log.created_at | created at / created_at / creation time / record created / log entry created / timestamp created | datetime | schema / task_log |
| task_log.updated_at | updated at / updated_at / last updated / modification time / record updated / last modified | datetime | schema / task_log |
| task_log.deleted_at | deleted at / deleted_at / deletion time / soft delete timestamp / record deleted / removed at | datetime | schema / task_log |
| task_log.id | id / identifier / task log id / record id / primary key / log identifier | int | schema / task_log |
| task_log.task_name | task name / task_name / job name / scheduled task / task title | varchar(255) | schema / task_log |
| task_log.state | state / task status / job state / execution status / task condition | varchar(255) | schema / task_log |
| task_log.host | host / server name / machine host / execution host / computer name | varchar(255) | schema / task_log |
| task_log.period_beginning | period beginning / period_beginning / start time / task start / period start / execution start | datetime | schema / task_log |
| task_log.period_ending | period ending / period_ending / end time / task end / period end / execution end | datetime | schema / task_log |
| task_log.message | message / log message / status message / error message / task notes | varchar(255) | schema / task_log |
| task_log.task_items | task items / task_items / item count / number of items / processed items / task item total | int | schema / task_log |
| task_log.errors | errors / error count / number of errors / failure count / error total | int | schema / task_log |
| task_log.deleted | deleted / is deleted / soft delete flag / record status / active flag | int | schema / task_log |

## virtual_interfaces

Stores metadata for virtual network interfaces (VIFs) attached to compute instances, including their IP addresses, network associations, and lifecycle status.

恢复表名: virtual interfaces / vifs / network interfaces / interface records / virtual network interfaces
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| virtual_interfaces.created_at | created at / creation time / created date / timestamp created / when created | datetime | schema / virtual_interfaces |
| virtual_interfaces.updated_at | updated at / last updated / modification time / updated date / last modified | datetime | schema / virtual_interfaces |
| virtual_interfaces.deleted_at | deleted at / deletion time / deleted date / soft delete timestamp / when deleted | datetime | schema / virtual_interfaces |
| virtual_interfaces.id | id / identifier / interface id / primary key / record id / vif id | int | schema / virtual_interfaces |
| virtual_interfaces.address | address / ip address / ip / network address / interface ip | varchar(255) | schema / virtual_interfaces |
| virtual_interfaces.network_id | network id / network identifier / associated network / vif network | int | schema / virtual_interfaces |
| virtual_interfaces.uuid | uuid / interface uuid / unique identifier / vif uuid / global id | varchar(36) | schema / virtual_interfaces |
| virtual_interfaces.instance_uuid | instance uuid / instance id / server uuid / vm uuid / associated instance | varchar(36) | schema / virtual_interfaces |
| virtual_interfaces.deleted | deleted / is deleted / deletion flag / soft delete flag / active status | int | schema / virtual_interfaces |

## volume_id_mappings

Stores mappings between internal volume identifiers and their unique UUIDs, including creation, update, and deletion timestamps.

恢复表名: volume id mappings / volume identifier mappings / volume mappings / volume uuid mappings / volume id map
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| volume_id_mappings.created_at | created at / creation date / created timestamp / record created / mapping created / creation time | datetime | schema / volume_id_mappings |
| volume_id_mappings.updated_at | updated at / update date / last updated / modified timestamp / record updated / last modification time | datetime | schema / volume_id_mappings |
| volume_id_mappings.deleted_at | deleted at / deletion date / deleted timestamp / record deleted / soft delete time / removal date | datetime | schema / volume_id_mappings |
| volume_id_mappings.id | id / identifier / primary key / record id / mapping id / internal id / row id | int | schema / volume_id_mappings |
| volume_id_mappings.uuid | uuid / volume uuid / unique identifier / volume unique id / guid / volume guid | varchar(36) | schema / volume_id_mappings |
| volume_id_mappings.deleted | deleted / is deleted / deletion flag / soft delete flag / active status / deleted status | int | schema / volume_id_mappings |

## volume_usage_cache

Stores cached cumulative and current I/O usage statistics (reads, writes, bytes) for block storage volumes, including timestamps for data refresh and volume metadata.

恢复表名: volume usage cache / volume usage statistics / volume I/O metrics / block storage usage / volume read write stats / storage volume performance
SQL表别名: —

| Physical | 恢复名称 | Type | 来源 |
|---|---|---|---|
| volume_usage_cache.created_at | created at / creation time / record created / inserted at / start date | datetime | schema / volume_usage_cache |
| volume_usage_cache.updated_at | updated at / last updated / modification time / record updated / change date | datetime | schema / volume_usage_cache |
| volume_usage_cache.deleted_at | deleted at / deletion time / removed at / soft delete date / archived at | datetime | schema / volume_usage_cache |
| volume_usage_cache.id | id / identifier / primary key / record id / usage id / unique identifier | int | schema / volume_usage_cache |
| volume_usage_cache.volume_id | volume id / volume identifier / volume uuid / block storage id / disk id / storage volume identifier | varchar(36) | schema / volume_usage_cache |
| volume_usage_cache.tot_last_refreshed | tot last refreshed / total last refreshed / total last refresh / cumulative refresh time / total stats updated / lifetime refresh date | datetime | schema / volume_usage_cache |
| volume_usage_cache.tot_reads | tot reads / total reads / cumulative read count / lifetime reads / total read operations | bigint | schema / volume_usage_cache |
| volume_usage_cache.tot_read_bytes | tot read bytes / total read bytes / cumulative read size / lifetime read data / total bytes read | bigint | schema / volume_usage_cache |
| volume_usage_cache.tot_writes | tot writes / total writes / cumulative write count / lifetime writes / total write operations | bigint | schema / volume_usage_cache |
| volume_usage_cache.tot_write_bytes | tot write bytes / total write bytes / cumulative write size / lifetime write data / total bytes written | bigint | schema / volume_usage_cache |
| volume_usage_cache.curr_last_refreshed | curr last refreshed / current last refresh / current stats refresh time / period refresh date / current update time | datetime | schema / volume_usage_cache |
| volume_usage_cache.curr_reads | curr reads / current reads / period read count / recent reads / current read operations | bigint | schema / volume_usage_cache |
| volume_usage_cache.curr_read_bytes | curr read bytes / current read bytes / period read size / recent read data / current bytes read | bigint | schema / volume_usage_cache |
| volume_usage_cache.curr_writes | curr writes / current writes / period write count / recent writes / current write operations | bigint | schema / volume_usage_cache |
| volume_usage_cache.curr_write_bytes | curr write bytes / current write bytes / period write size / recent write data / current bytes written | bigint | schema / volume_usage_cache |
| volume_usage_cache.deleted | deleted / is deleted / deletion flag / soft delete status / active status | int | schema / volume_usage_cache |
| volume_usage_cache.instance_uuid | instance uuid / instance id / server uuid / vm id / compute instance identifier | varchar(36) | schema / volume_usage_cache |
| volume_usage_cache.project_id | project id / project identifier / project uuid / tenant id / account id | varchar(36) | schema / volume_usage_cache |
| volume_usage_cache.user_id | user id / user identifier / user uuid / owner id / account user | varchar(64) | schema / volume_usage_cache |
| volume_usage_cache.availability_zone | availability zone / az / zone / data center zone / region zone | varchar(255) | schema / volume_usage_cache |

## 表关系与连接依据

- aggregate_hosts.aggregate_id ↔ aggregate_metadata.aggregate_id; profile_name_value_compatibility
- aggregate_hosts.aggregate_id ↔ shadow_aggregate_hosts.aggregate_id; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ certificates.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ fixed_ips.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ migrations.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ networks.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ quotas.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- aggregate_hosts.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- aggregate_hosts.host ↔ compute_nodes.host; declared_or_materialized_relationship, profile_name_value_compatibility
- aggregate_hosts.host ↔ services.host; profile_name_value_compatibility
- aggregate_hosts.host ↔ shadow_instances.host; profile_name_value_compatibility
- aggregate_hosts.host ↔ shadow_services.host; profile_name_value_compatibility
- aggregate_metadata.aggregate_id ↔ shadow_aggregate_hosts.aggregate_id; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ certificates.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ fixed_ips.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ migrations.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ networks.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ quotas.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- aggregate_metadata.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- aggregate_metadata.key ↔ instance_type_extra_specs.key; profile_name_value_compatibility
- aggregate_metadata.key ↔ shadow_aggregate_metadata.key; profile_name_value_compatibility
- aggregates.deleted ↔ certificates.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ fixed_ips.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ migrations.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ networks.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ quotas.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- aggregates.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- aggregates.deleted_at ↔ shadow_aggregate_metadata.deleted_at; profile_name_value_compatibility
- block_device_mapping.boot_index ↔ shadow_block_device_mapping.boot_index; profile_name_value_compatibility
- block_device_mapping.created_at ↔ instance_actions.created_at; profile_name_value_compatibility
- block_device_mapping.created_at ↔ instance_actions_events.created_at; profile_name_value_compatibility
- block_device_mapping.created_at ↔ instance_info_caches.created_at; profile_name_value_compatibility
- block_device_mapping.created_at ↔ instance_system_metadata.created_at; profile_name_value_compatibility
- block_device_mapping.created_at ↔ instances.created_at; profile_name_value_compatibility
- block_device_mapping.delete_on_termination ↔ shadow_block_device_mapping.delete_on_termination; profile_name_value_compatibility
- block_device_mapping.deleted ↔ certificates.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ fixed_ips.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ migrations.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ networks.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ quotas.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- block_device_mapping.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- block_device_mapping.destination_type ↔ shadow_block_device_mapping.destination_type; profile_name_value_compatibility
- block_device_mapping.device_type ↔ shadow_block_device_mapping.device_type; profile_name_value_compatibility
- block_device_mapping.instance_uuid ↔ instance_actions.instance_uuid; profile_name_value_compatibility
- block_device_mapping.instance_uuid ↔ instance_info_caches.instance_uuid; profile_name_value_compatibility
- block_device_mapping.instance_uuid ↔ instance_system_metadata.instance_uuid; profile_name_value_compatibility
- block_device_mapping.source_type ↔ shadow_block_device_mapping.source_type; profile_name_value_compatibility
- certificates.deleted ↔ fixed_ips.deleted; profile_name_value_compatibility
- certificates.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_extra.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- certificates.deleted ↔ instances.deleted; profile_name_value_compatibility
- certificates.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- certificates.deleted ↔ migrations.deleted; profile_name_value_compatibility
- certificates.deleted ↔ networks.deleted; profile_name_value_compatibility
- certificates.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- certificates.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- certificates.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- certificates.deleted ↔ quotas.deleted; profile_name_value_compatibility
- certificates.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- certificates.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- certificates.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- certificates.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- certificates.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- certificates.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- certificates.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- certificates.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- certificates.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- certificates.project_id ↔ floating_ips.project_id; profile_name_value_compatibility
- certificates.project_id ↔ quotas.project_id; profile_name_value_compatibility
- certificates.project_id ↔ security_groups.project_id; profile_name_value_compatibility
- certificates.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- certificates.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- certificates.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- certificates.user_id ↔ security_groups.user_id; profile_name_value_compatibility
- certificates.user_id ↔ shadow_instance_actions.user_id; profile_name_value_compatibility
- certificates.user_id ↔ shadow_instances.user_id; profile_name_value_compatibility
- certificates.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- certificates.user_id ↔ snapshots.user_id; profile_name_value_compatibility
- compute_nodes.current_workload ↔ shadow_compute_nodes.current_workload; profile_name_value_compatibility
- compute_nodes.deleted ↔ instance_group_member.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ instance_types.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- compute_nodes.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- compute_nodes.host ↔ services.host; profile_name_value_compatibility
- compute_nodes.host ↔ shadow_instance_faults.host; profile_name_value_compatibility
- compute_nodes.host ↔ shadow_instances.host; profile_name_value_compatibility
- compute_nodes.host ↔ shadow_services.host; profile_name_value_compatibility
- compute_nodes.hypervisor_type ↔ shadow_compute_nodes.hypervisor_type; profile_name_value_compatibility
- compute_nodes.local_gb_used ↔ shadow_compute_nodes.local_gb_used; profile_name_value_compatibility
- compute_nodes.memory_mb_used ↔ shadow_compute_nodes.memory_mb_used; profile_name_value_compatibility
- compute_nodes.running_vms ↔ shadow_compute_nodes.running_vms; profile_name_value_compatibility
- compute_nodes.stats ↔ shadow_compute_nodes.stats; profile_name_value_compatibility
- compute_nodes.uuid ↔ resource_providers.uuid; declared_or_materialized_relationship
- compute_nodes.vcpus ↔ shadow_compute_nodes.vcpus; profile_name_value_compatibility
- compute_nodes.vcpus_used ↔ shadow_compute_nodes.vcpus_used; profile_name_value_compatibility
- fixed_ips.allocated ↔ shadow_fixed_ips.allocated; profile_name_value_compatibility
- fixed_ips.created_at ↔ shadow_fixed_ips.created_at; profile_name_value_compatibility
- fixed_ips.deleted ↔ floating_ips.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_extra.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ instances.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ migrations.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ networks.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ quotas.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- fixed_ips.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- fixed_ips.host ↔ shadow_instance_faults.host; profile_name_value_compatibility
- fixed_ips.leased ↔ shadow_fixed_ips.leased; profile_name_value_compatibility
- fixed_ips.network_id ↔ shadow_fixed_ips.network_id; profile_name_value_compatibility
- fixed_ips.network_id ↔ shadow_virtual_interfaces.network_id; profile_name_value_compatibility
- fixed_ips.reserved ↔ quota_usages.reserved; profile_name_value_compatibility
- fixed_ips.reserved ↔ shadow_fixed_ips.reserved; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_actions.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_extra.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ instances.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ migrations.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ networks.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ quotas.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- floating_ips.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- floating_ips.project_id ↔ instance_type_projects.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ quotas.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ security_groups.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ shadow_instance_actions.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- floating_ips.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- instance_actions.created_at ↔ instance_actions_events.created_at; profile_name_value_compatibility
- instance_actions.created_at ↔ instance_info_caches.created_at; profile_name_value_compatibility
- instance_actions.created_at ↔ instance_system_metadata.created_at; profile_name_value_compatibility
- instance_actions.created_at ↔ instances.created_at; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_actions_events.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_extra.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_actions.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_actions.instance_uuid ↔ instance_info_caches.instance_uuid; profile_name_value_compatibility
- instance_actions.instance_uuid ↔ instance_system_metadata.instance_uuid; profile_name_value_compatibility
- instance_actions.project_id ↔ instances.project_id; profile_name_value_compatibility
- instance_actions.user_id ↔ instances.user_id; profile_name_value_compatibility
- instance_actions_events.created_at ↔ instance_info_caches.created_at; profile_name_value_compatibility
- instance_actions_events.created_at ↔ instance_system_metadata.created_at; profile_name_value_compatibility
- instance_actions_events.created_at ↔ instances.created_at; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_extra.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_actions_events.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_actions_events.event ↔ shadow_instance_actions_events.event; profile_name_value_compatibility
- instance_actions_events.result ↔ shadow_instance_actions_events.result; profile_name_value_compatibility
- instance_extra.deleted ↔ instance_faults.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_extra.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_extra.instance_uuid ↔ instances.uuid; declared_or_materialized_relationship, target_disjoint_historical_join
- instance_extra.pci_requests ↔ shadow_instance_extra.pci_requests; profile_name_value_compatibility
- instance_faults.code ↔ shadow_instance_faults.code; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_faults.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ instance_group_policy.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ instance_types.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- instance_group_member.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- instance_group_member.deleted_at ↔ instance_group_policy.deleted_at; profile_name_value_compatibility
- instance_group_member.deleted_at ↔ instance_groups.deleted_at; profile_name_value_compatibility
- instance_group_member.group_id ↔ instance_group_policy.group_id; profile_name_value_compatibility
- instance_group_policy.created_at ↔ instance_groups.created_at; profile_name_value_compatibility
- instance_group_policy.deleted ↔ instance_groups.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ instance_types.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_group_policy.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_group_policy.deleted_at ↔ instance_groups.deleted_at; profile_name_value_compatibility
- instance_group_policy.policy ↔ shadow_instance_group_policy.policy; profile_name_value_compatibility
- instance_groups.deleted ↔ instance_id_mappings.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ instance_types.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_groups.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_groups.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- instance_groups.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- instance_groups.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instance_info_caches.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instance_metadata.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_id_mappings.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_info_caches.created_at ↔ instance_system_metadata.created_at; profile_name_value_compatibility
- instance_info_caches.created_at ↔ instances.created_at; profile_name_value_compatibility
- instance_info_caches.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_info_caches.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_info_caches.instance_uuid ↔ instance_system_metadata.instance_uuid; profile_name_value_compatibility
- instance_info_caches.instance_uuid ↔ instances.uuid; declared_or_materialized_relationship, target_disjoint_historical_join
- instance_metadata.deleted ↔ instance_system_metadata.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_metadata.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_system_metadata.created_at ↔ instances.created_at; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ instance_type_projects.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ instances.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ key_pairs.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_system_metadata.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_system_metadata.instance_uuid ↔ instances.uuid; declared_or_materialized_relationship, target_disjoint_historical_join
- instance_type_extra_specs.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_type_extra_specs.deleted_at ↔ instance_type_projects.deleted_at; profile_name_value_compatibility
- instance_type_extra_specs.instance_type_id ↔ instance_type_projects.instance_type_id; profile_name_value_compatibility
- instance_type_extra_specs.key ↔ shadow_instance_type_extra_specs.key; profile_name_value_compatibility
- instance_type_projects.deleted ↔ instance_types.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ networks.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instance_type_projects.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instance_type_projects.project_id ↔ security_groups.project_id; profile_name_value_compatibility
- instance_type_projects.project_id ↔ shadow_instance_actions.project_id; profile_name_value_compatibility
- instance_type_projects.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- instance_type_projects.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- instance_type_projects.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- instance_type_projects.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_instance_extra.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- instance_types.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- instance_types.disabled ↔ services.disabled; profile_name_value_compatibility
- instance_types.ephemeral_gb ↔ instances.ephemeral_gb; profile_name_value_compatibility
- instance_types.ephemeral_gb ↔ shadow_instances.ephemeral_gb; profile_name_value_compatibility
- instance_types.memory_mb ↔ instances.memory_mb; profile_name_value_compatibility
- instance_types.memory_mb ↔ shadow_instances.memory_mb; profile_name_value_compatibility
- instance_types.root_gb ↔ instances.root_gb; profile_name_value_compatibility
- instance_types.root_gb ↔ shadow_instances.root_gb; profile_name_value_compatibility
- instance_types.vcpus ↔ instances.vcpus; profile_name_value_compatibility
- instance_types.vcpus ↔ shadow_compute_nodes.vcpus; profile_name_value_compatibility
- instance_types.vcpus ↔ shadow_instances.vcpus; profile_name_value_compatibility
- instances.cleaned ↔ shadow_instances.cleaned; profile_name_value_compatibility
- instances.deleted ↔ migrations.deleted; profile_name_value_compatibility
- instances.deleted ↔ networks.deleted; profile_name_value_compatibility
- instances.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- instances.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- instances.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- instances.deleted ↔ quotas.deleted; profile_name_value_compatibility
- instances.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- instances.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- instances.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- instances.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- instances.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- instances.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- instances.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- instances.disable_terminate ↔ shadow_instances.disable_terminate; profile_name_value_compatibility
- instances.host ↔ migrations.dest_compute; declared_or_materialized_relationship, target_disjoint_historical_join
- instances.host ↔ migrations.source_compute; declared_or_materialized_relationship, target_disjoint_historical_join
- instances.host ↔ shadow_instance_faults.host; profile_name_value_compatibility
- instances.launch_index ↔ shadow_instances.launch_index; profile_name_value_compatibility
- instances.locked ↔ shadow_instances.locked; profile_name_value_compatibility
- instances.progress ↔ shadow_instances.progress; profile_name_value_compatibility
- instances.root_device_name ↔ shadow_instances.root_device_name; profile_name_value_compatibility
- instances.root_gb ↔ shadow_instances.root_gb; profile_name_value_compatibility
- instances.uuid ↔ migrations.instance_uuid; declared_or_materialized_relationship, target_disjoint_historical_join
- instances.vcpus ↔ shadow_compute_nodes.vcpus; profile_name_value_compatibility
- instances.vcpus ↔ shadow_instances.vcpus; profile_name_value_compatibility
- instances.vm_state ↔ shadow_instances.vm_state; profile_name_value_compatibility
- key_pairs.deleted ↔ migrations.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ networks.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ quotas.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- key_pairs.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- migrations.deleted ↔ networks.deleted; profile_name_value_compatibility
- migrations.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- migrations.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- migrations.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- migrations.deleted ↔ quotas.deleted; profile_name_value_compatibility
- migrations.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- migrations.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- migrations.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- migrations.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- migrations.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- migrations.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- migrations.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- migrations.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- migrations.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- migrations.hidden ↔ shadow_migrations.hidden; profile_name_value_compatibility
- networks.deleted ↔ pci_devices.deleted; profile_name_value_compatibility
- networks.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- networks.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- networks.deleted ↔ quotas.deleted; profile_name_value_compatibility
- networks.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- networks.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- networks.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- networks.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- networks.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- networks.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- networks.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- networks.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- networks.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- pci_devices.address ↔ shadow_pci_devices.address; profile_name_value_compatibility
- pci_devices.compute_node_id ↔ shadow_pci_devices.compute_node_id; profile_name_value_compatibility
- pci_devices.deleted ↔ quota_classes.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ quotas.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- pci_devices.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- pci_devices.dev_id ↔ shadow_pci_devices.dev_id; profile_name_value_compatibility
- pci_devices.dev_type ↔ shadow_pci_devices.dev_type; profile_name_value_compatibility
- pci_devices.extra_info ↔ shadow_pci_devices.extra_info; profile_name_value_compatibility
- pci_devices.label ↔ shadow_pci_devices.label; profile_name_value_compatibility
- pci_devices.numa_node ↔ shadow_pci_devices.numa_node; profile_name_value_compatibility
- pci_devices.product_id ↔ shadow_pci_devices.product_id; profile_name_value_compatibility
- pci_devices.vendor_id ↔ shadow_pci_devices.vendor_id; profile_name_value_compatibility
- quota_classes.deleted ↔ quota_usages.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ quotas.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- quota_classes.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- quota_classes.resource ↔ quotas.resource; profile_name_value_compatibility
- quota_classes.resource ↔ reservations.resource; profile_name_value_compatibility
- quota_classes.resource ↔ shadow_reservations.resource; profile_name_value_compatibility
- quota_usages.deleted ↔ quotas.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- quota_usages.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- quota_usages.id ↔ reservations.usage_id; declared_or_materialized_relationship
- quota_usages.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- quota_usages.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- quota_usages.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- quota_usages.reserved ↔ shadow_fixed_ips.reserved; profile_name_value_compatibility
- quotas.deleted ↔ s3_images.deleted; profile_name_value_compatibility
- quotas.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- quotas.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- quotas.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- quotas.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- quotas.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- quotas.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- quotas.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- quotas.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- quotas.project_id ↔ security_groups.project_id; profile_name_value_compatibility
- quotas.project_id ↔ shadow_instance_actions.project_id; profile_name_value_compatibility
- quotas.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- quotas.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- quotas.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- quotas.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- quotas.resource ↔ reservations.resource; profile_name_value_compatibility
- quotas.resource ↔ shadow_reservations.resource; profile_name_value_compatibility
- reservations.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- reservations.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- reservations.resource ↔ shadow_reservations.resource; profile_name_value_compatibility
- s3_images.deleted ↔ security_group_rules.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- s3_images.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- security_group_rules.cidr ↔ shadow_security_group_rules.cidr; profile_name_value_compatibility
- security_group_rules.deleted ↔ security_groups.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ shadow_block_device_mapping.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- security_group_rules.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- security_group_rules.from_port ↔ shadow_security_group_rules.from_port; profile_name_value_compatibility
- security_group_rules.parent_group_id ↔ security_groups.id; declared_or_materialized_relationship, target_disjoint_historical_join
- security_group_rules.protocol ↔ shadow_security_group_rules.protocol; profile_name_value_compatibility
- security_group_rules.to_port ↔ shadow_security_group_rules.to_port; profile_name_value_compatibility
- security_groups.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- security_groups.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- security_groups.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- security_groups.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- security_groups.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- security_groups.project_id ↔ shadow_instance_actions.project_id; profile_name_value_compatibility
- security_groups.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- security_groups.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- security_groups.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- security_groups.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- security_groups.user_id ↔ shadow_instance_actions.user_id; profile_name_value_compatibility
- security_groups.user_id ↔ shadow_instances.user_id; profile_name_value_compatibility
- security_groups.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- security_groups.user_id ↔ snapshots.user_id; profile_name_value_compatibility
- services.disabled ↔ shadow_services.disabled; profile_name_value_compatibility
- services.forced_down ↔ shadow_services.forced_down; profile_name_value_compatibility
- services.host ↔ shadow_instances.host; profile_name_value_compatibility
- services.host ↔ shadow_services.host; profile_name_value_compatibility
- services.version ↔ shadow_services.version; profile_name_value_compatibility
- shadow_aggregate_hosts.deleted ↔ shadow_compute_nodes.deleted; profile_name_value_compatibility
- shadow_block_device_mapping.deleted ↔ shadow_fixed_ips.deleted; profile_name_value_compatibility
- shadow_block_device_mapping.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- shadow_block_device_mapping.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- shadow_block_device_mapping.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- shadow_block_device_mapping.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- shadow_fixed_ips.deleted ↔ shadow_instance_system_metadata.deleted; profile_name_value_compatibility
- shadow_fixed_ips.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- shadow_fixed_ips.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- shadow_fixed_ips.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- shadow_fixed_ips.network_id ↔ shadow_virtual_interfaces.network_id; profile_name_value_compatibility
- shadow_instance_actions.created_at ↔ shadow_instance_actions_events.created_at; profile_name_value_compatibility
- shadow_instance_actions.created_at ↔ shadow_instance_system_metadata.created_at; profile_name_value_compatibility
- shadow_instance_actions.instance_uuid ↔ shadow_instance_system_metadata.instance_uuid; profile_name_value_compatibility
- shadow_instance_actions.project_id ↔ shadow_instance_type_projects.project_id; profile_name_value_compatibility
- shadow_instance_actions.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- shadow_instance_actions.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- shadow_instance_actions.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- shadow_instance_actions.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- shadow_instance_actions.user_id ↔ shadow_instances.user_id; profile_name_value_compatibility
- shadow_instance_actions.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- shadow_instance_actions.user_id ↔ snapshots.user_id; profile_name_value_compatibility
- shadow_instance_actions_events.created_at ↔ shadow_instance_system_metadata.created_at; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_instance_metadata.deleted; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- shadow_instance_extra.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_instance_group_member.group_id ↔ shadow_instance_group_policy.group_id; profile_name_value_compatibility
- shadow_instance_metadata.deleted ↔ shadow_instance_type_extra_specs.deleted; profile_name_value_compatibility
- shadow_instance_metadata.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- shadow_instance_metadata.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- shadow_instance_metadata.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- shadow_instance_metadata.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_instance_system_metadata.deleted ↔ shadow_migrations.deleted; profile_name_value_compatibility
- shadow_instance_system_metadata.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- shadow_instance_system_metadata.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- shadow_instance_type_extra_specs.deleted ↔ shadow_instances.deleted; profile_name_value_compatibility
- shadow_instance_type_extra_specs.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- shadow_instance_type_extra_specs.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- shadow_instance_type_extra_specs.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_instance_type_projects.project_id ↔ shadow_instances.project_id; profile_name_value_compatibility
- shadow_instance_type_projects.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- shadow_instance_type_projects.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- shadow_instance_type_projects.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- shadow_instances.deleted ↔ shadow_pci_devices.deleted; profile_name_value_compatibility
- shadow_instances.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- shadow_instances.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_instances.host ↔ shadow_services.host; profile_name_value_compatibility
- shadow_instances.project_id ↔ shadow_reservations.project_id; profile_name_value_compatibility
- shadow_instances.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- shadow_instances.project_id ↔ snapshots.project_id; profile_name_value_compatibility
- shadow_instances.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- shadow_instances.user_id ↔ snapshots.user_id; profile_name_value_compatibility
- shadow_key_pairs.user_id ↔ shadow_snapshots.user_id; profile_name_value_compatibility
- shadow_migrations.deleted ↔ snapshot_id_mappings.deleted; profile_name_value_compatibility
- shadow_migrations.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility
- shadow_pci_devices.deleted ↔ shadow_reservations.deleted; profile_name_value_compatibility
- shadow_pci_devices.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_reservations.deleted ↔ shadow_services.deleted; profile_name_value_compatibility
- shadow_reservations.project_id ↔ shadow_snapshots.project_id; profile_name_value_compatibility
- shadow_snapshots.volume_id ↔ snapshots.volume_id; profile_name_value_compatibility
- shadow_snapshots.volume_size ↔ snapshots.volume_size; profile_name_value_compatibility
- snapshot_id_mappings.deleted ↔ volume_id_mappings.deleted; profile_name_value_compatibility

## 业务口径、总体与粒度

### QEMU hypervisor type

```json
{
  "kind": "metric",
  "formula": "\"Aggregate ID 1\" is predicated by \"aggregates.id = '1'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.808eb5129fb4e42a2eaa"
  ]
}
```

### how many

```json
{
  "kind": "metric",
  "formula": "\"Aggregate ID 1\" is predicated by \"aggregates.id = '1'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.52787a5a1d59840fbd7e"
  ]
}
```

### extra record creation timestamp

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cc6466ce1a74c3d7b08b"
  ]
}
```

### non-deleted instances

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9e7078e7b93cd1db42a7"
  ]
}
```

### instance flavor JSON

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a9e0ab8ba566e79bd1e6"
  ]
}
```

### INSTANCE_EXTRA id

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.61a140232b411440d7d5"
  ]
}
```

### instance UUID

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f9ab417c9b4a5629c40d"
  ]
}
```

### instance-extra NUMA topology JSON

```json
{
  "kind": "metric",
  "formula": "\"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.667c7aededece26d045c"
  ]
}
```

### non-empty PCI requests value

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"non-empty PCI requests value\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.4f9cdf72063b35d670c2\", \"physical_identifier\": \"instance_extra.pci_requests\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4f9cdf72063b35d670c2"
  ]
}
```

### non-deleted network info cache

```json
{
  "kind": "metric",
  "formula": "\"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.55b02c4868e91eac937a"
  ]
}
```

### cache record ID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.dd51a4046321960018fc"
  ]
}
```

### instance

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b7401137729ac42438a0"
  ]
}
```

### network info

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c7889a0d856ea8c9433a"
  ]
}
```

### time between when the instance was created and when its network info cache record was last updated

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2141bc9ae3c4766f6a6c"
  ]
}
```

### metadata deleted flag

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6b17f88592d75d29e113"
  ]
}
```

### system metadata ID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5ae8340b1c1e741818b5"
  ]
}
```

### UUID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2ff80bbba73644d90c48"
  ]
}
```

### key name

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ed33b50f088c5ce6bf9f"
  ]
}
```

### metadata value

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e6df43306e711628edef"
  ]
}
```

### availability zone

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8a19945b05ee1f61c37c"
  ]
}
```

### average days to launch

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.de0a220f3e54425ada1e"
  ]
}
```

### not deleted

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.7b00f82d71aff52df2fb"
  ]
}
```

### forge

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.5cd5e44d083f7bfbc740"
  ]
}
```

### hostname

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.660ca9b88a396172c7e4"
  ]
}
```

### instance ID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.01999b88ccebb57c3841"
  ]
}
```

### instance type (INSTANCE_TYPE_ID)

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c3e14f39487108fce530"
  ]
}
```

### key name

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.9e5d178872770a8d281e"
  ]
}
```

### launched in 2014

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0d3de916fa749ae210e6"
  ]
}
```

### range

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f2299ff311971c6e7ec1"
  ]
}
```

### power state

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.66eacec77f30e958bdb2"
  ]
}
```

### project ID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4b0dc400818375f25e45"
  ]
}
```

### average

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.edc1ef029759f5bd7a50"
  ]
}
```

### user ID

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'flare'\" is predicated by \"instances.display_name REGEXP 'flare'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.c6b612ff3e9bd4be9e20"
  ]
}
```

### UUID

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.684974bcafdfc81aa5f5"
  ]
}
```

### VCPUs

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.08af9d53e2bb13858246"
  ]
}
```

### VM state

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.2d30a0bb347ed55a6bf9"
  ]
}
```

### migration created timestamp

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e03e0f5a8b9b5e4f2223"
  ]
}
```

### migrations not deleted

```json
{
  "kind": "metric",
  "formula": "\"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\" | Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a740b9c106bdb2b3dd35"
  ]
}
```

### destination compute

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.a5fd43285cb465638ce9"
  ]
}
```

### destination host

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.64a8a9ab505fcbc9c4cb"
  ]
}
```

### migrations that are not hidden

```json
{
  "kind": "metric",
  "formula": "\"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\" | Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f0951dd6cb963991e4d0"
  ]
}
```

### migration

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | \"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.bc11227eafab52b89577"
  ]
}
```

### how many

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.6454807eccec0d68a145"
  ]
}
```

### memory processed

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.679bb945678e6794742e"
  ]
}
```

### memory remaining

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ac7a6cbd0cb179cc1c24"
  ]
}
```

### migrations

```json
{
  "kind": "metric",
  "formula": "Host \"prime-35\" is predicated by \"instances.host = 'prime-35'\" | \"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0a8fdcc83a89918a0452"
  ]
}
```

### migration type

```json
{
  "kind": "metric",
  "formula": "Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.22ef80b3b000190189b3"
  ]
}
```

### source compute

```json
{
  "kind": "metric",
  "formula": "\"Display 'prime'\" is predicated by \"instances.display_name REGEXP 'prime'\" | Host \"ether-18\" is predicated by \"instances.host = 'ether-18'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.e0efeb2eb1396d866dd6"
  ]
}
```

### status

```json
{
  "kind": "metric",
  "formula": "\"Active migrations\" is predicated by \"migrations.status NOT IN ('accepted', 'confirmed', 'reverted', 'error', 'failed', 'completed')\" | Host \"blaze8-12\" is predicated by \"instances.host = 'blaze8-12'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.ecba750eb853b5d73f7c"
  ]
}
```

### quota usage not deleted

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f1d4d309456669a63f3e"
  ]
}
```

### quota usage ID

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0576224df98d538f5593"
  ]
}
```

### in-use amount

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-05-13 16:53:07\" is predicated by \"reservations.expire < '2021-05-13 16:53:07'\" | \"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.0bfbc6b0cd27eeca8850"
  ]
}
```

### project id

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.d8c699d89e397927c84f"
  ]
}
```

### reserved amount

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"reserved amount\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.704c854ff901602fa14c\", \"physical_identifier\": \"quota_usages.reserved\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.704c854ff901602fa14c"
  ]
}
```

### resource

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4c4873dd667d3d9d64a0"
  ]
}
```

### reserved delta

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.af871bbdf0427769cf63"
  ]
}
```

### number of reservations

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f0cbdd03bcc40851f025"
  ]
}
```

### reservations whose resource is 'cores'

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-05-13 16:53:07\" is predicated by \"reservations.expire < '2021-05-13 16:53:07'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cb1087cffab6c3115940"
  ]
}
```

### linked reservations

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-11-16 19:30:59\" is predicated by \"reservations.expire < '2021-11-16 19:30:59'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cc53b9a747a019b8f2c0"
  ]
}
```

### reservation UUID

```json
{
  "kind": "metric",
  "formula": "\"Reservations expired before 2021-05-13 16:53:07\" is predicated by \"reservations.expire < '2021-05-13 16:53:07'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.4f113806f6477baf92c7"
  ]
}
```

### linked to a resource provider (matching on UUID)

```json
{
  "kind": "metric",
  "formula": "\"Aggregate ID 1\" is predicated by \"aggregates.id = '1'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.23754a878de6759c9223"
  ]
}
```

### CIDR

```json
{
  "kind": "metric",
  "formula": "\"Service binary nova-scheduler\" is predicated by \"services.binary = 'nova-scheduler'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1f37ad5563c3c88c3014"
  ]
}
```

### non-deleted rules

```json
{
  "kind": "metric",
  "formula": "\"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.f279b4a58844e55d2ed5"
  ]
}
```

### from port

```json
{
  "kind": "metric",
  "formula": "\"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.043d368af2b1e4a4702f"
  ]
}
```

### rules

```json
{
  "kind": "metric",
  "formula": "\"Service binary nova-scheduler\" is predicated by \"services.binary = 'nova-scheduler'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.29c599a6bff8351f10ea"
  ]
}
```

### security group rules

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"security group rules\", \"associated rule (join)\", \"associated security group rules\", \"parent group ID (ordering for window)\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.351f2cb02d9641c22e00\", \"physical_identifier\": \"security_group_rules.parent_group_id\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.351f2cb02d9641c22e00"
  ]
}
```

### protocol

```json
{
  "kind": "metric",
  "formula": "\"Service binary nova-scheduler\" is predicated by \"services.binary = 'nova-scheduler'\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.8eba4e0193f042c45f17"
  ]
}
```

### to port

```json
{
  "kind": "metric",
  "formula": "\"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.b1af5d06d79f94896af6"
  ]
}
```

### non-deleted groups

```json
{
  "kind": "metric",
  "formula": "\"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.541f88a76a63fef6af9c"
  ]
}
```

### description

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"description\", \"security group\", \"group description\", \"security group description\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.683f2051b98160660443\", \"physical_identifier\": \"security_groups.description\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.683f2051b98160660443"
  ]
}
```

### group ID

```json
{
  "kind": "metric",
  "formula": "\"Service binary nova-scheduler\" is predicated by \"services.binary = 'nova-scheduler'\" | \"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.26d223b633217081b96b"
  ]
}
```

### group name

```json
{
  "kind": "metric",
  "formula": "\"Service binary nova-scheduler\" is predicated by \"services.binary = 'nova-scheduler'\" | \"Enabled instance types\" is predicated by \"instance_types.disabled = false\"",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.cd1f1c2bfd6aa2192bb5"
  ]
}
```

### project ID

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"project ID\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.1a816980c7981e876cbd\", \"physical_identifier\": \"security_groups.project_id\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.1a816980c7981e876cbd"
  ]
}
```

### user ID

```json
{
  "kind": "metric",
  "formula": "{\"aliases\": [\"user ID\"], \"confidence\": 0.92, \"description\": \"\", \"evidence_id\": \"beaver_kb.67b782a8ee199accaa7e\", \"physical_identifier\": \"security_groups.user_id\", \"schema_context\": \"nova\", \"semantic_type\": \"unknown\", \"source_name\": \"BEAVER target-disjoint historical mapping and KB\"}",
  "grain": [],
  "population_scope": null,
  "upstream_scopes": [],
  "execution_contract": null,
  "source_history_ids": [
    "beaver_kb.67b782a8ee199accaa7e"
  ]
}
```


## 增量维护事件

