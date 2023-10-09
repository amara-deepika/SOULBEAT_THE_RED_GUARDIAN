import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACfb7f22460b6f2b5bd537927c6b75ad90'
auth_token = '2f6b2ae403c13b1721c9e220104ff3a9'
client = Client(account_sid, auth_token)
a=("jagratha "+"dog"+" vastundi" )*5
call = client.calls.create(
                        twiml='<Response><Say voice="male" language="te"> %s </Say></Response>'%(a),
                        to='+918072485316',
                        from_='+13082108219'
                    )

  

