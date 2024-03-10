import re

details = """['On-site', 'Matches your job preferences, workplace type is On-site.', 'Full-time', 'Matches your job preferences, job type is Full-time.', 'Mid-Senior level', '10,001+ employees · Food and Beverage Manufacturing', '12 company alumni work here', '·', '6 school alumni work here', 'Skills: MLOps, Communication, +8 more', 'View verifications related to this job post.', 'View verifications related to this job post.', 'Show all', 'See how you compare to 7 applicants.', 'Reactivate Premium', 'Company Description', 'Louis Dreyfus Company is a leading merchant and processor of agricultural goods. Our activities span the entire value chain from farm to fork, across a broad range of business lines, we leverage our global reach and extensive asset network to serve our customers and consumers around the world. Structured as a matrix organization of six geographical regions and ten platforms, Louis Dreyfus Company is active in over 100 countries and employs approximately 17,000 people globally.', 'Job Description', 'LDC is on the lookout for a Quantitative Strategist to enhance our Global Data Science team. In this multifaceted role, you will first play a key part in improving our systematic trading infrastructure. And as the project evolves you will be more and more at the forefront of developing innovative trading strategies. You will collaborate with systematic trading and IT teams, applying your expertise to systematically implement and peer-review trading strategies, as well as driving technological advancements across the company.', 'Main responsibilities:', 'Spearhead the enhancement of our framework, introducing new features and capabilities to meet the users’ requirements.', 'Lead the resolution of complex technical challenges independently or by orchestrating team members’ tasks.', 'Design and execute advanced quantitative models for market analysis, risk management, and implement proven trading strategies.', 'Facilitate the integration of these strategies into our trading platforms, working alongside systematic and proprietary trading teams.', 'Oversea the peer-review process of the strategies presented by systematic traders.', 'Maintain a leading edge in systematic trading to integrate advanced trading strategies.', 'Collaborate with IT and Data Science teams to facilitate platform improvements and increase adoption.', 'Responsible of DevOps/MLOps best practices, including code/data versioning, and rigorous testing protocols.', 'Clearly communicate complex quantitative concepts and strategies to a diverse range of stakeholders.', 'Experience', 'MSc or PhD in a quantitative field such as Mathematics, Statistics, Financial Engineering, Econometrics, Computer Science, or similar.', '7+ years of experience in quantitative research in a commodity trading firm, Hedge Fund, or bank.', 'Skilled in Python (backend in object-oriented – and frontend being a plus).', 'Experience with DevOps and MLOps.', 'Exceptional analytical and statistical capabilities, with a proven track record in problem-solving.', 'Experience with implementing machine learning trading models in finance.', 'Excellent communication skills for effectively conveying complex concepts.', 'Passionate about financial markets and systematic trading.', 'Ability to work independently and in collaborative settings, with proven leadership skills.', 'Experience in agricultural commodities trading is a strong plus.', 'Additional Information', 'Additional Information for the job', 'Diversity & Inclusion', 'LDC is driven by a set of shared values and high ethical standards, with diversity and inclusion being part of our DNA. LDC is an equal opportunity employer committed to providing a working environment that embraces and values diversity, equity and inclusion.', 'LDC encourages diversity, supports local communities and environmental initiatives. We encourage people of all backgrounds to apply.', 'Sustainability', 'Sustainable value is at the heart of our purpose as a company.', 'We are passionate about creating fair and sustainable value, both for our business and for other value chain stakeholders: our people, our business partners, the communities we touch and the environment around us', '"What We Offer', 'We provide a dynamic and stimulating international environment, which will stretch and develop your abilities and channel your skills and expertise with outstanding career development opportunities in one of the largest and most solid private companies in the world.', 'We offer', 'Competitive salary', 'Attractive social and financial benefits', 'Flexible working environment', 'Access to training and development "']
[Finished in 368ms]"""

# Extract pay range
pay_range = re.search(r'£(\d+(?:,\d+)*)/yr - £(\d+(?:,\d+)*)/yr', details)
pay_start = pay_range.group(1) if pay_range else None
pay_end = pay_range.group(2) if pay_range else None

# Extract workplace type
workplace_match = re.search(r'workplace type is (\w+)', details, re.IGNORECASE)
workplace = workplace_match.group(1) if workplace_match else None

# Extract job type
job_type_match = re.search(r'job type is (\w+)', details, re.IGNORECASE)
job_type = job_type_match.group(1) if job_type_match else None

# Extract job level
job_level_match = re.search(r'(Junior|Mid|Mid-Senior|Senior|Executive) level', details)
job_level = job_level_match.group(1) if job_level_match else None

# Extract number of employees
employees_match = re.search(r'(\d+)-(\d+) employees', details)
employees_start = employees_match.group(1) if employees_match else None
employees_end = employees_match.group(2) if employees_match else None

# Extract skill match
skill_match_match = re.search(r'(\d+) of (\d+) skills match your profile', details)
skill_match = f"{skill_match_match.group(1)} out of {skill_match_match.group(2)}" if skill_match_match else None

# Print extracted information
print("Pay Range:", pay_start, "-", pay_end)
print("Workplace Type:", workplace)
print("Job Type:", job_type)
print("Job Level:", job_level)
print("Number of Employees:", employees_start, "-", employees_end)
print("Skill Match:", skill_match)
