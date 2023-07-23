from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='hci',
    version='1.0.0',
    description='Library for creating and parsing HCI packets.',
    long_description='This library is start with Arthur Crippa Búrigo & Pedro Gyrão,'
                     'I am continuing their work to accommodate the constantly updated bluetooth spec'
                     'I hope these jobs can help bluetooth engineers.'
                     'If you have any request or bugs, please email me.',
    url='https://github.com/cc4728/python-hci',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.11',
    ],
    keywords=['HCI', 'protocol','mtk','mediatek','encode', 'decode',
              'ble', 'bluetooth low energy'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    author='Jing Cai',
    author_email='jcmtk16230@gmail.com',
)
