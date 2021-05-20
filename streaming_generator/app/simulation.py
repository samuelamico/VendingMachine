import json
import time
import random


def output_function(event, output: str, kafka_producer):
    if(output == 'local'):
        print(event)

    elif(output == 'kafka'):
        kafka_producer.send('machine-topic', event)


def machine_simulation(machine, sensor_machine, kafka_producer, output: str = 'local'):
    print(f"Turn ON the Machine = {machine.id} , {machine()} \n")
    print(machine)
    while not machine.stopped_flag:
        # If Machine ON and not refilled generate output
        while not machine.refil_flag:
            product = machine.get_product()
            event_json = json.loads(sensor_machine.sensor_event())

            # Send event to output:
            output_function(event_json, output, kafka_producer)

            # Check if the machine stopped or is refiled
            if(machine.stopped_flag or machine.refil_flag):
                break

            # Random time between each event generator
            time.sleep(random.randint(5,10))
        

    print(f"Turn OFF the Machine = {machine.id}")
    return 