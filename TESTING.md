### Issues
- Email confirmation not loading in terminal
    - Attempted to fix with try/except statements, printing the error in the terminal if there is an issue sending the email. 
        - No issues with sending the email detected but confirmation still not showing in the terminal.
    - Added a print statement to check that the _send_confirmation_email() function is being called
        - Statement not printed in terminal indicating an issue with the function being called and executed.
    - In python shell I tested the email functionality outside of the webhook handler context in order to isolate the issue. 
        - The confirmation email successfully printed in the terminal 