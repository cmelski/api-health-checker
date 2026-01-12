Config-Driven API Health Checker (Python)

A production-quality, config-driven API health checker built in Python.
Designed to demonstrate clean engineering, validation, logging, and error handling.

Project Goals

This project was built to demonstrate:

-Writing clean, maintainable Python

-Designing config-driven test tools

-Validating inputs defensively

-Logging execution clearly and meaningfully

-Handling failures gracefully (without crashing or hiding errors)

-Structuring code as production software, not scripts

What This Tool Does

The script:

-Reads a JSON configuration file

-Validates the configuration

-Sends HTTP requests to configured endpoints

-Logs execution details and results

-Reports failures clearly and exits cleanly

No code changes are required to add or remove endpoints — behavior is driven entirely by config.

How to run:

python health_checker.py -e test -u add_product_api
