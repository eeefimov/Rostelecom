# Rostelecom Automated Testing

This project focuses on testing the authorization, registration, and password recovery forms on the Rostelecom Information Technologies site using UI testing with Pytest, Selenium, and Allure reports.

## Introduction
As part of the diploma project's completion, we need to thoroughly test the new authentication interface within the customer's personal account on the Rostelecom Information Technologies site.

## Test Site
- [Rostelecom B2C Passport](https://b2c.passport.rt.ru)

## Implemented Checks

The following checks have been implemented in this project:

- ✅ UI Verify essential elements.
- ✅ UI Verify essential elements' names.
- ✅ UI Verify elements' functionality (e.g., error messages, redirection to different forms).

[![Python application](https://github.com/eeefimov/Rostelecom/actions/workflows/run_tests.yml/badge.svg)](https://github.com/eeefimov/Rostelecom/actions/workflows/run_tests.yml)

Also was completed authorization and new user registration but they do not include to the repository. 
Reason: 
- vpn access sometimes required
- Captch showed up, after several atemps to login (valid or invalid)

## Requirements
- Detailed test requirements can be found [here](https://drive.google.com/file/d/1yMRCT2JT6EWqIWMwW0LSa6mn70_7XYVi/view?usp=sharing).

## Local Tests Run
To run the tests locally, follow these steps:

1. Download the entire project folder along with the `requirements.txt` file.
2. Install project dependencies using the following command:

   ```bash
   pip install -r requirements.txt
- Move to Tests folder. Depending on the environment you are using, run the tests:
- run tests without allure reports: `pytest -v Tests`
- run tests with allure report(allure should be installed on PC):

  `pytest -v -s Tests/ --alluredir="allure_reports`
- **macOS**: `allure serve allure_reports`
- **Windows**: `allure\bin\allure.bat serve allure-results`

##  Examples of issues you will find in the tests file with links. 
