#############*An email service created using FastAPI and Kafka*##################

import asyncio
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from kafka import KafkaConsumer
import json
from config import settings


# FastAPI-Mail configuration
mail_conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS
)

# Initialize FastAPI-Mail
fastmail = FastMail(mail_conf)

###########################################################################
# HTML email template
email_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- <link rel="stylesheet" href="template.css"> -->
    <style>
        body{{
    margin: 0;
    padding: 0;
}}

.header{{
    width: 100%;
    height: 100px;
    background-color: #b3bbbb;
}}
.logo{{
    margin-top: 0;
    padding-top: 20px;
    text-align: center;
}}
.quantum{{
    color:cyan;
    font-size: 45px;
}}
.food{{
    font-size: 45px;
    color: white;
}}
.bg-food{{
    background: url('././ood.jpg');
    height: 350px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 0px;
}}
.bg-food div{{
    padding-top: 50px;
}}
.bg-food h3{{
    margin: 0;
    color: white;
    text-align: center;
    font-family: cursive;
    font-size: 80px;
    font-weight: bolder;
}}
.text-bg{{
    background-color: #69984d;
    padding-bottom: 50px;
}}
.text-bg h5{{
    margin-top: 0;
    text-align: center;
    padding-top: 50px;
    margin-bottom: 30px;
    font-size: 40px;
    color: white;
}}
.text-bg p{{
    text-align: center;
    font-size: 27px;
    color: white;
    margin: 0;
    padding-left: 30px;
    padding-right: 30px;
}}

@media (max-width: 1030px) {{
    .header{{
        height: 150px;
    }}
    .logo{{
        padding-top: 40px;
    }}
    .quantum{{
        font-size: 55px;
    }}
    .food{{
        font-size: 55px;
    }}
    .bg-food{{
        height: 500px;
    }}
    .bg-food div{{
        padding-top: 100px;
    }}
    .bg-food h3{{
        font-size: 100px;
    }}
    .text-bg{{
        padding-bottom: 397px;
        padding-top: 100px;
    }}
    .text-bg h5{{
        font-size: 50px;
    }}
    .text-bg p{{
        font-size: 35px;
        padding-left: 55px;
        padding-right: 55px;
    }}
}}

@media(max-width: 830px){{
    .header{{
        height: 120px;
    }}
    .logo{{
        padding-top: 27px;
    }}
    .text-bg{{
        padding-bottom: 222px;
        padding-top: 80px;
    }}
    .text-bg h5{{
        font-size: 50px;
    }}
}}

@media(max-width: 770px){{
    .bg-food h3{{
        font-size: 90px;
    }}
    .text-bg{{
        padding-bottom: 115px;
        padding-top: 30px;
    }}
    .text-bg h5{{
        font-size: 50px;
    }}
}}

@media(max-width: 545px){{
    .header{{
        height: 85px;
    }}
    .logo{{
        padding-top: 15px;
    }}
    .bg-food{{
        height: 350px;
    }}
    .bg-food div{{
        padding-top: 60px;
    }}
    .bg-food h3{{
        font-size: 65px;
    }}
    .text-bg{{
        padding-bottom: 54px;
    }}
    .text-bg h5{{
        padding-top: 20px;
    }}
    .text-bg p{{
        text-align: center;
        font-size: 27px;
        color: white;
        margin: 0;
        padding-left: 30px;
        padding-right: 30px;
    }}
}}

@media(max-width: 435px){{
    .header{{
        height: 80px;
    }}
    .logo{{
        padding-top: 10px;
    }}
    .quantum{{
        font-size: 45px;
    }}
    .food{{
        font-size: 45px;
    }}
    .bg-food{{
        height: 330px;
    }}
    .bg-food div{{
        padding-top: 60px;
    }}
    .bg-food h3{{
        font-size: 55px;
    }}
    .text-bg{{
        padding-bottom: 250px;
    }}
    .text-bg h5{{
        padding-top: 60px;
        font-size: 35px;
    }}
    .text-bg p{{
        font-size: 25px;
        padding-left: 10px;
        padding-right: 10px;
    }}
}}

@media(max-width: 416px){{
    .text-bg{{
        padding-bottom: 233px;
    }}
}}

@media(max-width: 377px){{
    .text-bg{{
        padding-bottom: 150px;
    }}
}}

@media(max-width: 285px){{
    .header{{
        height: 70px;
    }}
    .logo{{
        padding-top: 10px;
    }}
    .quantum{{
        font-size: 35px;
    }}
    .food{{
        font-size: 35px;
    }}
    .bg-food{{
        height: 290px;
    }}
    .bg-food div{{
        padding-top: 50px;
    }}
    .bg-food h3{{
        font-size: 40px;
    }}
    .text-bg{{
        padding-bottom: 70px;
    }}
    .text-bg h5{{
        padding-top: 10px;
        font-size: 35px;
    }}
    .text-bg p{{
        font-size: 20px;
        padding-left: 8px;
        padding-right: 8px;
    }}
}}
    </style>
</head>
<body>
    <div class="header">
        <h1 class="logo">
            <span class="quantum">Quantum</span><span class="food">Food</span>
        </h1>
    </div>
    <div class="bg-food">
        <div>
            <h3>Thanks for</h3>
            <h3>your order!</h3>   
        </div>
    </div>
    <div class="text-bg">
        <h5>Hello {username}</h5>
        <p>
            Thank you for your recent order. We are pleased to confirm that your order for {food} has been received and 
            it is currently being processed. 
        </p>
    </div>
</body>
</html>
"""
##################################################################################

##################################################################################
#kafka consumer code
topic_name = settings.topic_name
kafka_server = settings.kafka_server

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=kafka_server,
    auto_offset_reset="earliest",
    value_deserializer=bytes
)

print("connected", consumer.bootstrap_connected())
print("Receiving data from ", topic_name)
print(kafka_server)
##################################################################################


##################################################################################
#processing of json file and sending of email
async def process_message(data):
    food = data.get("food")
    username = data.get("username")
    email = data.get("email")

    if food and username and email:
        # Compose and send the email using the template
        subject = f"Your Food Request: {food}"
        body = email_template.format(username=username, food=food)

        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype="html"
        )

        await fastmail.send_message(message)
        print(f"Email sent to {email} for food request: {food}")
    else:
        print("Incomplete data received from Kafka topic")

#conversion of events from binary format to JSON form
async def consume_messages():
    while True:
        for message in consumer:
            try:
                data = json.loads(message.value.decode("utf-8"))
                await process_message(data)
            except Exception as e:
                print(f"Error processing Kafka message: {e}")

# Run the asynchronous consumer
loop = asyncio.get_event_loop()
loop.create_task(consume_messages())
loop.run_forever()
