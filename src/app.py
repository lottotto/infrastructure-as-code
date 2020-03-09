#!/usr/bin/env python3

from aws_cdk import core

from src.src_stack import SrcStack


app = core.App()
SrcStack(app, "src")

app.synth()
