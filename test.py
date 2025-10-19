column_names = ['id', 'color', 'style']
column_values = [1, 'red', 'bold']

# Convert lists to a dictionary
name_to_value_dict = dict(zip(column_names, column_values))

print(name_to_value_dict)
# Output: {'id': 1, 'color': 'red', 'style': 'bold'}
