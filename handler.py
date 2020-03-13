import json

import boto3


import os
grupo = os.environ['GROUP']

codepipeline = boto3.client('codepipeline')

def main(event, context):
    print(str(event))
    print(str(context))
    
    
    responsePipeline = codepipeline.start_pipeline_execution(
        name='hackathon-CD-app-stack',
    )
    
    response = {
        'statusCode': 200,
        'body': json.dumps(responsePipeline)
    }
    
    return response
    
    
   
    
