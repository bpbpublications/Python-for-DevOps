# Script: 004_opentelemetry_jaeger_integration.py

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Configure Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Hostname of the Jaeger agent
    agent_port=6831,             # Port of the Jaeger agent
)

# Create a batch span processor and configure it with the Jaeger exporter
span_processor = BatchExportSpanProcessor(jaeger_exporter)

# Create a tracer provider and register the batch span processor
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(span_processor)

# Register the tracer provider with OpenTelemetry
trace.set_tracer_provider(tracer_provider)
