# API docs
Action | Url | Method | Data | Headers | Remarks 
------ | --- | ------ | ---- | ------- | -------
To create a user | localhost:8000/drip/user/ | POST | <ul><li>email (O)</li><li>phone (O)</li></ul> | Content-Type = 'application/json' | Either or both of email or phone needs to be passed. phone should be exactly 10 characters.
To update a user if either phone or email is present | localhost:8000/drip/user/ | PUT | <ul><li>email (M)</li><li>phone (M)</li></ul> | Content-Type = 'application/json' | Both email and phone needs to be passed where either of them is already registered. phone should be exactly 10 characters.
To get initial data of all users and reminder_type | localhost:8000/drip/user/ | GET | | Content-Type = 'application/json' | While sending request to /remind api, use reminder_mode id.
To schedule a reminder | localhost:8000/drip/remind/ | POST | <ul><li>user (M)</li><li>scheduled_time (M)</li><li>reminder_type (M)</li><li>msg (M)</li></ul> | Content-Type = 'application/json' | <ul><li>user should be user id</li><li>scheduled_time should be UTC time in format "YYYY-MM-DD hh:mm:ss"</li><li>reminder_type should be a list of reminder_mode id</li><li>msg is a string</li></ul>
**Note:**
* **M** - Mandatory
* **O** - Optional