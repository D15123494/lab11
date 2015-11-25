# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
from urllib2 import urlopen

res = urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key")
response = res.read().split(":");

# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = response[0]
secret_access_key = response[1]

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
if (len(sys.argv)==2):
	q = conn.get_queue(sys.argv[1])
	res = q.get_messages()
	print res[0].get_body()

