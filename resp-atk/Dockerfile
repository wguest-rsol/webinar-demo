# Start with an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install required dependencies
RUN apt-get update && \
    apt-get install -y \
    openssh-server \
    python3 \
    python3-pip \
    sudo \
    iproute2 \
    git \
    dnsutils \
    bash \
    ufw \
    && rm -rf /var/lib/apt/lists/*

# Create a user named "attacker" and set the password "HelloWorld!"
RUN useradd -m -s /bin/bash attacker && \
    echo "attacker:HelloWorld!" | chpasswd && \
    usermod -aG sudo attacker

RUN pip3 install impacket
RUN pip3 install netifaces
RUN cd /opt/ && git clone https://github.com/lgandx/Responder.git && chown -R attacker:attacker /opt/Responder
    

# Configure SSH to allow password authentication
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config

# Expose port 22 for SSH connections
EXPOSE 22

# Start SSH service and allow SSH connections
CMD ["/usr/sbin/sshd", "-D"]
