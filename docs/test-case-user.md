# User

## Login

1. Login Page:

   1. Navigate to the "Login" page
   2. Try to submit the empty form and verify that an error message about the required fields appears
   3. Try to submit the form with an invalid email address and verify that a relevant error message appears
   4. Try to submit the form with all inputs valid and verify that a success message appears.

## Password

1. Password Reset Request:

   1. Navigate to the "Login" page
   2. Click on Forgot Password? link
   3. Enter an invalid email address, verify you get a successful message so a malicious user won't be provided with the information than an account already exists.
   4. Try to submit the form with a valid email address and verify that a success message appears. Check your email inbox and verify that a new message to reset the password is received.

2. Password Reset Complete:
   1. Perform steps on (1)
   2. Click on the email link to perform a password reset.
   3. Try to submit the empty form and verify that an error message about the required fields appears
   4. Try to submit the form with an invalid password and verify that a relevant error message appears
   5. Try to submit the form with passwords that won't match and verify that a relevant error message appears
   6. Try to submit the form with all inputs valid and verify that a success message appears.
   7. Try reusing the same email link and verify you get an error message stating the link is no longer valid.

## Register

1. User Registration:
   1. Navigate to the "Register" page
   2. Try to submit the empty form and verify that an error message about the required fields appears
   3. Try to submit the form with invalid fields and verify that a relevant error message appears
   4. Try to submit the form with all inputs valid and verify that a success message appears.
   5. After login, verify that the user is logged in by checking that the LOGIN and REGISTER menu options have changed to PROFILE and LOGOUT

## Profile

1. View and Edit Profile:
   1. Log in with any user
   2. Navigate to the "Profile" page
   3. Verify that all the information displayed is what was registered for your account
   4. Click on Edit Profile button
   5. Try to submit the form with invalid fields and verify that a relevant error message appears
   6. Try to submit the form with all inputs valid and verify that a success message appears.
   7. Verify that the updated information now appears in the profile page

## User Permissions

1. Superuser or Staff User:

   1. Log in with an admin account
   2. Verify that two new menu options appear: ALL ENTRIES and ADMIN
   3. Try accessing the ADMIN menu, it should display the Django Admin Panel
   4. Go back and access ALL ENTRIES, verify it display both NEWS and BLOG posts in the same page
   5. Go to any post and click "Read More", verify that an "Edit Post" button appears and clicking it will take you to the "Edit Post" form

2. Contributor user:

   1. Log in with a contributor account
   2. Verify that ALL ENTRIES and ADMIN options won't appear
   3. Try navigating to the ADMIN panel by typing the url, verify an error message appears not granting access
   4. Go back and access ALL ENTRIES, verify it display both NEWS and BLOG posts in the same page
   5. Go to any post and click "Read More", verify that an "Edit Post" button appears and clicking it will take you to the "Edit Post" form

3. Regular user:
   1. Log in with a regular user account
   2. Verify that one new menu options appear: ALL ENTRIES
   3. Try navigating to the ADMIN panel by typing the url, verify an error message appears not granting access
   4. Go to any post and click "Read More", verify that an "Edit Post" button won't appear
