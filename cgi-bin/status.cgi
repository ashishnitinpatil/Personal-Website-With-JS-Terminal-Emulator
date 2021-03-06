#!/bin/bash

echo "Content-type:\ttext"
echo

up=0
down=-1
#Alright. I know you're probably like "What the fuck? Why is that being instantiated as -1? Well, the truth is. I HAVE NO IDEA. For some reason /dev/tcp ALWAYS sets $down to 1 after it has been ran. Even if it's alive and it sets $up to 1 as well. So.. well this is my fix. Not sure if the same bug applies to $up or not... but my tests are showing the proper amount of servers are being returned with it being instatiated at 0. So ima leave it. whatever.

timeout .1 bash -c "</dev/tcp/io.sol.milkyway/53" && printf "AD DNS:\t\tUp\n" || printf "AD DNS:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/io.sol.milkyway/53" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/io.sol.milkyway/389" && printf "AD LDAP:\t\tUp\n" || printf "AD LDAP:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/io.sol.milkyway/389" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/io.sol.milkyway/88" && printf "AD Kerberos:\t\tUp\n" || printf "AD Kerberos:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/io.sol.milkyway/88" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/2000" && printf "Apache:\t\tUp\n" || printf "Apache:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/2000" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/5050" && printf "CouchPotato:\t\tUp\n" || printf "CouchPotato:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/5050" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/jupiter.sol.milkyway/631" && printf "CUPS:\t\tUp\n" || printf "CUPS:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/jupiter.sol.milkyway/631" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/8112" && printf "Deluge:\t\tUp\n" || printf "Deluge:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/8112" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/7852" && printf "Deluge Traffic:\t\tUp\n" || printf "Deluge Traffic:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/7852" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/saturn.sol.milkyway/443" && printf "ESXi:\t\tUp\n" || printf "ESXi:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/saturn.sol.milkyway/443 " && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/8442" && printf "LibreNMS:\t\tUp\n" || printf "LibreNMS:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/8442" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/rp.tjzimmerman.com/443" && printf "Netdata RP:\t\tUp\n" || printf "Netdata RP:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/rp.tjzimmerman.com/443 " && let up++ || let down++

timeout .1 bash -c "</dev/tcp/tjzimmerman.com/443" && printf "NGINX:\t\tUp\n" || printf "NGINX:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/tjzimmerman.com/443" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/943" && printf "OpenVPN:\t\tUp\n" || printf "OpenVPN:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/943" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/8050" && printf "OpenVPN - TCP:\t\tUp\n" || printf "OpenVPN - TCP:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/8050" && let up++ || let down++

timeout .1 bash -c "</dev/udp/24.17.195.62/8051" && printf "OpenVPN - UDP:\t\tUp\n" || printf "OpenVPN - UDP:\t\tDown\n"
timeout .1 bash -c "</dev/udp/24.17.195.62/8051" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/sol.sol.milkyway/80" && printf "OpenWRT:\t\tUp\n" || printf "OpenWRT:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/sol.sol.milkyway/80" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/luna.sol.milkyway/80" && printf "Pi-Hole:\t\tUp\n" || printf "Pi-Hole:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/luna.sol.milkyway/80" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/luna.sol.milkyway/53" && printf "Pi-Hole DNS:\t\tUp\n" || printf "Pi-Hole DNS:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/luna.sol.milkyway/53" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/32400" && printf "Plex:\t\tUp\n" || printf "Plex:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/32400" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/janus.sol.milkyway/8181" && printf "PlexPy:\t\tUp\n" || printf "PlexPy:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/janus.sol.milkyway/8181" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/24.17.195.62/8989" && printf "Sonarr:\t\tUp\n" || printf "Sonarr:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/24.17.195.62/8989" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/jupiter.sol.milkyway/9510" && printf "Unified Remote:\t\tUp\n" || printf "Unified Remote:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/jupiter.sol.milkyway/9510" && let up++ || let down++

timeout .1 bash -c "</dev/tcp/pluto.sol.milkyway/443" && printf "VMware VCSA:\t\tUp\n" || printf "VMware VCSA:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/pluto.sol.milkyway/443" && let up++ || let down++ 

timeout .1 bash -c "</dev/tcp/pluto.sol.milkyway/443" && printf "VMware vROps:\t\tUp\n" || printf "VMware vROps:\t\tDown\n"
timeout .1 bash -c "</dev/tcp/pluto.sol.milkyway/443" && let up++ || let down++ 

echo
echo "----------------"
echo "Servers Up:   "$up
echo "Servers Down: "$down
