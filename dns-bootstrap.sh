#!/bin/bash

# Set up resolver
echo "Configuring DNS Resolution on the host..."
sudo mkdir /etc/resolver
echo 'nameserver 127.0.0.1' | sudo tee /etc/resolver/dev
echo 'port 53535' | sudo tee -a /etc/resolver/dev
echo ''

# Set up dnsmasq container
echo 'Setting up dnsmasq container...'
docker run -d --name dnsmasq --restart always -p 53535:53/tcp -p 53535:53/udp --cap-add NET_ADMIN andyshinn/dnsmasq --address=/dev/127.0.0.1
