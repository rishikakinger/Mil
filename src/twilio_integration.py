from twilio.rest import Client

def send_alert(message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='abc',  
        to='xyz'      
    )

    print(f"Alert sent: {message.sid}")