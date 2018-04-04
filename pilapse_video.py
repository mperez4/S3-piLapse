import argparse
import boto3
import os 

from picamera import PiCamera
from time import sleep, gmtime, strftime 

# create arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--interval', help='input desired capture interval rate')
ap.add_argument('-b', '--bucket', required=True, help='AWS S3 Bucket Name')
args = vars(ap.parse_args())

# parse interval rate
interval = args['interval']

print('[INFO] Capture Interval: ' + str(interval) + ' seconds.')

# s3 setup
s3 = boto3.client('s3')

# parse AWS bucket location
bucketname = args['bucket']
print('[INFO] AWS S3 Bucket: ' + str(bucketname))

# initialize camera
camera = PiCamera()
camera.resolution = (640, 460)
#camera.start_preview()
print('[INFO] Starting Camera...')
sleep(2)

try:
    while True:
        filename ='video/' +  strftime('%Y-%m-%d %H:%M:%S', gmtime()) + '.h264'
        camera.start_recording(str(filename))
        camera.wait_recording(int(interval))

        camera.stop_recording()
        s3.upload_file(filename, bucketname, filename)
        os.remove(filename)
        print('Uploaded: ' + filename)
finally:
        print('[INFO] Stopping Camera...')
        camera.stop_recording
