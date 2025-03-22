# Script: 028_modify_redis_cluster.py

import boto3

def modify_redis_cluster(cluster_id):
    elasticache_client = boto3.client('elasticache')
    try:
        response = elasticache_client.modify_cache_cluster(
            CacheClusterId=cluster_id,
            ApplyImmediately=True,
            CacheNodeType='cache.t3.micro'
        )
        print(f"Redis cluster '{cluster_id}' modified successfully.")
        print(response)
    except Exception as e:
        print(f"Error modifying Redis cluster: {e}")

if __name__ == "__main__":
    modify_redis_cluster("my-redis-cluster")
