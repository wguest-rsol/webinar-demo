# Start with an official Ubuntu base image
FROM ubuntu:24.04

# Set environment variables to prevent interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install required dependencies
RUN apt-get update && \
    apt-get install -y \
    openssh-server \
    sudo \
    iproute2 \
    bash \
    git \
    curl \
    wget \
    make \
    g++ \
    automake \
    python3 \
    python3-build \
    python3-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create a user named "attacker" and set the password "HelloWorld!"
RUN useradd -m -s /bin/bash user && \
    echo "user:HelloWorld!" | chpasswd && \
    usermod -aG sudo user

RUN mkdir /home/user/.ssh
COPY id_rsa.pub  /home/user/.ssh/authorized_keys

# Configure SSH to allow password authentication
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config

# permissions for ssh
RUN chmod 700 /home/user/.ssh && chmod 600 /home/user/.ssh/authorized_keys && chown -R user:user /home/user/.ssh

# Expose port 22 for SSH connections
EXPOSE 22

# Start SSH service and allow SSH connections
CMD ["/usr/sbin/sshd", "-D"]
