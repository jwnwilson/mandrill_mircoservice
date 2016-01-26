# Micro Service project

Building a mini micro service to send e-mails from a fake payment service when an event is received

## To run

source ./setup.sh

python main.py

## Brief

Programming Task
Write a nameko service that sends an email via Mandrill whenever an event is received from another service.

The email sent via Mandrill should be plaintext with the following body:

Dear {payee},

You have received a payment of {amount} {currency} from {client} ({email}).

Yours,
student.com
Below is a service you can use to generate appropriate events while prototyping. Its only dependencies are Faker and nameko. While running it will dispatch an event every 10 seconds.

from faker import Factory

from nameko.events import EventDispatcher
from nameko.timer import timer

fake = Factory.create()


class PaymentService(object):
    name = "payments"

    dispatch = EventDispatcher()

    @timer(interval=10)
    def emit_event(self):

        payload = {
            'client': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payee': {
                'name': fake.name(),
                'email': fake.safe_email()
            },
            'payment': {
                'amount': fake.random_int(),
                'currency': fake.random_element(
                    ("USD", "GBP", "EUR")
                )
            }
        }
        self.dispatch("payment_received", payload)
        
You can create a free and disposable account on Mandrill to integrate your service against.

Your solution should be a single nameko service plus unit and integration tests for it. Take as long as you need to produce something that is as complete and polished as you can.

When you test your service, be sure to apply the eventlet.monkey_patch(). If you choose pytest to run your tests, it will be automatically applied for you.