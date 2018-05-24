import boto3
import configparser
import logging
import requests
import sys

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class GitHubS3Sync:
    def __init__(self, repository, bucket):
        # Check GitHub repository path provided
        if 'github.com' in repository:
            # USE REQUESTS TO TEST PATH HERE

            # IF VALID PATH
            self.repository = repository

            if self.repository[-1] != '/':
                self.repository += '/'

            self.repository += 'archive/latest.zip'

            logger.debug('self.repository: ' + self.repository)

        else:
            logger.error('Invalid repository path. Exiting.')

            sys.exit(1)

        # Check AWS S3 path provided
        if 's3://' in bucket:
            # USE BOTO3 TO TEST PATH AND CREDENTIALS HERE

            # IF VALID PATH
            self.bucket = bucket

        else:
            logger.error('Invalid S3 bucket path. Exiting.')

            sys.exit(1)


    def copy_file_s3(self):
        pass


    def check_repository_changes(self):
        # Check if any new changes

        # If changes made since last check, get repo-master.zip

        # Copy repo-master.zip to s3 bucket

        pass


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(config_path)

    gs = GitHubS3Sync(repository='https://github.com/hmallen/TeslaBot',
                      bucket='s3://teslabot')
