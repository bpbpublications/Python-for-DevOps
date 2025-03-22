# Script: 006_jaeger_exporter_with_opentelemetry.py

import time
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Configure Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Hostname of the Jaeger agent
    agent_port=6831              # Port of the Jaeger agent
)

# Create a batch span processor and configure it with the Jaeger exporter
span_processor = BatchExportSpanProcessor(jaeger_exporter)

# Create a tracer provider and register the batch span processor
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(span_processor)

# Register the tracer provider with OpenTelemetry
from opentelemetry import trace
trace.set_tracer_provider(tracer_provider)

# Sleep to allow time for spans to be exported
time.sleep(5)  # Sleep for 5 seconds to ensure spans are sent to Jaeger
