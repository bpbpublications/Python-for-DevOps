# Script: 027_create_redis_cluster.py

import boto3

def create_redis_cluster(cluster_id):
    elasticache_client = boto3.client('elasticache')
    try:
        response = elasticache_client.create_cache_cluster(
            CacheClusterId=cluster_id,
            Engine='redis',
            CacheNodeType='cache.t2.micro',
            NumCacheNodes=1,  # Single-node cluster
            SecurityGroupIds=['your-security-group-id']
        )
        print(f"Redis ElastiCache cluster '{cluster_id}' is being created.")
        print(response)
    except Exception as e:
        print(f"Error creating Redis cluster: {e}")

if __name__ == "__main__":
    create_redis_cluster("my-redis-cluster")
