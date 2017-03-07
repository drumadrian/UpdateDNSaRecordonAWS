
##################################################################################################
# Purpose:      This function will be triggered when an EC2 instance
#               is started that needs to have an A-Record updated with
#               the newly assigned Public AWS Elastic IP address.
#
# Author:       Adrian Drummond
#
# Date:         March 1, 2017  (initial creation)
#               ?              (updated)
#
# Triggered by: The AWS EC2 instance should trigger an AWS CloudWatch event
#
# Summary: 		The triggered CloudWatch event should post to an AWS SNS topic
#               The SNS topic should alert the admin that the Instance has been started
#        		and the Lambda function is being triggered with the CloudWatch information
#        		The Lambda function should find the AWS EC2 instance using the instanceID
#        		and get the Public IP address.  The EC2 Instance should also be tagged
#        		with the desired public DNS Name.  Ex: securefiles.diegotax.com
#        		The function should updated the A Record in AWS Route53 to have the new AWS
#        		assigned Public IP address.
##################################################################################################


##import boto3








#Find the instance
def get_instance(event):
    IDofInstance = event['instanceID']
    print 'IDofInstance = {}'.format(IDofInstance)
    return IDofInstance


#Get the Public IP
def get_public_IP(targetInstance_ID):
    ##boto3 = boto3.client('EC2')
    #publicIP = boto3.get_public_IP(targetInstance_ID)
    
    publicIP = '123.235.122.112'
    print 'publicIP = {}'.format(publicIP)
    return publicIP



#Get the DNS/hostname to be updated
def get_instance_hostname():
    ##boto3 = boto3.client('EC2')
    #publicIP = boto3.get_public_IP(targetInstance_ID)

    publicIP = '123.235.122.112'
        print 'publicIP = {}'.format(publicIP)
        return publicIP



#Update the hostname



#Notify the SNS Topic





def lambda_handler(event):
    #Find the instance
    targetInstance_ID = get_instance(event)
    
    #Get the Public IP
    public_IP = get_public_IP(targetInstance_ID)
    
    #Get the DNS/hostname to be updated
    hostname = get_instance_hostname(targetInstance_ID)
    
    #Update the hostname
    #Notify the SNS Topic
    print 'Running lambda_handler'










# Update DNS for WHO (HOSTNAME) to WHAT (IP ADDRESS)
if __name__ == '__main__':
    print 'Running Locally?....'
    #Create test event
    event = dict()
    event['instanceID'] = 'i-12345678901234567890'
    lambda_handler(event)
else:
    print '__name__ !=__main__ So this is probably running in AWS'
    print 'ALERT:  You should NOT be seeing this Alert!!'
























