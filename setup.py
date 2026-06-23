#!/usr/bin/env python
# Copyright (c) Megvii, Inc. and its affiliates. All Rights Reserved

import re
import setuptools
import glob
from os import path
import torch
from torch.utils.cpp_extension import CppExtension

os.system("pip install -r requirements.txt")
torch_ver = [int(x) for x in torch.__version__.split(".")[:2]]
assert torch_ver >= [1, 3], "Requires PyTorch >= 1.3"


with open("README.md", "r") as f:
    long_description = f.read()

def get_package_dir():
    pkg_dir = {
        "tracker": "tracker",
    }
    return pkg_dir


setuptools.setup(
    name="botsort",
    version="0.1.0",
    author="basedet team",
    url="https://github.com/360iQ/BoT-SORT.git",
    python_requires=">=3.6",
    install_requires=get_install_requirements(),
    setup_requires=["wheel", "torch"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Independent"],
    cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
    packages=list(get_package_dir().keys()),
)
