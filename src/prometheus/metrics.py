from src.kube.constants import pod_jobs, pod_runtime_jobs
from src.prometheus.metrics_excluder import provide_exclude, provide_exclude_clear

# rate(x[10s]) - rate by 10 seconds range
# sum by (instance) - sum all metric occurences by instance
# {route=~".+"} - excluding

exlude_route = '''route=~".+"'''
only_without_item = '''item!~".+"'''

metric_labels = {
    pod_runtime_jobs: [
        ('aspnetcore_requests_per_second_sum', f'sum by (app) (aspnetcore_requests_per_second{provide_exclude_clear()})'),

        ('aspnetcore_requests_per_second_avg', f'avg by (app) (aspnetcore_requests_per_second{provide_exclude_clear()})'),

        ('aspnetcore_requests_duration_seconds',
         f'max by (app) (rate(aspnetcore_requests_duration_seconds_sum{{{provide_exclude() + exlude_route}}}[10s]))'),

        # 'dotnet_gc_collection_reasons_total', ? not useful

        ('dotnet_gc_cpu_ratio', f'sum by (app) (rate(dotnet_gc_cpu_ratio{provide_exclude_clear()}[10s]))'),

        ('dotnet_gc_pause_ratio', f'sum by (app) (rate(dotnet_gc_pause_ratio{provide_exclude_clear()}[10s]))'),

        ('dotnet_threadpool_adjustments_total', f'sum by (app) (rate(dotnet_threadpool_adjustments_total{provide_exclude_clear()}[10s]))'),

        ('dotnet_threadpool_scheduled_total', f'sum by (app) (rate(dotnet_threadpool_scheduled_total{provide_exclude_clear()}[5s]))'),

        ('runtime_lock_contention_total', f'sum by (app) (rate(runtime_lock_contention_total{provide_exclude_clear()}[10s]))'),

        ('runtime_threadpool_threads_total_sum', f'sum by (app) (runtime_threadpool_threads_total{provide_exclude_clear()})'),

        ('runtime_threadpool_threads_total_min', f'min by (app) (runtime_threadpool_threads_total{provide_exclude_clear()})')

    ],
    pod_jobs: [
        ('application_httprequests_errors', f'sum by (app) (application_httprequests_errors{provide_exclude_clear()})'),

        ('application_httprequests_error_rate_total', f'sum by (app) (rate(application_httprequests_error_rate_total{provide_exclude_clear()}[10s]))'),

        ('application_httprequests_transactions_sum', f'sum by (app) (rate(application_httprequests_transactions_sum{provide_exclude_clear()}[10s]))'),

        ('application_httprequests_transactions_max', f'max by (app) (rate(application_httprequests_transactions_sum{provide_exclude_clear()}[10s]))'),


        ('application_qos_violation', f'sum by (app) (increase(application_qos_violation{{{provide_exclude() + only_without_item}}}[10s]))')
    ],
}