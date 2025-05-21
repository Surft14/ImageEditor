from setuptools import setup, find_packages

setup(
    name="image-editor",
    version="1.0.0",
    description="Modular image editor based on Pillow",
    author="Surft14",
    packages=find_packages(),
    install_requires=[
        "Pillow>=8.0.0"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "imgedit=image_editor.main:main",
        ],
    },
)