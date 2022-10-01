"""
Setup.py
"""
import linecache

import setuptools

setuptools.setup(
    # Includes all other files that are within your project folder
    include_package_data=True,

    # Name of your Package
    name='vlc_streamer',

    # Project Version
    version='1.0',

    # Description of your Package
    description='A vlc based music engine',

    # Website for your Project or GitHub repo
    url="https://github.com/KreativeThinker/vlc-streamer",

    # Name of the Creator
    author='KreativeThinker',

    # Creator's mail address
    author_email='',

    # Projects you want to include in your Package
    packages=setuptools.find_packages(),

    # Dependencies/Other modules required for your package to work
    install_requires=linecache.getlines('requirements.txt'),

    # Detailed description of your package
    long_description='View github repp',

    # Format of your Detailed Description
    long_description_content_type="text/markdown",

    # Classifiers allow your Package to be categorized based on functionality
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
