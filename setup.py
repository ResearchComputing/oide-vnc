# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='oide-vnc',
    version='0.0.dev1',
    author=u'Zebula Sampedro',
    author_email='sampedro@colorado.edu',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ResearchComputing/oide-vnc',
    license='AGPLv3, see LICENSE',
    description="Online Integrated Development Environment (OIDE) - VNC App",
    long_description=open('README.md').read(),
    zip_safe=False,
    install_requires=[
        'oide',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Text Editors :: Integrated Development Environments (IDE)',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
    ],
)
