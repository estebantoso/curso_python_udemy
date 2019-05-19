numbers = (1, 2, 3, 4)

print(type(numbers))

locations = {
    (35.6895, 39.6971): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}

print(locations.keys())

print(locations[(35.6895, 39.6971)])

print(type(locations.items()))