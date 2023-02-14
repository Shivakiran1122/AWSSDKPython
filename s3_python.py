import boto3;
BucketName="shivasampledemo"
s3= boto3.client("s3")

#-------------------------------------------------------------------------------------------------------------------

# 1. List all the buckets
#--------------------------

#buckets_response=s3.list_buckets()
#for bucket in buckets_response["Buckets"]:
    #print(bucket)



# 2. List all the objects inside the bucket
#------------------------------------------

#response=s3.list_objects_v2(Bucket=BucketName)
#for obj in response["Contents"]:
    #print(obj)


# 3. Upload files to bucket
#--------------------------

#with open("./burger.jpg","rb") as f:
    #s3.upload_fileobj(f,BucketName,"burger_new_upload.jpg",ExtraArgs={"ACL":"public-read"})
    


# 4. Downloading file
#---------------------

# s3.download_file(BucketName,"lion.jpg","downloaded_lion.jpg")



# 5. Download  file with binary data
#-----------------------------------

#with open("lionimage.jpg","wb") as f:
    #s3.download_fileobj(BucketName,"lion.jpg",f)
    


# 6. presigned url to give limited access  to an unauthorized user
#-----------------------------------------------------------------

#url=s3.generate_presigned_url("get_object",Params={"Bucket":BucketName,"Key":"lion.jpg"},ExpiresIn=0)
#print(url)



# 7. Create Bucket
#-----------------

#bucket_location=s3.create_bucket(Bucket="new-s3-buckets")
#print(bucket_location)



# 8. copy objects to other bucket
#--------------------------------

#s3.copy_object(Bucket="new-s3-buckets",CopySource=f"/{BucketName}/lion.jpg",Key="new-lion.jpg")



# 9. Get Object
#--------------

response=s3.get_object(Bucket=BucketName,Key="burger_new_upload.jpg")
print(response)






