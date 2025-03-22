# Script: 024_setup_cloudfront.py

import boto3

def setup_cloudfront(bucket_name):
    """
    Sets up a CloudFront distribution for the given S3 bucket.

    :param bucket_name: The name of the S3 bucket to use as the origin for CloudFront.
    """
    # Initialize the CloudFront client
    cloudfront = boto3.client('cloudfront')

    try:
        # Create a CloudFront distribution for the specified S3 bucket
        response = cloudfront.create_distribution(
            DistributionConfig={
                'CallerReference': 'unique-id',  # Unique reference to ensure idempotency
                'Origins': [
                    {
                        'Id': 'S3-' + bucket_name,  # Unique ID for the S3 origin
                        'DomainName': f"{bucket_name}.s3.amazonaws.com",  # S3 bucket domain name
                        'S3OriginConfig': {'OriginAccessIdentity': ''}  # S3 origin access identity (empty for public)
                    }
                ],
                'DefaultCacheBehavior': {
                    'TargetOriginId': 'S3-' + bucket_name,  # Origin ID for the default cache behavior
                    'ViewerProtocolPolicy': 'redirect-to-https',  # Force redirect to HTTPS
                    'AllowedMethods': ['GET', 'HEAD'],  # Allowed HTTP methods
                    'CachedMethods': ['GET', 'HEAD'],  # Methods to be cached
                    'ForwardedValues': {
                        'QueryString': False,  # Do not forward query strings
                    },
                    'MinTTL': 0  # Minimum time-to-live (TTL) for cache (no caching initially)
                },
                'Enabled': True  # Enable the distribution
            }
        )

        # Output the CloudFront distribution ID
        print(f"CloudFront distribution created: {response['Distribution']['Id']}")

    except Exception as e:
        # Handle errors during distribution creation
        print(f"Error creating CloudFront distribution: {e}")

if __name__ == "__main__":
    # Example: Set up a CloudFront distribution for the 'my-react-app-bucket' S3 bucket
    setup_cloudfront("my-react-app-bucket")
