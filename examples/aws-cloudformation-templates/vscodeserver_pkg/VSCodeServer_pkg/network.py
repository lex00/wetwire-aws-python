"""Network resources: NetworkVPC, NetworkPublicSubnet1RouteTable, NetworkPublicSubnet1, NetworkPublicSubnet1RouteTableAssociation, NetworkPublicSubnet1EIP, NetworkInternetGateway, NetworkVPCGW, NetworkPublicSubnet1DefaultRoute, NetworkPublicSubnet1NATGateway, NetworkPublicSubnet2EIP, NetworkPublicSubnet2RouteTable, NetworkPublicSubnet2, NetworkPublicSubnet2RouteTableAssociation, NetworkPublicSubnet2DefaultRoute, NetworkPublicSubnet2NATGateway, NetworkPrivateSubnet1Subnet, NetworkPrivateSubnet1RouteTable, NetworkPrivateSubnet1RouteTableAssociation, InstanceSecurityGroup, NetworkPrivateSubnet1DefaultRoute, NetworkPrivateSubnet2Subnet, NetworkPrivateSubnet2RouteTable, NetworkPrivateSubnet2DefaultRoute, NetworkPrivateSubnet2RouteTableAssociation, CloudFrontCachePolicy."""

from . import *  # noqa: F403


class NetworkVPCAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server'


class NetworkVPC(ec2.VPC):
    resource: ec2.VPC
    cidr_block = '10.0.0.0/16'
    enable_dns_hostnames = True
    enable_dns_support = True
    instance_tenancy = 'default'
    tags = [NetworkVPCAssociationParameter]


class NetworkPublicSubnet1RouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-1-rt'


class NetworkPublicSubnet1RouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet1RouteTableAssociationParameter]


class NetworkPublicSubnet1AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-1'


class NetworkPublicSubnet1(ec2.Subnet):
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet1AssociationParameter]


class NetworkPublicSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPublicSubnet1RouteTable
    subnet_id = NetworkPublicSubnet1


class NetworkPublicSubnet1EIPAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-1-eip'


class NetworkPublicSubnet1EIP(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet1EIPAssociationParameter]


class NetworkInternetGatewayAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server'


class NetworkInternetGateway(ec2.InternetGateway):
    resource: ec2.InternetGateway
    tags = [NetworkInternetGatewayAssociationParameter]


class NetworkVPCGW(ec2.VPCGatewayAttachment):
    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = NetworkInternetGateway
    vpc_id = NetworkVPC


class NetworkPublicSubnet1DefaultRoute(ec2.Route):
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = NetworkInternetGateway
    route_table_id = NetworkPublicSubnet1RouteTable
    depends_on = [NetworkVPCGW]


class NetworkPublicSubnet1NATGatewayAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-1-ngw'


class NetworkPublicSubnet1NATGateway(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = NetworkPublicSubnet1EIP.AllocationId
    subnet_id = NetworkPublicSubnet1
    tags = [NetworkPublicSubnet1NATGatewayAssociationParameter]
    depends_on = [NetworkPublicSubnet1DefaultRoute, NetworkPublicSubnet1RouteTableAssociation]


class NetworkPublicSubnet2EIPAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-eip'


class NetworkPublicSubnet2EIP(ec2.EIP):
    resource: ec2.EIP
    domain = 'vpc'
    tags = [NetworkPublicSubnet2EIPAssociationParameter]


class NetworkPublicSubnet2RouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-2-rt'


class NetworkPublicSubnet2RouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet2RouteTableAssociationParameter]


class NetworkPublicSubnet2AssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-2'


class NetworkPublicSubnet2(ec2.Subnet):
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = NetworkVPC
    tags = [NetworkPublicSubnet2AssociationParameter]


class NetworkPublicSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPublicSubnet2RouteTable
    subnet_id = NetworkPublicSubnet2


class NetworkPublicSubnet2DefaultRoute(ec2.Route):
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = NetworkInternetGateway
    route_table_id = NetworkPublicSubnet2RouteTable
    depends_on = [NetworkVPCGW]


class NetworkPublicSubnet2NATGatewayAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-public-subnet-ngw'


class NetworkPublicSubnet2NATGateway(ec2.NatGateway):
    resource: ec2.NatGateway
    allocation_id = NetworkPublicSubnet2EIP.AllocationId
    subnet_id = NetworkPublicSubnet2
    tags = [NetworkPublicSubnet2NATGatewayAssociationParameter]
    depends_on = [NetworkPublicSubnet2DefaultRoute, NetworkPublicSubnet2RouteTableAssociation]


class NetworkPrivateSubnet1SubnetAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-private-subnet-1'


class NetworkPrivateSubnet1Subnet(ec2.Subnet):
    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet1SubnetAssociationParameter]


class NetworkPrivateSubnet1RouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-private-subnet-1-rt'


class NetworkPrivateSubnet1RouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet1RouteTableAssociationParameter]


class NetworkPrivateSubnet1RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPrivateSubnet1RouteTable
    subnet_id = NetworkPrivateSubnet1Subnet


class InstanceSecurityGroupIngress(ec2.SecurityGroup.Ingress):
    description = 'Allow HTTP from com.amazonaws.global.cloudfront.origin-facing'
    ip_protocol = 'tcp'
    from_port = 8080
    to_port = 8080
    source_prefix_list_id = FindInMap("Prefixes", AWS_REGION, 'PrefixList')


class InstanceSecurityGroupEgress(ec2.SecurityGroup.Egress):
    cidr_ip = '0.0.0.0/0'
    description = 'Allow all outbound traffic by default'
    ip_protocol = '-1'


class InstanceSecurityGroupAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-isg'


class InstanceSecurityGroup(ec2.SecurityGroup):
    resource: ec2.SecurityGroup
    group_description = 'vscode-server-isg'
    security_group_ingress = [InstanceSecurityGroupIngress]
    security_group_egress = [InstanceSecurityGroupEgress]
    tags = [InstanceSecurityGroupAssociationParameter]
    vpc_id = NetworkVPC


class NetworkPrivateSubnet1DefaultRoute(ec2.Route):
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NetworkPublicSubnet1NATGateway
    route_table_id = NetworkPrivateSubnet1RouteTable


class NetworkPrivateSubnet2SubnetAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-private-subnet-2'


class NetworkPrivateSubnet2Subnet(ec2.Subnet):
    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet2SubnetAssociationParameter]


class NetworkPrivateSubnet2RouteTableAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = 'vscode-server-private-subnet-2-rt'


class NetworkPrivateSubnet2RouteTable(ec2.RouteTable):
    resource: ec2.RouteTable
    vpc_id = NetworkVPC
    tags = [NetworkPrivateSubnet2RouteTableAssociationParameter]


class NetworkPrivateSubnet2DefaultRoute(ec2.Route):
    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = NetworkPublicSubnet2NATGateway
    route_table_id = NetworkPrivateSubnet2RouteTable


class NetworkPrivateSubnet2RouteTableAssociation(ec2.SubnetRouteTableAssociation):
    resource: ec2.SubnetRouteTableAssociation
    route_table_id = NetworkPrivateSubnet2RouteTable
    subnet_id = NetworkPrivateSubnet2Subnet


class CloudFrontCachePolicyCookiesConfig(cloudfront.CachePolicy.CookiesConfig):
    cookie_behavior = 'all'


class CloudFrontCachePolicyHeadersConfig(cloudfront.CachePolicy.HeadersConfig):
    header_behavior = 'whitelist'
    headers = ['Accept-Charset', 'Authorization', 'Origin', 'Accept', 'Referer', 'Host', 'Accept-Language', 'Accept-Encoding', 'Accept-Datetime']


class CloudFrontCachePolicyQueryStringsConfig(cloudfront.CachePolicy.QueryStringsConfig):
    query_string_behavior = 'all'


class CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin(cloudfront.CachePolicy.ParametersInCacheKeyAndForwardedToOrigin):
    cookies_config = CloudFrontCachePolicyCookiesConfig
    enable_accept_encoding_gzip = False
    headers_config = CloudFrontCachePolicyHeadersConfig
    query_strings_config = CloudFrontCachePolicyQueryStringsConfig


class CloudFrontCachePolicyCachePolicyConfig(cloudfront.CachePolicy.CachePolicyConfig):
    default_ttl = 86400
    max_ttl = 31536000
    min_ttl = 1
    name = 'vscode-server'
    parameters_in_cache_key_and_forwarded_to_origin = CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin


class CloudFrontCachePolicy(cloudfront.CachePolicy):
    resource: cloudfront.CachePolicy
    cache_policy_config = CloudFrontCachePolicyCachePolicyConfig
