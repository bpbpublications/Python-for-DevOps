# Script: 020_create_cloudfront_distribution.py

import boto3

def create_cloudfront_distribution(bucket_name):
    """
    Creates a CloudFront distribution for the given S3 bucket.

    :param bucket_name: The name of the S3 bucket to be used as the origin for CloudFront.
    """
    # Initialize the CloudFront client
    cloudfront = boto3.client('cloudfront')

    try:
        # Create the CloudFront distribution
        response = cloudfront.create_distribution(
            DistributionConfig={
                'CallerReference': 'unique-id',  # Unique reference for the distribution request
                'Origins': [
                    {
                        'Id': 'S3-' + bucket_name,  # The ID for the S3 origin
                        'DomainName': f"{bucket_name}.s3.amazonaws.com",  # S3 bucket domain name
                        'S3OriginConfig': {'OriginAccessIdentity': ''}  # Config for S3 access identity
                    }
                ],
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'S3-' + bucket_name,  # The ID of the origin to be used for caching
                    'ViewerProtocolPolicy': 'redirect-to-https',  # Enforce HTTPS for viewers
                    'AllowedMethods': ['GET', 'HEAD'],  # Allowed HTTP methods
                    'CachedMethods': ['GET', 'HEAD'],  # Cached HTTP methods
                    'ForwardedValues': {
                        'QueryString': False,  # Do not forward query strings
                        'Cookies': {'Forward': 'none'}  # Do not forward cookies
                    },
                    'MinTTL': 0,  # Minimum TTL for cached content
                    'DefaultTTL': 86400,  # Default TTL for cached content (1 day)
                    'MaxTTL': 31536000  # Maximum TTL for cached content (1 year)
                },
                'Enabled': True  # Enable the distribution
            }
        )

        # Output the CloudFront distribution ID
        print(f"CloudFront distribution created successfully. ID: {response['Distribution']['Id']}")
    
    except Exception as e:
        # Handle errors during distribution creation
        print(f"Error creating CloudFront distribution: {e}")

if __name__ == "__main__":
    # Example: Create a CloudFront distribution for the 'my-frontend-assets' S3 bucket
    create_cloudfront_distribution("my-frontend-assets")
