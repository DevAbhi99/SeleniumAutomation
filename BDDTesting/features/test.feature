Feature: Test the Orange HRM

Scenario Outline: Test successful login
Given The user is on the login page
When the user provides correct username "<username>" and password "<password>" 
And The user clicks on the login button
Then The user go to the Orange HRM main page

Examples:
    | username | password | 
    | Admin  | admin123  | 


Scenario: Test the availability of jobs
Given When the user is on the main page
When the user clicks on Admins tab
And The user clicks on Jobs tab and then Jobs title tab
Then The jobs are displayed and a screenshot is taken


Scenario: Testing the logout functionality
Given The user is on the main page
When The user clicks on profile tab and dropdown icon
And The user clicks on the logout button
Then The user is logged out