from flask_admin.contrib.mongoengine import ModelView
from flask_admin.actions import action
from app import admin, app
from app.models import Job, Batch


@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


class JobView(ModelView):
    # form_columns = ('job_id', 'name', 'events', 'new_file')
    form_excluded_columns = ['status', 'complete', 'batches', 'started']
    form_ajax_refs = {
        'batches': {
            'fields': ['batch_id']
        }
    }
    # column_searchable_list = ['job_id']
    can_export = True

    @action('start', 'Start', 'Are you sure you want to start?')
    def action_start(self, ids):
        for id in ids:
            job = Job.objects.get(pk=id)
            if not job.started:
                job.start()


admin.add_view(JobView(Job, name='Jobs'))
admin.add_view(ModelView(Batch, name='Batches'))
