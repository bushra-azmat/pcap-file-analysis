from scapy.all import rdpcap, wrpcap
from scapy.layers.inet import IP

# Path to the input pcap file
input_file = 'sip-captured.pcap'

# Path to the output pcap file
output_file = 'modified_packets.pcap'

# Read packets from the input pcap file
packets = rdpcap(input_file)

for packet in packets:
    if IP in packet:
        ip_layer = packet[IP]

        # Check if the packet has SIP layer
        if 'SIP' in ip_layer.payload:
            sip_layer = ip_layer.payload['SIP']

            # Extract desired fields (To, From, Call-ID)
            to_field = sip_layer.get_field('To')
            from_field = sip_layer.get_field('From')
            call_id_field = sip_layer.get_field('Call-ID')

            # Get the current value of the From field
            from_value = from_field.show

            # Modify the From field to include name as a prefix
            modified_from_value = 'Bushra' + from_value

            # Set the modified From field value
            from_field.show = modified_from_value

    # Write the modified packet to the output pcap file
    wrpcap(output_file, packet, append=True)

print("Packets written to", output_file)

