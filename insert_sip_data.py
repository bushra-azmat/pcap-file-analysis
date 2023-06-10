import pyshark
import sqlite3

# Path to the input pcap file
input_file = 'sip-captured.pcap'

# Connect to the SQLite database
conn = sqlite3.connect('sip_data.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Read packets from the input pcap file
capture = pyshark.FileCapture(input_file)

for packet in capture:
    try:
        # Extract SIP portion of the packet
        sip_layer = packet.sip

        # Extract the desired fields
        to_field = sip_layer.get_field('To').show
        from_field = sip_layer.get_field('From').show
        call_id_field = sip_layer.get_field('Call-ID').show

        # Insert the extracted data into the database
        cursor.execute('''
            INSERT INTO sip_packets (source, destination, call_id)
            VALUES (?, ?, ?)
        ''', (to_field, from_field, call_id_field))

    except AttributeError:
        # Skip packets that don't have a SIP layer
        pass

# Commit the changes and close the connection
conn.commit()
conn.close()

