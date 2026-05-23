# tracing.py

from openinference.instrumentation.langchain import LangChainInstrumentor

from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.resources import Resource

from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)

_is_instrumented = False


def setup_tracing(
    project_name: str = "default-project",
    service_name: str = "default-service",
):

    global _is_instrumented

    provider = TracerProvider(
        resource=Resource.create(
            {
                # Phoenix Project Name
                "openinference.project.name": project_name,

                # OTEL Service Name
                "service.name": service_name,
            }
        )
    )

    trace.set_tracer_provider(provider)

    provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint="http://127.0.0.1:6006/v1/traces"
            )
        )
    )

    if not _is_instrumented:

        LangChainInstrumentor().instrument()

        _is_instrumented = True