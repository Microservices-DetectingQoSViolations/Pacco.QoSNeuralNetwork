def exclude_metrics_by_service_name(excluding_services, only_excluder):
    if len(excluding_services) == 0:
        return ''

    excluding_services_query = f'''app!~"{'|'.join(excluding_services)}"'''

    if only_excluder:
        return "{" + excluding_services_query + "}"
    else:
        return excluding_services_query + ", "
