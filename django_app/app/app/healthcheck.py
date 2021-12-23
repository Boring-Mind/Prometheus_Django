from django.http import HttpResponse
from django_prometheus.exports import ExportToDjangoView
from health_check.mixins import CheckMixin


class HealthCheck(CheckMixin):
    """Perform django-health-check in a neat way.

    This class is needed only to call healthcheck function from django-health-check
    package in a neat way.
    """

    def healthy(self) -> bool:
        return not bool(self.errors)


def django_prometheus_with_healthcheck_view(request) -> HttpResponse:
    """Modified django_prometheus /metrics view that contains Django health metric."""
    response = ExportToDjangoView(request)
    response.write(
        "# HELP django_health Django health"
        "\n# TYPE django_health gauge"
        f"\ndjango_health {int(HealthCheck().healthy())}"
    )
    return response
