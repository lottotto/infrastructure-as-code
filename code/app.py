#!/usr/bin/env python3

from aws_cdk import core

from src.s3_stack import S3Stack
from src.ec2_stack import EC2Stack



app = core.App()
# S3Stack(app, "src")
EC2Stack(app, "cdk-ec2")

app.synth()
