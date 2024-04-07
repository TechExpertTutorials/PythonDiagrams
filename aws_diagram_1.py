from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import VPC, ELB
from diagrams.aws.compute import EKS, EC2, Lambda, EC2Instance, LambdaFunction
from diagrams.aws.mobile import APIGateway
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.general import InternetGateway

with Diagram("My App", show=False):
    lb = ELB("Elastic Load Balancer")
    # Kubernetes
    k8s = EKS("EKS Cluster")
    igw = APIGateway("API Gateway")

    with Cluster("Lambda Functions"):
        lambda_group = [Lambda("fnc1"),
                     Lambda("fnc2"),
                     Lambda("fnc3")]
    
    rds = RDS("Postgres RDS")
    lb >> k8s >> igw >> lambda_group >> rds