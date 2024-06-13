import json
import requests
import numpy as np

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetProduct(Action):
    def name(self) -> Text:
        return "action_get_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('call')
        # set_categories = tracker.get_slot('category')
        set_categories = tracker.latest_message['text']
        response = requests.get(f'https://fakestoreapi.com/products/category/{set_categories}')
        if response.status_code == 200:
            list_products = []
            json_read = json.dumps(response.json())
            json_read = json.loads(json_read)
            for i in range(len(json_read)):
                result = json_read[i].items()
                data = list(result)
                list_products.append(np.array(data))
            print(list_products)
            dispatcher.utter_message(text=f"{list_products}")
        else:
            dispatcher.utter_message(text="Products not found")
            return []
