invited = {"Alice", "Bob", "Charlie"}
arrived = {"Alice", "Charlie", "Diana"}
unexpected_guests = arrived - invited
if unexpected_guests:
    print("Unexpected guests:", unexpected_guests)