# Mini Project
## _NETWORK TRAFFIC ANALYZER_
A python based packet sniffer and traffic visualiser .

## Features

- Dynamic traffic analysing 
- Packet count customisation
- Easy to use and set up 
- Data visualisation

## Setup and Execution

Built for ubuntu and debian based systems

Start by running the setup script.

```sh
$ cd Network_Traffic_Analyzer
$ sudo ./setup.sh
```

Completed setups will provide the following output

```sh
 Setup Complete 
============================================================================================
```
The setup need only be run once and can skipped for future uses.

To run the analyzer : 

```sh
$ sudo ./run.sh
```
The script makes it easier to find the wireless interface to listen to and to find the ip adress of the user.

The Programme requires three variables The wireless interface to use, The number of packets and The ip address of the user . For the sake of customisability The variables can be modified by the user at the begining of the programme .
The programme outputs an analysis of the traffic and plots a matplot interface to visualise the same .
The data can be saved according to the wish of the user

## Plugins

Instructions to download the prerequisites are linked below.

| Requirements | Sorce address |
| ------ | ------ |
| Python3 | https://docs.python-guide.org/starting/install3/linux/ |
| Pip | https://pypi.org/project/pip/ |
| Pyshark | https://pypi.org/project/pyshark/ |
| Matplotlib | https://pypi.org/project/matplotlib/ |