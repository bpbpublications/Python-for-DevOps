# Script: 012_triage_incident.py

def triage_incident(incident):
    """
    Triage an incident by determining its priority based on its type.
    """
    incident_type = incident.get("type")  # Get the type of the incident
    priority = incident_priorities.get(incident_type, "medium")  # Determine the priority (default to "medium")
    return {"priority": priority, **incident}  # Return the incident with its priority
