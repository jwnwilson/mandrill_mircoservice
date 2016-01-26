"""
    ::Author: Matt

    Code provided for this exercise to create a periodic event with test data
"""
from faker import Factory

from nameko.rpc import rpc
from nameko.events import EventDispatcher
from nameko.timer import timer

fake = Factory.create()


class PaymentService(object):
    """
    Payment micro service to launch events to the email sender
    """
    name = "payments"

    dispatch = EventDispatcher()

    @timer(interval=10)
    @rpc
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