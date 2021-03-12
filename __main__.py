"""A Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a storage bucket in GCP
bucket = storage.Bucket('my-bucket')

# Export the DNS name of the bucket
pulumi.export('bucket_name',  bucket.url)
