import warnings
import pandas as pd
from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from app.vending_machine import Machine
from app.products import Drinks
from app.sensor_streaming import SensorStreaming
from app.simulation import machine_simulation
from models import Refilled
from app import simulation 
from kafka import KafkaProducer
import json

warnings.filterwarnings('ignore')

app = FastAPI()
global vending_machine
global stopped_machine


vending_machine = {}
stopped_machine = {}
kafka_config = {}

# Load --- 
# TODO: Adding the Kafka



@app.on_event("startup")
async def create_machine():
    # Load the machine
    vending_machine['machine'] = Machine(Drinks)
    vending_machine['machine'].stopped_flag = False
    vending_machine['sensor'] = SensorStreaming(vending_machine['machine'])
    stopped_machine['flag'] = False
   
    kafka_config['producer'] = KafkaProducer(bootstrap_servers=['kafka:29092'],api_version=(0,11,5),
                            value_serializer=lambda v: str(v).encode('utf-8'))

@app.get("/")
async def root() -> str:
    return "Vending Machine"


@app.get("/stop")
async def stop_machine() -> str:
    vending_machine['machine'].stopped_flag = True
    return "Stopping the Vending Machine"

@app.post("/refil")
async def refil_machine(products: Refilled) -> str:
    vm = vending_machine['machine']
    vm.refil(products.Products)
    return f"Machine {vm.id} Refiled = {vm()}"

@app.get("/start")
async def predict(background_tasks: BackgroundTasks):
    vending_machine['machine'].stopped_flag = False
    background_tasks.add_task(simulation.machine_simulation, vending_machine['machine'], vending_machine['sensor'], kafka_producer=kafka_config['producer'], output='kafka')
    return {"message": "Machine Simulation sent in the background"}
