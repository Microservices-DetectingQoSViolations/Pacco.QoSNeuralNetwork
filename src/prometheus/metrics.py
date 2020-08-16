from src.kube.constants import pod_jobs, pod_runtime_jobs

# rate(x[10s]) - rate by 10 seconds range
# sum by (instance) - sum all metric occurences by instance
# {route=~".+"} - excluding

metric_labels = {
    pod_runtime_jobs: {
        ('aspnetcore_requests_per_second', 'aspnetcore_requests_per_second'),  # simple pass metric

        ('aspnetcore_requests_duration_seconds_sum',
         'sum by (instance) (rate(aspnetcore_requests_duration_seconds_sum{route=~".+"}[10s]))'),

        # 'dotnet_gc_collection_reasons_total', ? not useful

        ('dotnet_gc_cpu_ratio', 'rate(dotnet_gc_cpu_ratio[10s])'),

        ('dotnet_gc_pause_ratio', 'rate(dotnet_gc_pause_ratio[10s])'),

        ('dotnet_threadpool_adjustments_total', 'rate(dotnet_threadpool_adjustments_total[10s])'),

        ('dotnet_threadpool_scheduled_total', 'rate(dotnet_threadpool_scheduled_total[5s])'),

        ('runtime_lock_contention_total', 'rate(runtime_lock_contention_total[10s])'),

        ('runtime_threadpool_threads_total', 'runtime_threadpool_threads_total')
    },
    pod_jobs: {
        ('application_httprequests_errors', 'application_httprequests_errors'),
        ('application_httprequests_error_rate_total', 'rate(application_httprequests_error_rate_total[10s])'),
        ('application_httprequests_transactions_sum', 'rate(application_httprequests_transactions_sum[10s])'),

        ('application_qos_violation', 'rate(application_qos_violation[10s])') # rate by 10 seconds range
    },
}