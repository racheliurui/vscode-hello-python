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

sudo python setup.py install

sudo apt update
sudo apt install python-pip
pip install awsiotsdk


### Default installation location:
/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK

### Default python Path on EV3
```shell
robot@ev3dev:~/vscode-hello-python/downloads/awsiot$ python -c "import sys; print sys.path"
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-arm-linux-gnueabi', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gtk-2.0']
```
/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK

 python -c "import sys; sys.path.append('/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK');import AWSIoTPythonSDK; print sys.modules['AWSIoTPythonSDK']"


 python -c "import sys; import AWSIoTPythonSDK; print sys.modules['AWSIoTPythonSDK']"


export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK

PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK
 python <your-program>

sdk/test/Python


# Open issues

>
https://github.com/ev3dev/ev3dev/issues/1294
