# Use Ubuntu base image
FROM ubuntu:20.04

# Set non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install impacket (needed for SMB authentication)
RUN pip3 install impacket
RUN pip3 install scapy

# Create a working directory for the script
WORKDIR /root

# Copy the LLMNR/SMB authentication script into the container
COPY llmnr.py ./llmnr.py

# Set execute permissions for the script
RUN chmod +x ./llmnr.py

# Define the default command to run the script
CMD ["python3", "/root/llmnr.py"]
