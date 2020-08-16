from src.kube.constants import pod_jobs, pod_runtime_jobs

metric_labels = {
    pod_runtime_jobs: {
        'aspnetcore_requests_per_second',
        'aspnetcore_requests_duration_seconds_sum',
        'dotnet_gc_collection_reasons_total',
        'dotnet_gc_cpu_ratio',
        'dotnet_gc_pause_ratio',
        'dotnet_threadpool_adjustments_total',
        'dotnet_threadpool_scheduled_total',
        'runtime_lock_contention_total',
        'runtime_threadpool_threads_total',
    },
    pod_jobs: {
        'application_httprequests_errors',
        'application_httprequests_error_rate_total',
        'application_httprequests_transactions_sum',

        'application_qos_violation',  # rate(application_qos_violation[10s])
    },
}