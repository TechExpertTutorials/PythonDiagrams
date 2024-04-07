from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import VPC, ELB, PrivateSubnet, PublicSubnet, RouteTable
from diagrams.aws.compute import EKS, EC2, Lambda, EC2Instance, LambdaFunction
from diagrams.aws.mobile import APIGateway
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.general import InternetGateway

with Diagram("My Diagram", show=False):
    igw = InternetGateway("Internet Gateway")
    with Cluster("Network"):
        vpc = VPC("VPC")
        rt = RouteTable("Route Table")

        with Cluster("Public"):
            with Cluster("Subnet 1"):
                ec2 = EC2("EC2")
        with Cluster("Private Subnet Group"):
            with Cluster("Subnet 3"):
                rds1 = RDS("PostgreSQL Primary")
            with Cluster("Subnet 2"):
                rds2 = RDS("PostgreSQL Secondary")
        
    igw >> rt >> ec2 >> rds1
    ec2 >> rds2