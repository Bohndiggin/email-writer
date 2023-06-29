# email-writer

Email Writer takes a csv of recipients, a csv email style guide, then writes and formats an email for you for each recipient. You can then send the emails.

## Prep/Installation

1. Create a .env file with ```EMAIL_ADDRESS="youremail@example.com"```
2. For Gmail accounts you need to go here https://myaccount.google.com/security
3. Click on '2-Step Verification'
4. Scroll to bottom and click on 'app passwords'
5. Add a new password.
6. copy password and add to the .env file as ```EMAIL_SECRET="password"```
7. This authorizes email-writer to send an email on your behalf. DO NOT UPLOAD .env Keep it a secret.

## GENERAL USE

1. Write an email and split it up into phrases (see /examples/example_author_style.csv)
2. Make a .csv of your recipients (see /examples/example_recipient_list.csv)
3. Open Email-Writer
4. Edit > Documents > Add Document Type...
5. Enter a name (this will be the SUBJECT LINE)
6. Enter a Description (for you only)
7. Edit > Authors > Add Author Style...
8. Choose your author style .csv and click Open
9. Name your author and choose which document it'll write
10. Click on your document, then the author
11. File > Load Recipients
12. Choose the recipients .csv
13. File > Write Emails
14. Program will write the emails by choosing phrases from each line to construct the email, then it will format the document to replace the keys in the recipient list with the values of the current recipient.
15. Send will send the email, <> are navigation