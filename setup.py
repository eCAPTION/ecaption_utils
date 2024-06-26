from setuptools import setup

setup(
    name="ecaption_utils",
    version="0.0.15",
    description="Package containing common utility functions for the eCAPTION application",
    url="https://github.com/eCAPTION/ecaption_utils.git",
    author="Chow En Rong",
    author_email="chowenrong@u.nus.edu",
    license="unlicensed",
    packages=["ecaption_utils/kafka", "ecaption_utils/kafka/events"],
    install_requires=["faust"],
    zip_safe=False,
)
