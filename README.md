# Flash the card guide

https://sites.google.com/site/ev3devpython/setting-up-vs-code


## SD flash card image

https://www.ev3dev.org/docs/getting-started/
Python 2.7.13



### Offical Version

https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Not recommended, it's using brickrun and micropython



## download aws iot sdk and manuall install

https://pypi.org/project/AWSIoTPythonSDK/1.0.0/#installation

```shell
sudo python setup.py install
sudo apt update
sudo apt install python-pip
pip install awsiotsdk
```

### Default installation location:
/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK
cp /usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK <coderoot>/


# Setup VS Code

```cmd
py -3 -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install python-ev3dev2
```

See below

> https://github.com/ev3dev/ev3dev/issues/1220

# Open issues

>
https://github.com/ev3dev/ev3dev/issues/1294



