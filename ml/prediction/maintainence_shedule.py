def maintance_shedule(health_score,failure_probability):
    if health_score < 40 or failure_probability >= 75:
        return "Immediate Maintenance"

    elif health_score < 60 or failure_probability >= 50:
        return "Maintenance Within 7 Days"

    elif health_score < 80 or failure_probability >= 20:
        return "Schedule Maintenance"

    else:
        return "Routine Maintenance"



health = 59.29
failure_probability = 72

schedule = maintance_shedule(
    health,
    failure_probability
)

print("Maintenance:", schedule)