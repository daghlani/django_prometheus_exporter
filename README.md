# django_prometheus_exporter


## Sources:

## To create custome metrics

> [client_python](https://github.com/prometheus/client_python)


## To create exporter

> [django-prometheus](https://github.com/korfuri/django-prometheus)


# Routes:

## The page of created exporter

```bash
http://<your ip>:<your port>/prom/metrics
```


## The sample page of a counter metric

```bash
http://<your ip>:<your port>/counter
```

> when you browse this page, a metric with the name `my_failures_total` will be counted and increased with any request.
