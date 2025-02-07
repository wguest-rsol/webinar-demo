# Start with an official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y proxychains4 nmap curl iproute2 openssh-server vim sudo ssh dnsutils
    # Create a user named "attacker" and set the password "HelloWorld!"


RUN useradd -m -s /bin/bash attacker && \
echo "attacker:HelloWorld!" | chpasswd && \
usermod -aG sudo attacker

WORKDIR /home/attacker

# Configure SSH to allow password authentication
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
COPY id_rsa /home/attacker/id_rsa
RUN chown attacker:attacker /home/attacker/id_rsa && chmod 600 /home/attacker/id_rsa

# Expose port 22 for SSH connections
EXPOSE 22

# Start SSH service and allow SSH connections
CMD ["/usr/sbin/sshd", "-D"]
