import re
import pandas as pd

# List to store extracted information from each content block
extracted_info = []

# Provided contents (assuming it's a list of strings)
contents = [
    """
    Harnham
    
    £80,000/yr - £90,000/yr
    Hybrid
    Matches your job preferences, workplace type is Hybrid.
    Full-time
    Matches your job preferences, job type is Full-time.
    Mid-Senior level
    201-500 employees · Staffing and Recruiting
    1 connection works here
    ·
    3 company alumni work here
    ·
    1 school alum works here
    4 of 4 skills match your profile - you may be a good fit
    """,
    # Add more content blocks here if needed
]

# Iterate through each content block
for content in contents:
    # Initialize dictionary to store extracted information
    info = {}

    # Extract pay range using regex
    pay_range_match = re.search(r'£(\d+(?:,\d+)*)/yr - £(\d+(?:,\d+)*)/yr', content)
    if pay_range_match:
        pay_range_start = pay_range_match.group(1)
        pay_range_end = pay_range_match.group(2)
    else:
        pay_range_start = pay_range_end = None
    info['Pay Range Start'] = pay_range_start
    info['Pay Range End'] = pay_range_end

    # Extract workplace using regex
    workplace_match = re.search(r'workplace type is (\w+)', content)
    workplace = workplace_match.group(1) if workplace_match else None
    info['Workplace'] = workplace

    # Extract employee numbers using regex
    employee_numbers_match = re.search(r'(\d+)-(\d+) employees', content)
    employee_numbers_start = employee_numbers_match.group(1) if employee_numbers_match else None
    employee_numbers_end = employee_numbers_match.group(2) if employee_numbers_match else None
    info['Employee Numbers Start'] = employee_numbers_start
    info['Employee Numbers End'] = employee_numbers_end

    # Extract skill match using regex
    skill_match_match = re.search(r'(\d+) of (\d+) skills match your profile - you may be a good fit', content)
    skill_match = f"{skill_match_match.group(1)} out of {skill_match_match.group(2)}" if skill_match_match else None
    info['Skill Match'] = skill_match

    # Append extracted information to the list
    extracted_info.append(info)

# # Create DataFrame from the list
# df = pd.DataFrame(extracted_info)

# # Write DataFrame to Excel
# df.to_excel('extracted_info.xlsx', index=False)

