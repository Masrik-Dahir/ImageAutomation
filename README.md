# ImageAutomation

S3 triger permisison: aws s3api put-bucket-notification-configuration --bucket masrikdahir --cli-input-json file://IAM/trigger.json


aws s3api get-bucket-notification-configuration --bucket masrikdahir-image                                                                         
{                                                                                                                                                                                                                                                                                                                  
    "LambdaFunctionConfigurations": [                                                       
        {
            "Id": "N2FjMDFkZDItNDE5YS00MDRhLTlhMGMtMmM1NzRkNzg1NzRl",
            "LambdaFunctionArn": "arn:aws:lambda:us-east-1:608089521175:function:ImageAutomation",
            "Events": [
                "s3:ObjectCreated:*"
            ]
        }
    ]
}



aws lambda get-policy --function-name ImageAutomation                                                                                        
{                                                                                                                                                                                                                                                                                                                  
    "Policy": "{\"Version\":\"2012-10-17\",\"Id\":\"default\",\"Statement\":[{\"Sid\":\"ImageAutomation-ImageAutomationPermissionFromS3-JI1Jva0p64Oi\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"s3.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-1:608089521175:function:ImageAutomation\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:s3:::masrikdahir\"}}}]}",
    "RevisionId": "64f3c122-e156-44ea-a588-bd71cc6d941e"
}

sam build --no-cached; sam deploy --guided;