# external imports
from os.path import dirname, realpath


#
# VARIABLES
#


ROOT_DIR = dirname(realpath(__file__))

aws_test_server_ip = '3.89.41.136'
aws_access_key_id = ''
aws_secret_access_key = ''
aws_s3_bucket_title = ''

driver_wait_in_sec = 10


#
# SELENOID
#

selenoid_options = {
    'chrome106': {
        "browserName": "chrome",
        "browserVersion": "106.0",
        "platform": "linux",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False,
            "videoName": "chrome106.mp4"
        }
    },
    'chrome104': {
        "browserName": "chrome",
        "browserVersion": "104.0",
        "platformName": "linux",
        "selenoid:options": {
            "enableVNC": False,
            "enableVideo": False,
            "videoName": "chrome104.mp4"
        }

    }
}


#
# ENV
#


env_options = {
    'prod': {
        'frontend_url': 'https://www.foodrocket.me/',
        'backend_url': '',
    },
    'test': {
        'frontend_url': '',
        'backend_url': '',
    },
}
