# reminder

## Pre-requisites:
* pip install -r requirements.txt
* For sms reminder to work do the following:
  * Install [SMS Gateway API app](https://play.google.com/store/apps/details?id=networked.solutions.sms.gateway.api) from android play store.
  * Open the app and use the Device ID in reminder/settings/local.py as SMS_DEVICE_ID
* Install rabbitmq.

### After this do the following:
* Create a database on postgres with name **reminder**
* Create a user on postgres **lastfmuser** with password **lastfmpass**
* Give admin access to **lastfmuser**
* Grant all privileges on **reminder** to **lastfmuser**
* Run the following commands:
  ```
  ./manage.py makemigrations 
  ```
  ```
  ./manage.py migrate
  ```
* Start the rabbitmq server
  ```
  sudo rabbitmq-server start
  ```
* Start celery with the command
  ```
  celery -A reminder worker -l info
  ```
* Start the server
  ```
  ./manage.py runserver
  ```
  

## API docs
Action | Url | Method | Data | Headers | Remarks 
------ | --- | ------ | ---- | ------- | -------
To create a user | localhost:8000/drip/user/ | POST | <ul><li>email (O)</li><li>phone (O)</li></ul> | Content-Type = 'application/json' | Either of email or phone needs to be passed. phone should be exactly 10 characters.
To update a user if either phone or email is present | localhost:8000/drip/user/ | PUT | <ul><li>email (M)</li><li>phone (M)</li></ul> | Content-Type = 'application/json' | Both email and phone needs to be passed where either of them is already registered. phone should be exactly 10 characters.
To get initial data of all users and reminder_type | localhost:8000/drip/user/ | GET | | Content-Type = 'application/json' | While sending request to /remind api, use reminder_mode id.
To schedule a reminder | localhost:8000/drip/remind/ | POST | <ul><li>user (M)</li><li>scheduled_time (M)</li><li>reminder_type (M)</li><li>msg (M)</li></ul> | Content-Type = 'application/json' | <ul><li>user should be user id</li><li>scheduled_time should be UTC time in format "YYYY-MM-DD hh:mm:ss"</li><li>reminder_type should be a list of reminder_mode id</li><li>msg is a string</li></ul>
**Note:**
* **M** - Mandatory
* **O** - Optional