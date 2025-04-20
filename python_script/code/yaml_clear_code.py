import yaml

# Load the YAML file
print("program start")
with open("input.yaml", "r") as file:
    data = yaml.safe_load(file)

# Sort the 'variables' list by the 'name' field
data["variables"] = sorted(data["variables"], key=lambda x: x["name"])

# Save the sorted YAML to a new file
with open("sorted.yaml", "w") as file:
    yaml.dump(data, file, sort_keys=False)

