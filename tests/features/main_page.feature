Feature: As a user, I want to see the correct design in the landing page.

    Scenario: Verify NavBar links
        Given that I go to the landing page
        When I go to the navigation bar
        Then I see the links "Work, Services, About, Insights, Careers, Contact".

    Scenario: Verify the title on the home page.
        Given that I go to the landing page
        When I go to the title
        Then I can see the title "The Connected TV App Experts".

    Scenario: Verify fields and the contact form.
        Given that I go to the landing page
        When I scroll to the contact form
        Then I can see a form with the fields "first name*, last name*, email address*, phone number, company/organisation website*, message*, CAPTCHA"
        And I can see a "Send" button.