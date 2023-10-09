import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'XXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)
a=("b+ donor required" )*5
call = client.calls.create(
                        twiml='<Response><Say voice="male" language="te"> %s </Say></Response>'%(a),
                        to='+91XXXXXXXXX6',
                        from_='+1XXXXXXX19'
                    )

  

