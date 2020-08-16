from typing import Text, List, Dict, Any, Union
import time
from ruamel import yaml

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted


class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
                "job_function",
                "use_case",
                "budget",
                "person_name",
                "company",
                "business_email",
            ]

    def submit(
                self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any],
            ) -> List[Dict]:
        print(f"Result Slot Values: {tracker.current_slot_values()}")
        dispatcher.utter_message(
        "Thanks for getting in touch, we’ll contact you soon")
        with open(f'saves/saved_data{time.time()}.yml', 'w+') as save_file:
            yaml.dump(tracker.current_slot_values())
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {"use_case": self.from_text(intent="inform")}
