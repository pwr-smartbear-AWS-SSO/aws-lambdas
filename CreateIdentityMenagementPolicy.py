import boto3
import json

def lambda_handler(event, context):
    
    client = boto3.client('iam')
    cognit_pool_arn = event['key1']
    policy_name = event['key2']
    
    policy_document = {
    "Version": "2012-10-17",
    "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "cognito-idp:DeleteIdentityProvider",
                    "cognito-idp:UpdateIdentityProvider",
                    "cognito-idp:CreateIdentityProvider"
                ],
                "Resource": cognit_pool_arn
            }
        ]   
    }

    response = client.create_policy(
    PolicyName=policy_name,
    PolicyDocument = json.dumps(policy_document)
    )


    #response = json.loads(json.dumps(response, default=str))
    return response["Policy"]["Arn"]
