from app import app
from app.models import Job, Batch
from flask import request, jsonify
import json


@app.route('/api/jobs', methods=['GET', 'POST'])
def list_jobs():
    if request.method == 'POST':



        # print(request.data)
        # print(type(request.data))
        data_dict = json.loads(request.data)
        # print(data_dict)
        # print(type(data_dict))
        job_object = Job(events=data_dict.get('events'), name=data_dict.get('name'),
                         out_dir=data_dict.get('out_dir'), log_dir=data_dict.get('log_dir'),
                         new_file=data_dict.get('new_file'))

        job_object.save()

        if data_dict.get('start') is True:
            job_object.start()
            started = True
        else:
            started = False

        return jsonify({'job_id': str(job_object.job_id),
                        'started': started})

    else:
        # Needs testing, potentially bad practice.
        # print([job.get() for job in Job.objects()])
        return jsonify({"jobs": [job.get() for job in Job.objects()]})
