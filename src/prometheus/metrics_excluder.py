from src.prometheus.constants import excluding_services

def exclude_metrics_by_service_name(excluding_services, only_excluder):
    if len(excluding_services) == 0:
        return ''

    excluding_services_query = f'''app!~"{'|'.join(excluding_services)}"'''

    if only_excluder:
        return "{" + excluding_services_query + "}"
    else:
        return excluding_services_query + ", "

def provide_exclude_clear():
    return exclude_metrics_by_service_name(excluding_services, True)

def provide_exclude():
    return exclude_metrics_by_service_name(excluding_services, False)
