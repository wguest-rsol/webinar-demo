# Start with an official Ubuntu base image
FROM ubuntu:24.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install required dependencies
RUN apt-get update && \
    apt-get install -y \
    openssh-server \
    python3 \
    python3-pip \
    python3-netifaces \
    sudo \
    iproute2 \
    git \
    dnsutils \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Create a user named "attacker" and set the password "HelloWorld!"
RUN useradd -m -s /bin/bash attacker && \
    echo "attacker:HelloWorld!" | chpasswd && \
    usermod -aG sudo attacker

RUN mkdir /home/attacker/.ssh
COPY id_rsa.pub  /home/attacker/.ssh/authorized_keys

RUN cd /home/attacker/ && git clone https://github.com/lgandx/Responder.git && chown -R attacker:attacker /home/attacker/Responder
    

# Configure SSH to allow password authentication
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config

# permissions for ssh
RUN chmod 700 /home/attacker/.ssh && chmod 600 /home/attacker/.ssh/authorized_keys && chown -R attacker:attacker /home/attacker/.ssh

# proxychains using 3434
COPY proxychains4.conf /etc/proxychains4.conf

# Expose port 22 for SSH connections
EXPOSE 22

# Start SSH service and allow SSH connections
CMD ["/usr/sbin/sshd", "-D"]
