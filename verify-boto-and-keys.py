from boto import *
from urllib2 import urlopen

res = urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key")
response = res.read().split(":");

print (response[0]+"\n"+response[1]+"\n"+boto.__version__)
