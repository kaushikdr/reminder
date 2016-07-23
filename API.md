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
To create a user | localhost:8000/drip/user/ | POST | <ul><li>email (O)</li><li>phone (O)</li></ul> | Content-Type = 'application/json' | Either of email or phone needs to be passed


