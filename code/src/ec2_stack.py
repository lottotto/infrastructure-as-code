# from aws_cdk import core
# from aws_cdk import aws_ec2 as ec2

from aws_cdk import (
    core,
    aws_ec2 as ec2
)

class EC2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cidr = '10.0.0.0/16'
        vpc = ec2.Vpc(
            self,
            id = 'cdk-test-vpc',
            cidr=cidr,
            max_azs=1)
    
        security_group = ec2.SecurityGroup(
            self,
            id='cdk-sg',
            vpc=vpc,
            security_group_name='cdk-sg',
        )
        # what is peer
        security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4(cidr),
            connection=ec2.Port.tcp(22),
        )
        security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/0'),
            connection=ec2.Port.tcp(80),
        )

        image_id = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2).get_image(self).image_id

        ec2.CfnInstance(
            self,
            id = 'cdk-instancd',
            availability_zone="ap-northeast-1a",
            image_id=image_id,
            instance_type="t2.micro",
            security_group_ids=[security_group.security_group_id],
            subnet_id=vpc.private_subnets[0].subnet_id,
            tags=[{
                "key":"Name",
                "value":"cdk-instance"
            }]
        )



