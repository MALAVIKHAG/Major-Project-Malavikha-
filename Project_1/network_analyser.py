import pyshark
import matplotlib.pyplot as plt
from collections import Counter

# Capture 1000 packets from a network interface (e.g., eth0)
x1=input("Enter the wireless interface : ")
y1=int(input("Enter number of packets : "))
ip1=input("Enter your IP adress : ")
capture = pyshark.LiveCapture(interface=x1)
packet_count = y1

# Initialize data holders
ip_src_list = []
ip_dst_list = []
protocol_list = []
data_sent = 0
data_received = 0

# Counter to track number of packets processed
packets_processed = 0

# Analyze packets
for packet in capture.sniff_continuously(packet_count=packet_count):
    packets_processed += 1
 
    # Print the number of packets received so far
    print(f"Packets received: {packets_processed}/{packet_count}")

    # IP Layer analysis
    if 'IP' in packet:
        ip_src_list.append(packet.ip.src)
        ip_dst_list.append(packet.ip.dst)

    # Protocol analysis
    if hasattr(packet, 'highest_layer'):
        protocol_list.append(packet.highest_layer)

    # Data sent and received
    if hasattr(packet, 'length'):
        packet_length = int(packet.length)
        if 'IP' in packet:
            # Assume traffic leaving the interface as sent, incoming as received
            if packet.ip.src == ip1:  # Replace with your local IP
                data_sent += packet_length
            else:
                data_received += packet_length

# Count occurrences
ip_src_count = Counter(ip_src_list)
ip_dst_count = Counter(ip_dst_list)
protocol_count = Counter(protocol_list)

# Convert data to lists for plotting
ip_src_labels, ip_src_values = zip(*ip_src_count.most_common(10))  # Top 10 IP sources
ip_dst_labels, ip_dst_values = zip(*ip_dst_count.most_common(10))  # Top 10 IP destinations
protocol_labels, protocol_values = zip(*protocol_count.most_common())

# Plotting
plt.figure(figsize=(14, 10))

# IP Source Distribution
plt.subplot(2, 2, 1)
plt.barh(ip_src_labels, ip_src_values, color='skyblue')
plt.title("Top 10 Source IP Addresses")
plt.xlabel("Packet Count")

# IP Destination Distribution
plt.subplot(2, 2, 2)
plt.barh(ip_dst_labels, ip_dst_values, color='salmon')
plt.title("Top 10 Destination IP Addresses")
plt.xlabel("Packet Count")

# Protocol Distribution
plt.subplot(2, 2, 3)
plt.pie(protocol_values, labels=protocol_labels, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title("Protocol Distribution")

# Data Sent vs Received
plt.subplot(2, 2, 4)
plt.bar(['Data Sent', 'Data Received'], [data_sent, data_received], color=['green', 'red'])
plt.title("Data Sent vs Data Received")
plt.ylabel("Bytes")

# Show all plots
plt.tight_layout()
plt.show()
