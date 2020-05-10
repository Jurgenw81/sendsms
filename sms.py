from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Account SID"
# Your Auth Token from twilio.com/console
auth_token  = "AUTH Token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="Your Number", 
    from_="FromYourNumber",
    body="Hello from Python!")

print(message.sid)
