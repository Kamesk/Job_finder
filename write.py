import re

def extract_info(details):
    extracted_infos = []
    for content in details:
        info = {}
        # Extract pay range using regex
        pay_range_match = re.search(r'£(\d+(?:,\d+)*)/yr - £(\d+(?:,\d+)*)/yr', content)
        if pay_range_match:
            pay_range_start = pay_range_match.group(1)
        else:
            pay_range_start = pay_range_end = None
        info['Pay'] = pay_range_start

        # Extract workplace using regex
        workplace_match = re.search(r'(?:remote|not)', content, re.IGNORECASE)
        workplace = 'Remote' if workplace_match and 'remote' in workplace_match.group(0).lower() else 'Not Remote'
        info['Workplace'] = workplace

        # Extract job level using regex
        level_match = re.search(r'(Junior|Mid|Mid-Senior|Senior|Executive) level', content)
        level = level_match.group(1) if level_match else None
        info['Level'] = level

        # Extract employee numbers using regex
        employee_numbers_match = re.search(r'(\d+)-(\d+) employees', content)
        employee_numbers_start = employee_numbers_match.group(1) if employee_numbers_match else None
        employee_numbers_end = employee_numbers_match.group(2) if employee_numbers_match else None
        info['Employee Numbers'] = employee_numbers_start

        # Extract skill match using regex
        skill_match_match = re.search(r'(\d+) of (\d+) skills match your profile - you may be a good fit', content)
        skill_match = f"{skill_match_match.group(1)} out of {skill_match_match.group(2)}" if skill_match_match else None
        info['Skill Match'] = skill_match

        # Append the current info dictionary to extracted_infos list
        extracted_infos.append(info)

    return extracted_infos
    


