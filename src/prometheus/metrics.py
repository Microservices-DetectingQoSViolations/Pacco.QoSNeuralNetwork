from src.kube.constants import pod_jobs, pod_runtime_jobs
from src.prometheus.metrics_excluder import provide_exclude, provide_exclude_clear

# rate(x[10s]) - rate by 10 seconds range
# sum by (instance) - sum all metric occurences by instance
# {route=~".+"} - excluding

exlude_route = '''route=~".+"'''
only_without_item = '''item!~".+"'''

def add_label_join(query):
    return f'label_join({query}, "instance", "", "app")'

metric_labels = {
    pod_runtime_jobs: [
        ('aspnetcore_requests_per_second_sum', f'label_join(sum by (app, job) (aspnetcore_requests_per_second{provide_exclude_clear()}), "instance", "", "app")'),

        ('aspnetcore_requests_duration_seconds',
         f'label_join(max by (app, job) (rate(aspnetcore_requests_duration_seconds_sum{{{provide_exclude() + exlude_route}}}[10s])), "instance", "", "app")'),

        # 'dotnet_gc_collection_reasons_total', ? not useful

        # ('dotnet_gc_cpu_ratio', f'label_join(sum by (app, job) (rate(dotnet_gc_cpu_ratio{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('dotnet_gc_pause_ratio', f'label_join(sum by (app, job) (rate(dotnet_gc_pause_ratio{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('dotnet_threadpool_adjustments_total', f'label_join(sum by (app, job) (rate(dotnet_threadpool_adjustments_total{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('dotnet_threadpool_scheduled_total', f'label_join(sum by (app, job) (rate(dotnet_threadpool_scheduled_total{provide_exclude_clear()}[5s])), "instance", "", "app")'),

        # ('runtime_lock_contention_total', f'label_join(sum by (app, job) (rate(runtime_lock_contention_total{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('runtime_threadpool_threads_total_sum', f'label_join(sum by (app, job) (runtime_threadpool_threads_total{provide_exclude_clear()}), "instance", "", "app")'),

        # ('runtime_threadpool_threads_total_min', f'label_join(min by (app, job) (runtime_threadpool_threads_total{provide_exclude_clear()}), "instance", "", "app")')

    ],
    pod_jobs: [
        ('application_httprequests_errors', f'label_join(sum by (app, job) (application_httprequests_errors{provide_exclude_clear()}), "instance", "", "app")'),

        ('application_httprequests_error_rate_total', f'label_join(sum by (app, job) (rate(application_httprequests_error_rate_total{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('application_httprequests_transactions_sum', f'label_join(sum by (app, job) (rate(application_httprequests_transactions_sum{provide_exclude_clear()}[10s])), "instance", "", "app")'),

        ('application_httprequests_transactions_max', f'label_join(max by (app, job) (rate(application_httprequests_transactions_sum{provide_exclude_clear()}[10s])), "instance", "", "app")'),


        ('application_qos_violation', f'label_join(sum by (app, job) (increase(application_qos_violation{{{provide_exclude() + only_without_item}}}[10s])), "instance", "", "app")')
    ],
}

dummy_metric_query = "max by (job) (dotnet_build_info)"