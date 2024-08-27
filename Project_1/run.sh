#!/bin/bash
echo "=========================================================="
echo -e "\e[1;4m Available nterfaces and their ip addresses \e[0m"
ip -o -4 addr list | while read -r line; do
    # Extract interface name and IP address
    iface=$(echo "$line" | awk '{print $2}')
    ip=$(echo "$line" | awk '{split($4, a, "/"); print a[1]}')
    
    # Print with formatting
    printf "\e[1m%s\e[0m : %s\n" "$iface" "$ip"
done
echo "=========================================================="
python3 network_analyser.py 
