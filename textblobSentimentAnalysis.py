import os
import uuid

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:


    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    print(connect_str)
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    #     # Create a unique name for the container
    container_name = str(uuid.uuid4())

    #     # Create the container
    container_client = blob_service_client.create_container(container_name)

    # Create a file in the local data directory to upload and download
    local_file_name = "updated_csv" + ".csv"
    upload_file_path = os.path.join("./", local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

    print("\nListing blobs...")

    print(container_name)
    # List the blobs in the container
    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print("\t" + blob.name)

except Exception as ex:
    print('Exception:')
    print(ex)