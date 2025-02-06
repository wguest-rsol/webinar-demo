# Start with an official Ubuntu base image
FROM ubuntu:24.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y hashcat john curl iproute2 openssh-server gzip vim sudo
    # Create a user named "attacker" and set the password "HelloWorld!"


RUN useradd -m -s /bin/bash attacker && \
echo "attacker:HelloWorld!" | chpasswd && \
usermod -aG sudo attacker

WORKDIR /home/attacker
COPY ./rockyou.txt.tar.gz ./rockyou.txt.tar.gz

RUN tar xzf rockyou.txt.tar.gz && rm rockyou.txt.tar.gz 

COPY ./hashes.txt ./hashes.txt

# Configure SSH to allow password authentication
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config

# Expose port 22 for SSH connections
EXPOSE 22

# Start SSH service and allow SSH connections
CMD ["/usr/sbin/sshd", "-D"]
