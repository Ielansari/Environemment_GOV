import os
import requests
from hdfs import InsecureClient

# Apache Atlas REST API endpoint
atlas_url = "http://host.docker.internal:21000/api/atlas/v2"

# Authentication credentials if required
auth = ("admin", "admin")  # If authentication is enabled

# Function to create entity in Apache Atlas
def create_entity(entity_type, attributes):
    headers = {'Content-Type': 'application/json'}
    url = f"{atlas_url}/entity/{entity_type}"
    data = {
        'entity': {
            'typeName': entity_type,
            'attributes': attributes
        }
    }
    response = requests.post(url, headers=headers, auth=auth, json=data)
    if response.status_code == 200:
        print(f"Entity '{entity_type}' created successfully.")
    else:
        print(f"Failed to create entity '{entity_type}'. Error: {response.text}")


hdfs_client = InsecureClient('http://localhost:50070', user='admin')


hdfs_directory = "/data/news_documents_data"


directory_contents = hdfs_client.list(hdfs_directory)

# Iterate over files in the HDFS directory
for filename in directory_contents:
    hdfs_filepath = os.path.join(hdfs_directory, filename)
    # Example metadata attributes for each file
    attributes = {"name": filename, "type": "file"}
    create_entity("hdfs_path", attributes)