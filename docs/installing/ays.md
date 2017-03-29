# Installing G8OS on a Packet.net Server using AYS

The AYS templates for installing a G8OS are available at https://github.com/g8os/ays_template_g8os.

In what follows we discuss the steps to install G8OS using local AYS installation:

- [Install AYS 8.2](#install-ays)
- [Install the AYS templates](#install-templates)
- [Install the Python client for Packet.net](#packet-client)
- [Deploy the Packet.net server](#deploy-server)
- [Get the IP address of your Packet.net server](#get-ip)
- [Install the G8OS on your Packet.net server](#install-g8os)


<a id="install-ays"></a>
## Install the AYS templates

The AYS templates for installing a G8OS require AYS v8.2.

See the installation instructions here: [Installation of JumpScale](https://gig.gitbooks.io/jumpscale-core8/content/Installation/Installation.html)


<a id="install-templates"></a>
## Install the AYS templates

```
cd $TMPDIR
rm -f install.sh
curl -k https://raw.githubusercontent.com/g8os/ays_template_g8os/master/install.sh?$RANDOM > install.sh
bash install.sh
```

<a id="packet-client"></a>
## Install the Python client for Packet.net

The AYS templates will install a G8OS on a Packet.net server, and require the packet.net Python client for this.

In order to install it execute:

```
pip3 install git+https://github.com/gigforks/packet-python.git --upgrade
```

<a id="deploy-server"></a>
## Deploy the Packet.net server

First update the `server.yaml` blueprint with your Packet.net token, the SSH key to authorize on the server and the description of the server you want to deploy.

```
# execute the first blueprint
ays blueprint 1_server.yaml
# execute the run
ays run create --follow
```

<a id="get-ip"></a>
## Get the IP address of your Packet.net server

Once the run is done, your node is ready.

Inspect the node service to get the IP address of your server:

```
ays service show -r node -n main


---------------------------------------------------
Service: main - Role: node
state : ok
key : 759a3405085755fd3ca9a589cda15f99

Instance data:
- client : zaibon
- deviceId : 6e67c0d1-94f6-4342-9e47-330371879e90
- deviceName : main
- deviceOs : custom_ipxe
- ipPublic : 147.75.101.117
- ipxeScriptUrl : https://stor.jumpscale.org/public/ipxe/g8os-0.12.0-generic.efi
- location : amsterdam
- planType : Type 0
- ports : ['22:22']
- projectName : kdstest
- sshLogin : root
- sshkey : packetnet

Parent: None

Children: None

Producers:
sshkey!packetnet
packetnet_client!zaibon

Consumers: None

Recurring actions: None

Event filters: None
```


<a id="install-g8os"></a>
## Install the G8OS on your Packet.net server

First update the `2_g8os.yaml` blueprint with the IP address of the server you got from the previous step:

```
g8os_client__main:
  redisAddr: 'PUT THE IP HERE'
```

Then execute the blueprint and create a run:

```
# execute the first blueprint
ays blueprint 2_g8os.yaml
# execute the run
ays run create --follow
```

Your container should now be running.

You can inspect it to see its ZeroTier IP:

```
ays service show -r container

Service: ubuntu2 - Role: container
state : ok
key : 64cc03d7bbe7317e1a5fc88a231bcd01

Instance data:
- hostname : ubuntu2
- id : 1
- node : ubuntu
- zerotierID : e5cd7a9e1c0270be
- zerotierIP : 192.168.193.120

Parent:
node!ubuntu

Children: None

Producers:
node!ubuntu

Consumers: None

Recurring actions:
monitor: period:1.0 minutes last run:2017/03/18 12:03:51

Event filters: None
```
