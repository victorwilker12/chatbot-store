# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPhone(Action):
    def name(self) -> Text:
        return "action_say_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone = tracker.get_slot("phone")
        doctor_name = tracker.latest_message.get('text')
        print(doctor_name)
        dispatcher.utter_message(text=f"Your phone number is {phone}")

        return []
