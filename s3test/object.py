#!/usr/bin/python
import boto
import boto.s3.connection
access_key = '096AKCQEC8N1PYC42QSN'
secret_key = 'EmeHO66qKgqQlwpGEBAFd138khygJs1ZqzG0OapT'
conn = boto.connect_s3(
				aws_access_key_id = access_key,
				aws_secret_access_key = secret_key,
				host = 'client6', port = 9000,
				is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat(),
				)

def create_bucket(bucket_name):
    bucket = conn.create_bucket(bucket_name)
    return bucket

def list_bucket():
    print "... List bucket ... "
    for bucket in conn.get_all_buckets():
        print "\t{name}".format(
        name = bucket.name,
        )

def list_bucket2():
    print "... List bucket ... "
    for bucket in conn.get_all_buckets():
        print "\t{name}\t{created}".format(
        name = bucket.name,
        created = bucket.creation_date,
        )
    
def delete_bucket(bucket_name):
    conn.delete_bucket(bucket_name)

def create_object(bucket, key, content):
    key = bucket.new_key(key)
    key.set_contents_from_string(content)

def create_object_from_file(bucket, key, filename):
    key = bucket.new_key(key)
    key.set_contents_from_filename(filename)

def list_object(bucket):
    for key in bucket.list():
        print "\t{name}\t{size}\t".format(
            name = key.name,
            size = key.size,
            )

def list_object2(bucket):
    for key in bucket.list():
        print "\t{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
            )

def delete_object(bucket, key):
    bucket.delete_key(key)

def download_object(bucket, key, filename):
    key = bucket.get_key(key)
    key.get_contents_to_filename(filename)

def get_object_as_str(bucket, key):
    key = bucket.get_key(key)
    print key.get_contents_as_string()

if __name__ == "__main__":
    bucket_name="bucket2"
    print "\n... Create bucket (%s) ..." % bucket_name
    bucket = create_bucket(bucket_name)
    list_bucket()
    
    key = "obj1"
    content = "Hello World!!\n"
    print "\n... Create object (%s) ..." %key
    create_object(bucket, key, content)

    print "... List object ..."
    list_object(bucket)

    print "\n... get content of object (%s) ..." % key
    get_object_as_str(bucket, key)

    filename = "/root/s3test/%s" %key
    print "... Download object (%s) to %s ..." %(key, filename)
    download_object(bucket, key, filename)

    #print "\n... Delete object (%s) ..." %key
    #delete_object(bucket, key)
    #print "... List object ..."
    #list_object(bucket)

    #print "\n... Delete bucket (%s) ..." % bucket_name
    #delete_bucket(bucket_name)
    #list_bucket()
    #print


