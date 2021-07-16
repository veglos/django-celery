import json
from celery.result import AsyncResult
from django.http import JsonResponse
from myapp.tasks import sample_task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def simple_task(request):
    if request.method == "POST":        
        body = json.loads(request.body)
        task = sample_task.delay(body['message'])
        return JsonResponse({"task_id": task.id}, status=202)

@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)