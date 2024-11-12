content = '/html/body/div[1]' #'//div[starts-with(@id, "q-")]'

modal_manager = '/html/body/div[2]' #'//div[starts-with(@id, "q")]'


# XPaths for the main login options on Tinder's login page
xpath_login = '//*[@id="t-342688478"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div'
xpath_continue_google = '//*[@aria-label="Continue with Google"]'
xpath_facebook_login_button = '//*[@aria-label="Log in with Facebook"]'
xpath_sms_phone_number_button = '//*[@aria-label="Log in with phone number"]'

# XPaths for input fields and buttons in Google login popup
xpath_google_email_input = "//input[@type='email']"
xpath_google_password_input = "//input[@type='password']"

# XPaths for elements in Facebook login popup
xpath_facebook_cookie_banner = '//*[@data-cookiebanner="accept_button"]'
xpath_facebook_email_input = '//*[@id="email"]'
xpath_facebook_password_input = '//*[@id="pass"]'
xpath_facebook_login_button_click = '//*[@id="loginbutton"]'

# XPaths for phone number login and country prefix selection
xpath_sms_phone_number_input = '//*[@name="phone_number"]'
xpath_prefix_selection = '//div[@aria-describedby="phoneErrorMessage"]/div/div'

# XPaths for handling popups and notifications
xpath_location_allow_button = '//*[@data-testid="allow"]'
xpath_notification_decline_button = '//*[@data-testid="decline"]'

# XPath for accepting cookies on various pages
xpath_accept_cookies_button = '//*[@type="button"]'

