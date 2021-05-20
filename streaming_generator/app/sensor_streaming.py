from app.vending_machine import Machine
from datetime import datetime
import json
import random
import time
random.seed()



class SensorStreaming:

    def __init__(self, machine: Machine) -> None:
        self._machine = machine

    def _properties_iot(self):
        content_properties = {
            "timestamp": str(datetime.today()),
            "machine_id": self._machine.id,
            "city": self._machine.city,
            "state": self._machine.state,
            "country": self._machine.country,
            "capacity": self._machine._capacity
        }
        content_properties.update(self._machine())
        return content_properties

    def sensor_event(self):
        event_json = {
            "type": "Feature",
            "geometry": self._machine.location,
            "properties": self._properties_iot()
        }
        return json.dumps(event_json)




