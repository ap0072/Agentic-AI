import boto3

def invalidate_cloudfront(distribution_id, paths=["/*"]):
    client = boto3.client("cloudfront")
    response = client.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            "Paths": {
                "Quantity": len(paths),
                "Items": paths
            },
            "CallerReference": str(hash(str(paths)))
        }
    )
    return response["Invalidation"]["Id"]

