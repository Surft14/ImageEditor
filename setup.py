# setup.py
from setuptools import setup, find_packages

setup(
    name="image-editor",            # pip install image-editor
    version="0.1.0",
    description="Modular image editor based on Pillow",
    author="Surft14",
    url="https://github.com/Surft14/ImageEditor",
    packages=find_packages(exclude=["tests*",]),
    install_requires=[
        "Pillow>=8.0.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)