# S3-piLapse

S3-piLapse are simple scripts to set up streams of images or video into your AWS S3 buckets from your raspberry pi.
These scripts will upload files into your S3 bucket with an interval rate until you stop the script. Files are not stored locally.

It uses boto3 and PiCamera. 
### Install 

First, install the library and set a default region:


    $ pip install boto3

Next, set up credentials (in e.g. ``~/.aws/credentials``):


    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

### Usage

pilapse_video.py will upload video clips from your pi into your AWS bucket. Simply run: 

'''python pilapse_video.py -i video_duration_rate_seconds -b your_bucket_name'''

pilapse_image.py will upload images from your pi into your AWS bucket. Simply run:

'''python pilapse_video.py -i image_interval_rate_seconds -b your_bucket_name'''
