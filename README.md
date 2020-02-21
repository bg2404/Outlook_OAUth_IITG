# Outlook_OAUth_IITG


### From Azure Portal
* Get App ID and Tenant ID
* Generate a new Secret Key to use
* Save a redirect url
* Add peremissions

### Inside app
* Update oauth_settings.yml
* make sure redirect url defined above exists in your app


### Tips
* Run as localhost not 127.0.0.1 (Azure differentiates between the two)
* Redirect url is slash-sensitive. ('https://www.google.co.in/' and 'https://www.google.co.in' are different) 