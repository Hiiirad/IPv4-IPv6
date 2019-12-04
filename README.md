# IP Repository!
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE)
![PyPI - Status](https://img.shields.io/pypi/status/Django.svg)

Hi everybody :)

This is my first repository and love to share my programs with everybody as I consider myself an Open-Source advocate.

## Getting Started

These programs will only works on **Linux** systems and I believe they would be work perfectly on Macbooks. My OS is Ubuntu 18.04 and I design these programs to run on all debian-based linux systems. The installation process will be different if you use other linux distributions.

There are 6 programs in this repository which each of has its own feature to play with IPs.

### Features

1. **IP Detection**: This program detects IP with regex (Regular Expression) and recognize these:
    * IPv4 or IPv6
    * IP ranges
    * Valid or Invalid IP
2. **Decimal to IPv4**: This program convert decimal format to IP address from dotted-decimal address.
3. **IPv4 to Decimal**: This program translate IP address from dotted-decimal address to decimal format.
4. **Generate IPv4**: Give this program a first of a range and an end IP of that range and you get all IPs between them.
5. **Subnet IPv4**: This program gets an IP and gives you netmask of it.
6. **Hosts of Network**: This program get you number of hosts based on any form of netmask.

### Prerequisites
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install git
```

### Installing
I prefer using [Anaconda](https://www.anaconda.com/) instead of using [Pip or PyPI](https://pypi.org/), but you decide which is good for you.
 - Using Pip:
    - ```sudo apt install python3-pip```
    - ```pip install pip```
    - ```pip install -r requirements.txt```
 - Using Anaconda: Installation process is completely documented [here](https://docs.anaconda.com/anaconda/install/linux/).

### Upgrading
* Pip:
    ```
    pip install -U pip
    ```
* Anaconda:
    ```
    conda update --all
    ```

### Version check to verify installation
* Pip:
    ```
    pip --version
    ```
* Anaconda:
    ```
    conda --version
    ```

## Usage
```
git clone https://github.com/Hiiirad/IPv4-IPv6.git
```
```
cd IPv4-IPv6/
```
```
python name-of-program.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
