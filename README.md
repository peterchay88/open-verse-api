# open-verse-api

## About
This project is a test framework based off a take home assessment for a QA Automation or SDET
position. 

## Task
Please tinker around with the OpenVerse API: https://api.openverse.engineering/v1/ and create a basic automation framework using the language and tools of your choice to test the standard operations of the API. (You will need to create an account with Openverse to do this.)

Please create test cases (Positive and Negative) for the below endpoints 
- POST /v1/auth_tokens/register/ (After this endpoint is hit, you must manually click a link that is sent to you as an email before you can test the other endpoints.) 
- POST /v1/auth_tokens/token/ 
- GET /v1/audio/ 
- GET /v1/audio/stats/ 

Bonus Tests:
On the /v1/audio/ endpoint response, assert the first entry in results array has the field “id” and the value is a valid UUID v4
Automate the email verification process while keeping your email credentials stored securely
