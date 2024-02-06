import json

# Open and load the JSON file
with open('/Users/lvning/Desktop/sde.json', 'r') as f:
    data = json.load(f)

# Initialize an empty list to store the "Action" items
actions = []

# Iterate over each statement in the JSON data
for statement in data['Statement']:
    action = statement['Action']
    # Check if the action is a list
    if isinstance(action, list):
        # If it's a list, extend the actions list
        actions.extend(action)
    else:
        # If it's not a list, append the action to the list
        actions.append(action)

# Remove duplicates by converting the list to a set, then convert it back to a list
actions = list(set(actions))
# Sort the actions list
actions.sort()
# Print the list of "Action" items
print(actions)

with open('iam_output.txt', 'w') as f:
    for action in actions:
        # Write each action to the file
        f.write(f'{action}\n')

print("Actions have been written to 'iam_output.txt'")
