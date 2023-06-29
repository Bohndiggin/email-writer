# email-writer

Email Writer takes a csv of recipients, a csv email style guide, then writes and formats an email for you for each recipient. You can then send the emails.

## Prep/Installation

create a 

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