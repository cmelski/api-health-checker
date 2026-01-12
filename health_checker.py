import argparse
import sys

from config_loader import ConfigLoader as conf_loader
from logger import Logger as log
from validator import Validator as validate
from api_util import APIUtility as api_util

# set up the parameters to be passed into the script from the command line:

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--env", type=str)
parser.add_argument("-u", "--endpoint_name", type=str)
args = parser.parse_args()
cli_env = args.env
cli_endpoint = args.endpoint_name

# get the config
try:
    config = conf_loader().config
except:
    log().logger.error(f'Config file not present. Please check configuration.')
    sys.exit()

config_env = config['environment']
config_endpoints = config['endpoints']

# start logging
log().logger.info('API Health Checker started...')
log().logger.info(f'Parameters provided in command line - Environment: {cli_env} / URL: {cli_endpoint}')

# validate CLI env parameter
validate().validate_environment(cli_env, config_env)
# validate CLI endpoint parameter
validate().validate_endpoint(cli_endpoint, config_endpoints)

# Find the matching dict, then get the values for API call
params = (next(item["method"]
               for item in config_endpoints if
               item["name"] == cli_endpoint),
          next(item["url"]
               for item in config_endpoints if
               item["name"] == cli_endpoint),
          next(item["expected_status"]
               for item in config_endpoints if
               item["name"] == cli_endpoint)
          )

method = params[0]
url = params[1]
expected_status_code = params[2]
payload = None


# check if payload exists in config

try:
    payload = next(item["payload"]
                   for item in config_endpoints if
                   item["name"] == cli_endpoint)

    log().logger.info('Payload is present in this endpoint. This is a POST request.')
    log().logger.info(f'Making API Test Call with parameters: {cli_endpoint}, {params[0]}, '
                      f'{params[1]}, {params[2]}, {payload}')
    api_response = api_util().post(endpoint=url, data=payload)
    log().logger.info(f'API response: {api_response.json()}')
    validate().validate_api_response(api_response,expected_status_code, cli_endpoint)
except:
    log().logger.info('Payload not present in this endpoint. This is a GET request.')

    log().logger.info(f'Making API Test Call with parameters: {cli_endpoint}, {params[0]}, '
                      f'{params[1]}, {params[2]}')
    api_response = api_util().get(endpoint=url)
    log().logger.info(f'API response: {api_response.json()}')
    validate().validate_api_response(api_response,expected_status_code, cli_endpoint)


