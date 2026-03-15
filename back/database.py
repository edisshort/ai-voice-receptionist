appointments = []

def add_appointment(name, service, time):
    appointment = {
        "name": name,
        "service": service,
        "time": time
    }
    appointments.append(appointment)
    return appointment


def get_appointments():
    return appointments