"""
    ::Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    ::Date: 25/01/2016

    Simple Email dispatcher service that integrates with mandrill
"""
import os
import logging
from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc
import mandrill

logger = logging.getLogger(__name__)

class EmailService(object):
    name = "emails"

    @event_handler("payments", "payment_received")
    def send_email(self, payload):
        """
        Send e-mails using payload data when triggered from the payment service
        :param payload: dict sender, recipient and message data
        :return: None
        """
        api_key = os.getenv("MANDRILL_API_KEY")
        if api_key is None:
            logger.error("No API key set unable to send e-mail for payload: %s" % str(payload))
            return

        mandrill_client = mandrill.Mandrill(api_key)

        message = {
            "from_email":"noreply@noel-wilson.co.uk",
            "to":[{"email":"jwnwilson@hotmail.co.uk"}],
            "subject": "Test Email",
            "text": "Test text message."
        }

        try:
            mandrill_client.messages.send(message=message,
                                          async=False,
                                          ip_pool='Main Pool')
        except mandrill.Error, e:
            logger.error("Unable to send e-mail through mandrill for payload: %s" % str(payload), exc_info=True)
            return

        logger.info("Successfully send e-mail for payload: %s" % str(payload))
