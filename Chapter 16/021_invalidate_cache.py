# Script: 021_invalidate_cache.py

import boto3

def invalidate_cache(distribution_id, paths=["/*"]):
    """
    Invalidates the CloudFront cache for the specified distribution and paths.

    :param distribution_id: The CloudFront distribution ID.
    :param paths: The paths to invalidate (default is all files).
    """
    # Initialize the CloudFront client
    cloudfront = boto3.client('cloudfront')

    try:
        # Create a cache invalidation request for the specified distribution and paths
        response = cloudfront.create_invalidation(
            DistributionId=distribution_id,  # CloudFront distribution ID
            InvalidationBatch={
                'Paths': {'Quantity': len(paths), 'Items': paths},  # List of paths to invalidate
                'CallerReference': 'unique-id-cache-invalidation'  # Unique reference for the invalidation request
            }
        )
        # Output the invalidation ID
        print(f"Cache invalidation created successfully. ID: {response['Invalidation']['Id']}")
    
    except Exception as e:
        # Handle errors during cache invalidation
        print(f"Error invalidating cache: {e}")

if __name__ == "__main__":
    # Example: Invalidate the cache for a specific CloudFront distribution
    invalidate_cache("your-cloudfront-distribution-id")
