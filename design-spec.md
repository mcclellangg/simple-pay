# Functional Design Spec

## Concept brief

<p>Simple pay will be a desktop payroll management application. It will give users the ability to create, and manage employee paychecks. This system will be broken up into three main features: Company Management, Record Display, and Paycheck Auto Calulator.</p>

## Main features

1. Company Management
    - Allows for creation of a company, really just initializes a blank db for the user to fill.

2. Paycheck Auto Calculator
    - Given employee name, gross pay, and number of exemptions will automatically calculate all deductions (federal, social security, medicare, state, and net) and return employee net pay.

3. Record Display
    - Will keep track of paychecks in chronological order
    - Will allow user to query database in specific ranges:
        - All
        - this week
        - this month
        - last week
        - last month
    - Will allow user to delete / update paycheck objects based on oid

## Deadlines

- [ ] By 11/26 Create git repo with completed design spec, and deadlines
- [ ] By 12/4 Create Load Screen with all basic features
    - Creat ecompany initialization screen with all basic features
    - Create 6 months of payroll data to get an idea how to best display it to user
- [ ] By 12/17 Create Record Display/Management with all basic and related features
- [ ] By 12/23 Have first round final product (all main features completed) ready for deployment testing

## Possible expansion of features/general improvements

<p>In a more advanced version it would be nice for the user to manage employees seperate from paychecks, and store more employee info. But I don't see how that is currently relevant to the most basic functionalites of the app (a paycheck manager) so I will leave it alone for now.</p>

<p>Once I get the app working, I will try to go back and sort functionalites into seperate classes to make the code cleaner, but for now I just want to get it up and running, and don't want to get too bogged down in that, since for me that would likely be an entirely seperate issue that will take significant time for me to address</p>
