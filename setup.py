from setuptools import setup, find_packages


setup (
    name             = "pkktranslator",
    version          = "0.1",
    description      = "Proxy for pkk5 map services",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)     