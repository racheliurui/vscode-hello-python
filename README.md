# Set up


## mirco SD Card

https://www.ev3dev.org/docs/getting-started/
Python 2.7.13

### Image version
>
https://github.com/ev3dev/ev3dev/releases/download/ev3dev-stretch-2019-10-23/ev3dev-stretch-ev3-generic-2019-10-23.zip

* __The official version not working well in lab, so avoid education.lego.com__

https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
Not sure if because it's using brickrun and micropython

### Setup Code environment 

```cmd
py -3 -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install python-ev3dev2
```

command for mac book

```mac 
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install python-ev3dev2

```

### Download Code  

```shell
#download code
cd 3 
curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt 

``` 


### Set up wifi dongle

* Connect to Wifi ; check the ip address
 
* Check traceroute to ip works; check port is opened

* Check the device name 
https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/

robot 
maker

```
uname -a
Linux ev3dev 4.14.117-ev3dev-2.3.4-ev3 #1 PREEMPT Thu May 9 15:13:01 CDT 2019 armv5tejl GNU/Linux
```


## update aws iot sdk 

Provision a thing, get the Python Starter Package.

https://pypi.org/project/AWSIoTPythonSDK/1.0.0/#installation

```shell

sudo python setup.py install
sudo apt update
sudo apt install python-pip
pip install awsiotsdk
ls /usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK
cp /usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK ~/github/vscode-hello-python/
```

## Check Policy

* Check Thing Policy has access to connect and publish 
* Check IoT rule has access to route message to target (SNS in this case)
* Enable IoT Rule Error log , so that if Rule has falure, you can capture it from cloudwatch
* Use Raw format from IoT Rule output when pumping data to SNS (to avoid format rule)


## Setup Robot Maker

```
robot@ev3dev:~$ curl https://d1onfpft10uf5o.cloudfront.net/greengrass-device-setup/downloads/gg-device-setup-latest.sh > gg-device-setup-latest.sh && chmod +x ./gg-device-setup-latest.sh && sudo -E ./gg-device-setup-latest.sh bootstrap-greengrass --region $AWS_REGION --group-name $GG_GROUP_NAME
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  115k  100  115k    0     0  27566      0  0:00:04  0:00:04 --:--:-- 27600
############### Greengrass Device Setup v1.0.0 ###############
[GreengrassDeviceSetup] The Greengrass Device Setup bootstrap log is available at: /tmp/greengrass-device-setup-bootstrap-1585537732.log
[GreengrassDeviceSetup] Using package management tool: apt-get...
[GreengrassDeviceSetup] Python (python3.7) not found. Attempting to install it...
[GreengrassDeviceSetup] Not able to install Python (python3.7).
[GreengrassDeviceSetup] Using runtime: python3.5...
[GreengrassDeviceSetup] Installing a dedicated pip for Greengrass Device Setup...
[GreengrassDeviceSetup] Validating and installing required dependencies...
[GreengrassDeviceSetup] The Greengrass Device Setup configuration is complete. Starting the Greengrass environment setup...
[GreengrassDeviceSetup] Forwarding command-line parameters: bootstrap-greengrass --region us-east-1 --group-name EV3Robot-group

[GreengrassDeviceSetup] Validating the device environment...
[GreengrassDeviceSetup] Platform Linux-4.14.117-ev3dev-2.3.4-ev3-armv5tejl-with-debian-9.10 not supported
Code 1, Message: Platform Linux-4.14.117-ev3dev-2.3.4-ev3-armv5tejl-with-debian-9.10 not supported

```

# Issues

> https://github.com/ev3dev/ev3dev/issues/1220

# Open issues

>
https://github.com/ev3dev/ev3dev/issues/1294



