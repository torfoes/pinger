from celery import shared_task
from .models import Domain
import requests

@shared_task
def ping_domains():
    print('Pinging domains...')
    domains = Domain.objects.filter(is_active=True)
    for domain in domains:
        response = requests.get(domain.url)
        print(f'Ping {domain.url}: {response.status_code}')
