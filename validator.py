import sys

from logger import Logger as log


class Validator:

    def __init__(self):
        pass

    def validate_environment(self, cli_env: str, config_env: str) -> None:
        try:
            assert cli_env == config_env, (f'Environment provided incorrect. '
                                           f'Expected: {config_env} Actual:{cli_env}')
            log().logger.info(f'CL environment parameter passed. Expected: {config_env} Actual: {cli_env} ')
        except AssertionError as err:
            log().logger.exception(f'An assertion error occurred. Environment provided incorrect.'
                                   f'Expected: {config_env} Actual: {cli_env}')
            log().logger.info('Exiting script.')
            sys.exit()

    def validate_endpoint(self, cli_endpoint: str, config_endpoints: list):

        is_found = any(d['name'] == cli_endpoint for d in config_endpoints)

        try:
            assert is_found, f'CL endpoint parameter incorrect. {cli_endpoint} not present in config'
            log().logger.info(f'CL endpoint parameter passed. {cli_endpoint} exists in config.')
        except AssertionError as err:
            log().logger.exception(f'An assertion error occurred. {cli_endpoint} not present in config.')
            log().logger.info('Exiting script.')
            sys.exit()

    def validate_api_response(self, api_response: dict, expected_status_code: str, cli_endpoint: str):

        api_response_status_code = api_response.status_code

        try:
            assert api_response.status_code == expected_status_code, (f'API response status code incorrect. Expected: '
                                                                      f'{expected_status_code} / Actual: {api_response_status_code}')
            log().logger.info(f'API status code correct: {api_response_status_code}')
            log().logger.info(f'API Health Check for endpoint {cli_endpoint} passed.')
        except AssertionError as err:
            log().logger.exception(
                f'An assertion error occurred. {expected_status_code} not received. {api_response_status_code}'
                f'received instead.')
            log().logger.info('Exiting script.')
            sys.exit()
