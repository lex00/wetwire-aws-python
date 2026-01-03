"""Network resources: CloudFrontCachePolicy, NetworkVPC, NetworkPrivateSubnet2RouteTable, NetworkInternetGateway, NetworkVPCGW, NetworkPublicSubnet2RouteTable, NetworkPublicSubnet2DefaultRoute, NetworkPublicSubnet2, NetworkPublicSubnet2RouteTableAssociation, NetworkPublicSubnet2EIP, NetworkPublicSubnet2NATGateway, NetworkPrivateSubnet2DefaultRoute, NetworkPrivateSubnet1Subnet, NetworkPublicSubnet1RouteTable, NetworkPublicSubnet1, NetworkPublicSubnet1RouteTableAssociation, NetworkPrivateSubnet2Subnet, NetworkPrivateSubnet2RouteTableAssociation, InstanceSecurityGroup, NetworkPublicSubnet1DefaultRoute, NetworkPrivateSubnet1RouteTable, NetworkPrivateSubnet1RouteTableAssociation, NetworkPublicSubnet1EIP, NetworkPublicSubnet1NATGateway, NetworkPrivateSubnet1DefaultRoute."""

from . import *  # noqa: F403


class CloudFrontCachePolicyCookiesConfig:
    resource: cloudfront.CachePolicy.CookiesConfig
    cookie_behavior = 'all'


class CloudFrontCachePolicyHeadersConfig:
    resource: cloudfront.CachePolicy.HeadersConfig
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


class CloudFrontCachePolicyQueryStringsConfig:
    resource: cloudfront.CachePolicy.QueryStringsConfig
    query_string_behavior = 'all'


class CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin:
    resource: cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin
    cookies_config = CloudFrontCachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CloudFrontCachePolicyHeadersConfig
    query_strings_config = CloudFrontCachePolicyQueryStringsConfig


class CloudFrontCachePolicyCachePolicyConfig:
    resource: cloudfront.CachePolicy.CachePolicyConfig
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = 'gitlab-server'
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicy:
    resource: cloudfront.CachePolicy
    cache_policy_config = CloudFrontCachePolicyCachePolicyConfig


class NetworkVPCAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


class NetworkVPC:
    resource: ec2.VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'
    tags = [NetworkVPCAssociationParameter]


class NetworkPrivateSubnet2RouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-2-rt'


class NetworkPrivateSubnet2RouteTable:
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet2RouteTableAssociationParameter]


class NetworkInternetGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server'


class NetworkInternetGateway:
    resource: ec2.InternetGateway
    tags = [NetworkInternetGatewayAssociationParameter]


class NetworkVPCGW:
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = NetworkInternetGateway
    vpc_id = NetworkVPC


class NetworkPublicSubnet2RouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-2-rt'


class NetworkPublicSubnet2RouteTable:
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet2RouteTableAssociationParameter]


class NetworkPublicSubnet2DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = NetworkInternetGateway
    route_table_id = NetworkPublicSubnet2RouteTable
    depends_on = [NetworkVPCGW]


class NetworkPublicSubnet2AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-2'


class NetworkPublicSubnet2:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet2AssociationParameter]


class NetworkPublicSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPublicSubnet2RouteTable
    subnet_id = NetworkPublicSubnet2


class NetworkPublicSubnet2EIPAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-eip'


class NetworkPublicSubnet2EIP:
    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet2EIPAssociationParameter]


class NetworkPublicSubnet2NATGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-ngw'


class NetworkPublicSubnet2NATGateway:
    resource: ec2.NatGateway
    allocation_id = NetworkPublicSubnet2EIP.AllocationId
    subnet_id = NetworkPublicSubnet2
    tags = [NetworkPublicSubnet2NATGatewayAssociationParameter]
    depends_on = [NetworkPublicSubnet2DefaultRoute, NetworkPublicSubnet2RouteTableAssociation]


class NetworkPrivateSubnet2DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NetworkPublicSubnet2NATGateway
    route_table_id = NetworkPrivateSubnet2RouteTable


class NetworkPrivateSubnet1SubnetAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1'


class NetworkPrivateSubnet1Subnet:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet1SubnetAssociationParameter]


class NetworkPublicSubnet1RouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-rt'


class NetworkPublicSubnet1RouteTable:
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet1RouteTableAssociationParameter]


class NetworkPublicSubnet1AssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1'


class NetworkPublicSubnet1:
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet1AssociationParameter]


class NetworkPublicSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPublicSubnet1RouteTable
    subnet_id = NetworkPublicSubnet1


class NetworkPrivateSubnet2SubnetAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-2'


class NetworkPrivateSubnet2Subnet:
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet2SubnetAssociationParameter]


class NetworkPrivateSubnet2RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPrivateSubnet2RouteTable
    subnet_id = NetworkPrivateSubnet2Subnet


class InstanceSecurityGroupIngress:
    resource: ec2.SecurityGroup.Ingress
    description = 'Allow HTTP from com.amazonaws.global.cloudfront.origin-facing'
    ip_protocol = 'tcp'
    from_port = 80
    to_port = 80
    source_prefix_list_id = FindInMap("Prefixes", AWS_REGION, 'PrefixList')


class InstanceSecurityGroupEgress:
    resource: ec2.SecurityGroup.Egress
    cidr_ip = '0.0.0.0/0'
    description = 'Allow all outbound traffic by default'
    ip_protocol = '-1'


class InstanceSecurityGroupAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-isg'


class InstanceSecurityGroup:
    resource: ec2.SecurityGroup
    group_description = 'gitlab-server-isg'
    security_group_ingress = [InstanceSecurityGroupIngress]
    security_group_egress = [InstanceSecurityGroupEgress]
    tags = [InstanceSecurityGroupAssociationParameter]
    vpc_id = NetworkVPC


class NetworkPublicSubnet1DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = NetworkInternetGateway
    route_table_id = NetworkPublicSubnet1RouteTable
    depends_on = [NetworkVPCGW]


class NetworkPrivateSubnet1RouteTableAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1-rt'


class NetworkPrivateSubnet1RouteTable:
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet1RouteTableAssociationParameter]


class NetworkPrivateSubnet1RouteTableAssociation:
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPrivateSubnet1RouteTable
    subnet_id = NetworkPrivateSubnet1Subnet


class NetworkPublicSubnet1EIPAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-eip'


class NetworkPublicSubnet1EIP:
    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet1EIPAssociationParameter]


class NetworkPublicSubnet1NATGatewayAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-ngw'


class NetworkPublicSubnet1NATGateway:
    resource: ec2.NatGateway
    allocation_id = NetworkPublicSubnet1EIP.AllocationId
    subnet_id = NetworkPublicSubnet1
    tags = [NetworkPublicSubnet1NATGatewayAssociationParameter]
    depends_on = [NetworkPublicSubnet1DefaultRoute, NetworkPublicSubnet1RouteTableAssociation]


class NetworkPrivateSubnet1DefaultRoute:
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NetworkPublicSubnet1NATGateway
    route_table_id = NetworkPrivateSubnet1RouteTable
