# NMap NSE scripts: Get Network CVEs faster in NMap

## Notes of Tutorial:
https://www.youtube.com/watch?v=3U1pJ-eJrAU

## What's NSE?
Lua script that "allows users to write (and share) simple scripts to automate a wide variety of networking tasks. Those scripts are then executed in parallel with the speed and efficiency you expect from Nmap."

## Tools
- https://github.com/vulnersCom/nmap-vulners
- https://github.com/scipag/vulscan

## Goal
Take NMap's identified scanning info and print out CVEs with detailed info about vulnerabilities for epxloitations

## Solution
Go to NMap scripts
``` python
cd /usr/share/nmap/scripts/
```
Clone the scripts
``` python
sudo git clone https://github.com/vulnersCom/nmap-vulners.git
sudo git clone https://github.com/scipag/vulscan.git
```
Make sure vulnerabilities databases are up to date
``` python
cd vulscan/utilities/updater/

sudo chmod +x updateFiles.sh

./updateFiles.sh
```
Scan w/ Vulners

Output: Open ports, CVE scores & links
``` python
sudo nmap --script vulscan/ -sV -p# ###.###.###.###
```
Scan w/ Vulscan

Output: Open ports, CVEs with descriptions from databases
``` python
sudo nmap --script vulscan/ -sV -p# ###.###.###.###

#specify database
sudo nmap --script vulscan/ --script-args vulscandb=exploitdb.csv -sV -p# ###.###.###.###
```
