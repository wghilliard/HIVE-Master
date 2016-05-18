# __author__ = 'W. Grayson Hilliard'
import time
from config import CONT_COUNT
from app import db
from app.master import add
import datetime


class Batch(db.Document):
    batch_id = db.IntField(required=True)
    job_id = db.IntField(required=True)
    events = db.IntField()
    out_path = db.StringField()
    log_path = db.StringField()
    err_path = db.StringField()
    status = db.StringField()
    complete = db.BooleanField(default=False)
    error = db.StringField()
    start_time = db.DateTimeField()
    end_time = db.DateTimeField()

    def __str__(self):
        return str(self.batch_id)


class Worker(db.Document):
    worker_id = db.StringField()
    hostname = db.StringField()


class Job(db.Document):
    job_id = db.IntField(required=True, unique=True)
    events = db.IntField(required=True)
    name = db.StringField(required=True, default='electron')
    out_dir = db.StringField(default='electron/')
    log_dir = db.StringField()
    batches = db.ListField(db.ReferenceField('Batch'))
    new_file = db.StringField()
    started = db.BooleanField(default=False)
    complete = db.BooleanField(default=False)
    start_time = db.DateTimeField()
    notes = db.StringField()

    def check_complete(self):
        if self.started:
            for batch in self.batches:
                if batch.complete is not True:
                    self.complete = False
            self.complete = True
        else:
            self.complete = False

        self.save()

    def get(self):
        return {"job_id": self.job_id,
                "events": self.events,
                "name": self.name,
                "out_dir": self.out_dir,
                "log_dir": self.log_dir,
                "batches": [batch.batch_id for batch in self.batches],
                "new_file": self.new_file,
                "started": self.started,
                "complete": self.complete,
                "start_time": str(self.start_time)}

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, **kwargs):
        if not self.job_id:
            self.job_id = int(time.time())
        return super(Job, self).save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs,
                                     save_condition, **kwargs)

    def start(self):
        events_per_cont = int(self.events) / int(CONT_COUNT)
        self.start_time = datetime.datetime.now()
        for x in range(0, int(CONT_COUNT)):
            batch = Batch(job_id=self.job_id, batch_id=int(x), events=events_per_cont).save()
            self.batches.append(batch)

            data = self.to_mongo().to_dict()
            data['batch_id'] = int(x)
            data['events'] = str(events_per_cont)

            del (data['start_time'])
            del (data['_id'])
            del (data['batches'])

            add(data)

            self.started = True
            self.save()
