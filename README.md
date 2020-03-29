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


## update aws iot sdk 

Get latest AWSIoTPythonSDK, replace the version under <gitroot>/AWSIoTPyThonSDK

https://pypi.org/project/AWSIoTPythonSDK/1.0.0/#installation

```shell
sudo python setup.py install
sudo apt update
sudo apt install python-pip
pip install awsiotsdk
ls /usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK
cp /usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK ~/github/vscode-hello-python/
```


# Issues

> https://github.com/ev3dev/ev3dev/issues/1220

# Open issues

>
https://github.com/ev3dev/ev3dev/issues/1294



