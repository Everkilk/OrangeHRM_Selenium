# OrangeHRM Testing Project – Software Testing Report Summary

**Description:** Conducted comprehensive testing for a human resources management system, focusing on manual, black-box, and automated testing using Selenium WebDriver and pytest.

**Technologies:** Python, Selenium WebDriver, pytest, Page Object Model (POM), Microsoft Excel, pytest-html, Black-Box Testing, Equivalence Partitioning, Boundary Value Analysis

**Responsibility:**
- Performed manual and black-box testing across 6 modules (Login, Dashboard, Leave, Employee Management, Admin, and Personal Info) to identify defects and ensure software quality.
- Developed and executed 65 automated test cases using Selenium WebDriver and pytest, following the Page Object Model (POM) design pattern to verify UI and functional behavior.
- Documented test scenarios, test cases, and generated HTML test reports using pytest-html for test result tracking and defect documentation.

---

## Manual Test Scenarios & Test Cases

### Module 1 – Login

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Validate login form inputs | Enter username only, leave password empty → expect error message |
| 2 | Validate login form inputs | Enter an invalid email format in the username field → expect validation error |
| 3 | Validate login form inputs | Leave both username and password empty → expect error message |
| 4 | Validate login form inputs | Enter a valid username with an incorrect password → expect "Invalid credentials" error |
| 5 | Successful authentication | Enter valid username and password → expect redirect to Dashboard |
| 6 | Forgot Password navigation | Click "Forgot Password" link → expect navigation to the Reset Password page |
| 7 | Forgot Password cancellation | Click "Cancel" on the Forgot Password page → expect return to Login page |
| 8 | Reset password flow | Submit a valid username on the Forgot Password page → expect confirmation message |
| 9 | UI visibility | Open the Login page → expect the OrangeHRM logo to be visible |
| 10 | UI visibility | Open the Login page → expect the page title text to be correct |
| 11 | UI visibility | Open the Login page → expect the page title element to be visible |
| 12 | Social media links | Open the Login page → expect the LinkedIn icon to be present and linked correctly |
| 13 | Social media links | Open the Login page → expect the Facebook icon to be present and linked correctly |
| 14 | Social media links | Open the Login page → expect the Twitter icon to be present and linked correctly |
| 15 | Social media links | Open the Login page → expect the YouTube icon to be present and linked correctly |
| 16 | Equivalence partitioning | Supply invalid user credentials from a data set → expect login to fail for all invalid partitions |
| 17 | Link integrity | Scan all hyperlinks on the Login page → expect no broken links (HTTP 200) |

---

### Module 2 – Dashboard

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Page identity | Navigate to Dashboard → expect page heading to display "Dashboard" |
| 2 | Widget navigation | Click the Time & Attendance widget → expect the Clock page to open |
| 3 | Widget navigation | Click the Performance widget → expect the Performance page to open |
| 4 | Widget navigation | Click "Assign Leave" shortcut → expect the Assign Leave page to open |
| 5 | Widget navigation | Click "Leave List" shortcut → expect the Leave List page to open |
| 6 | Widget navigation | Click "Timesheets" shortcut → expect the Timesheets page to open |
| 7 | Widget navigation | Click "Apply Leave" shortcut → expect the Apply Leave page to open |
| 8 | Widget navigation | Click "My Leave" shortcut → expect My Leave page to open |
| 9 | Widget navigation | Click "My Timesheet" shortcut → expect My Timesheet page to open |
| 10 | Widget navigation | Open Employee Leave Settings from the Dashboard → expect the correct settings page |
| 11 | Widget navigation | Click the Buzz widget → expect the Buzz page to open |
| 12 | Screen capture | Capture screenshots of all Dashboard sections → expect no rendering errors |
| 13 | Chart display | Check the Employee Distribution chart → expect it to be visible with data |
| 14 | Sidebar navigation | Click each item in the Admin sidebar from the Dashboard → expect all links to work |
| 15 | Link integrity | Scan all hyperlinks on the Dashboard → expect no broken links |

---

### Module 3 – Leave

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Menu access | Click the Leave menu item in the sidebar → expect the Leave page to load |
| 2 | Leave list display | Open the Leave List sub-menu → expect a table of leave records to appear |
| 3 | Search reset | Click the Reset button on the Leave List filter form → expect all filter fields to be cleared |
| 4 | Field validation | Submit the Leave List filter with the From Date field empty → expect a validation error |
| 5 | Field validation | Submit the Leave List filter with the To Date field empty → expect a validation error |
| 6 | Field validation | Submit the Leave List filter with the Status field empty → expect a validation error |
| 7 | Field validation | Submit the Leave List filter with all fields empty → expect validation errors on required fields |

---

### Module 4 – Employee Management (PIM)

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Menu navigation | Click the PIM menu item → expect the Employee List page to load |
| 2 | Add employee | Click the Add button → expect the Add Employee form page to open |
| 3 | Search by name | Enter an employee name in the search box → expect matching employees to appear in results |
| 4 | Search by ID | Enter an employee ID in the search box → expect the matching employee to appear |
| 5 | Filter by job title | Select a job title from the Job Title dropdown → expect the list to filter accordingly |
| 6 | Filter by status | Select an employment status from the Status dropdown → expect the list to filter accordingly |
| 7 | Filter by include option | Select an option from the Include dropdown → expect the list to reflect the selection |
| 8 | Filter by sub-unit | Select a sub-unit from the Sub Unit dropdown → expect the list to filter accordingly |
| 9 | Supervisor search | Enter a supervisor name in the Supervisor Name field → expect matching results |
| 10 | Reset filters | Click the Reset button → expect all search filter fields to be cleared |

---

### Module 5 – Admin

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Admin page access | Log in and navigate to the Admin page → expect the User Management table to be visible |
| 2 | Search users | Enter a username in the search field → expect matching system users to appear |
| 3 | Filter by role | Select a system role from the dropdown → expect users filtered by that role |
| 4 | Filter by employee name | Enter an employee name → expect users associated with that employee to appear |
| 5 | Filter by status | Select Active or Inactive from the Status dropdown → expect the list to filter accordingly |
| 6 | Add user button | Click the Add button → expect the Add User form to open |
| 7 | Add new user | Fill in the Add User form with valid data and submit → expect the new user to appear in the list |

---

### Module 6 – Personal Info (My Info)

| # | Scenario | Test Case |
|---|----------|-----------|
| 1 | Page access | Log in and navigate to My Info → expect the Personal Details form to be visible |
| 2 | Edit first name | Clear and type a new value in the First Name field → expect the field to accept the input |
| 3 | Edit middle name | Clear and type a new value in the Middle Name field → expect the field to accept the input |
| 4 | Edit last name | Clear and type a new value in the Last Name field → expect the field to accept the input |
| 5 | Date of birth | Select a date from the Date of Birth date picker → expect the selected date to be displayed |
| 6 | Dropdown selection | Select a value from the Gender / Nationality dropdown → expect the value to be selected |
| 7 | Form action button | Click the Save button → expect a success confirmation message |
| 8 | Blood group | Select a blood group from the Blood Type dropdown → expect the value to be saved |
| 9 | Form submission | Fill in all required fields and click Save → expect the form to submit successfully |
