# Open the GeoJSON file
with open('Hampton_Roads_MSA.geojson', 'r') as file:
    # Read the content of the file
    content = file.read()

# Remove any square brackets and split the content into coordinate pairs
coordinate_pairs = content.replace('[', '').replace(']', '').split(', ')

# Format coordinates
formatted_coordinates = ''
for i in range(0, len(coordinate_pairs), 2):
    formatted_coordinates += f"{coordinate_pairs[i]}, {coordinate_pairs[i + 1]}\n"

# Write formatted coordinates to a new file
with open('formatted_coordinates.txt', 'w') as file:
    file.write(formatted_coordinates)

print("Coordinates formatted and saved to 'formatted_coordinates.txt'.")
