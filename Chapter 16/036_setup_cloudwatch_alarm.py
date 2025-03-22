# Script: 036_setup_cloudwatch_alarm.py

import boto3

def setup_cloudwatch_alarm(alarm_name, metric_name, namespace, threshold, evaluation_periods):
    cloudwatch = boto3.client('cloudwatch')
    try:
        response = cloudwatch.put_metric_alarm(
            AlarmName=alarm_name,
            MetricName=metric_name,
            Namespace=namespace,
            Statistic='Average',
            Period=60,
            EvaluationPeriods=evaluation_periods,
            Threshold=threshold,
            ComparisonOperator='GreaterThanThreshold',
            AlarmActions=['arn:aws:sns:your-sns-topic-arn']
        )
        print(f"Alarm {alarm_name} created successfully.")
    except Exception as e:
        print(f"Error setting up alarm: {e}")

if __name__ == "__main__":
    setup_cloudwatch_alarm(
        alarm_name="HighCPUUsage",
        metric_name="CPUUtilization",
        namespace="AWS/EC2",
        threshold=80,
        evaluation_periods=2
    )
