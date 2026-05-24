import os
import yaml

# Paths
rtl_dir = 'rtl'
yaml_file = '.github/workflows/update_issue_template.yml'

# Get list of files in the rtl directory
rtl_files = [f for f in os.listdir(rtl_dir) if os.path.isfile(os.path.join(rtl_dir, f))]

if not rtl_files:
    rtl_files = ["No files found"]

# Load the existing YAML
with open(yaml_file, 'r') as file:
    data = yaml.safe_load(file)

# Find the dropdown and update options
for item in data.get('body', []):
    if item.get('id') == 'module' and item.get('type') == 'dropdown':
        item['attributes']['options'] = rtl_files
        # Ensure multi-select is enabled as you requested
        item['attributes']['multiple'] = True 

# Write the updated YAML back
with open(yaml_file, 'w') as file:
    yaml.dump(data, file, sort_keys=False, default_flow_style=False)
