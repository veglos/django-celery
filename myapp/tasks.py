from celery import shared_task

@shared_task
def sample_task(message):
    print("The sample task just ran with message: " + message)
    return True

@shared_task
def sample_beat_task():
    print("The sample beat task just ran")