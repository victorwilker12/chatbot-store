from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import Restarted, FollowupAction, ActionExecuted, SessionStarted, SlotSet


class ActionCategories(Action):
    def name(self) -> Text:
        return "action_categories_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        set_buttons = []
        response = requests.get("https://fakestoreapi.com/products/categories")
        print('call cc')
        if response.status_code == 200:
            msg = response.json()
            for value in msg:
                set_buttons.append({"title": value, "payload": value})
            dispatcher.utter_message(text="Categories", buttons=set_buttons)
            current_intent = tracker.latest_message['text']
            if current_intent in msg:
                return [FollowupAction('action_get_product'), SlotSet('category', current_intent)]
        else:
            dispatcher.utter_message(text="categories not found")
        #
