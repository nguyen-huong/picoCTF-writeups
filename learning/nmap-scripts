# NMap NSE scripts: Get CVEs faster in NMap

## Notes of Tutorial:

## What's NSE?
Lua script that "allows users to write (and share) simple scripts to automate a wide variety of networking tasks. Those scripts are then executed in parallel with the speed and efficiency you expect from Nmap."

## Tools
https://github.com/vulnersCom/nmap-vulners
https://github.com/scipag/vulscan

## Goal
Take NMap's identified scanning info and print out CVEs with detailed info about vulnerabilities for epxloitations

## Solution
Go to NMap scripts
``` terminal
cd /usr/share/nmap/scripts/

```
Clone the scripts
```
sudo git clone https://github.com/vulnersCom/nmap-vulners.git
sudo git clone https://github.com/scipag/vulscan.git

```
Make sure vulnerabilities databases are up to date
```
cd vulscan/utilities/updater/
sudo chmod +x updateFiles.sh
./updateFiles.sh

```
Scan w/ Vulners
```
sudo nmap --script vulscan/ -sV -p# ###.###.###.###

```
Scan w/ Vulscan
```
sudo nmap --script vulscan/ -sV -p# ###.###.###.###

```
