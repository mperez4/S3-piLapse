import argparse
import boto3
import os 

from picamera import PiCamera
from time import sleep 

# create arguments
ap = argparse.ArgumentParser(description='Timelapse to AWS S3.')
ap.add_argument('-i', '--interval', required=True, help='Timelapse interval rate (seconds).')
ap.add_argument('-b', '--bucket', required=True, help='AWS S3 Bucket Name')
args = vars(ap.parse_args())

# parse interval rate
interval = args['interval']
print('[INFO] Capture Interval: ' + str(interval) + ' seconds.')

# parse AWS bucket location 
bucketname = args['bucket']
print('[INFO] AWS S3 Bucket: ' + str(bucketname))

# s3 setup
s3 = boto3.client('s3')

# initialize camera
camera = PiCamera()
camera.resolution = (640, 460)
#camera.start_preview()
print('[INFO] Starting Camera...')
sleep(2)

try:
    for filename in camera.capture_continuous('images/{timestamp:%Y-%m-%d %H:%M:%S}.jpg'):
        sleep(float(interval))
        s3.upload_file(filename, bucketname, filename)
        print('Uploaded: %s' % filename)
        os.remove(filename)
finally:
    print('[INFO] Stopping Camera...')
    camera.stop_recording

