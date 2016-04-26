# __author__ = 'W. Grayson Hilliard'
import time
from config import CONT_COUNT
from app import db
from app.master import add


class Batch(db.Document):
    batch_id = db.IntField(required=True)
    job_id = db.IntField(required=True)
    out_path = db.StringField()
    log_path = db.StringField()
    status = db.StringField()
    complete = db.BooleanField(default=False)

    def __str__(self):
        return str(self.batch_id)


class Job(db.Document):
    job_id = db.IntField(required=True, default=int(time.time()))
    events = db.IntField(required=True)
    name = db.StringField(required=True, default='electron')
    out_dir = db.StringField(default='electron/')
    log_dir = db.StringField()
    batches = db.ListField(db.ReferenceField('Batch'))
    new_file = db.StringField()
    started = db.BooleanField(default=False)
    complete = db.BooleanField(default=False)
    # start_time = db.DateTimeField()

    def start(self):
        events_per_cont = int(self.events) / int(CONT_COUNT)

        for x in range(0, int(CONT_COUNT)):

            batch = Batch(job_id=self.job_id, batch_id=int(x)).save()
            self.batches.append(batch)

            data = self.to_mongo().to_dict()
            data['batch_id'] = int(x)
            data['events'] = str(events_per_cont)
            del(data['_id'])
            del(data['batches'])

            add(data)

            self.started = True
            self.save()
