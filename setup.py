from setuptools import (
    config,
    find_packages,
    setup,
)

import x_net_django_email_template


conf = config.read_configuration("setup.cfg")
metadata = conf.get("metadata")

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    version=x_net_django_email_template.__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
    ],
    **metadata
)
