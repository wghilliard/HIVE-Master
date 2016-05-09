import json
import pika
from pika.exceptions import ConnectionClosed


def add(data_dict):
    try:
        # master - worker dispatch via rabbitmq
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='dispatch')
        # data_dict = {"new_file": "fcl_files/MC_geant4_electron.fcl",
        #              "events": "10",
        #              "name": "test_name",
        #              "job_id": "12345412",
        #              "batch_id": "1",
        #              "out_dir": "test_name",
        #              "log_dir": "12345_0"}

        encoded_body = json.dumps(data_dict)
        channel.basic_publish(exchange='',
                              routing_key='dispatch',
                              body=encoded_body)
        connection.close()
    except ConnectionClosed as e:
        print e
        add(data_dict)

    except Exception as e:
        print(e)
        return
