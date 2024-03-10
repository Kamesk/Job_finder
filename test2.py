from bs4 import BeautifulSoup
content2 = """<span>
                <strong><!---->Company Description<!----><br><br></strong><!---->Louis Dreyfus Company is a leading merchant and processor of agricultural goods. Our activities span the entire value chain from farm to fork, across a broad range of business lines, we leverage our global reach and extensive asset network to serve our customers and consumers around the world. Structured as a matrix organization of six geographical regions and ten platforms, Louis Dreyfus Company is active in over 100 countries and employs approximately 17,000 people globally.<!----><br><br><br><strong><!---->Job Description<!----><br><br></strong><!---->LDC is on the lookout for a Quantitative Strategist to enhance our Global Data Science team. In this multifaceted role, you will first play a key part in improving our systematic trading infrastructure. And as the project evolves you will be more and more at the forefront of developing innovative trading strategies. You will collaborate with systematic trading and IT teams, applying your expertise to systematically implement and peer-review trading strategies, as well as driving technological advancements across the company.<!----><br><br><br><strong><!---->Main responsibilities:<span class="white-space-pre"> </span><br></strong>      <ul><li><!---->Spearhead the enhancement of our framework, introducing new features and capabilities to meet the users’ requirements.<!----></li><li><!---->Lead the resolution of complex technical challenges independently or by orchestrating team members’ tasks.<!----></li><li><!---->Design and execute advanced quantitative models for market analysis, risk management, and implement proven trading strategies.<!----></li><li><!---->Facilitate the integration of these strategies into our trading platforms, working alongside systematic and proprietary trading teams.<!----></li><li><!---->Oversea the peer-review process of the strategies presented by systematic traders.<!----></li><li><!---->Maintain a leading edge in systematic trading to integrate advanced trading strategies.<!----></li><li><!---->Collaborate with IT and Data Science teams to facilitate platform improvements and increase adoption.<!----></li><li><!---->Responsible of DevOps/MLOps best practices, including code/data versioning, and rigorous testing protocols.<!----></li><li><!---->Clearly communicate complex quantitative concepts and strategies to a diverse range of stakeholders.<!----><br><br></li></ul>
<strong><!---->Experience<!----><br></strong>      <ul><li><!---->MSc or PhD in a quantitative field such as Mathematics, Statistics, Financial Engineering, Econometrics, Computer Science, or similar.<!----></li><li><!---->7+ years of experience in quantitative research in a commodity trading firm, Hedge Fund, or bank.<!----></li><li><!---->Skilled in Python (backend in object-oriented – and frontend being a plus).<!----></li><li><!---->Experience with DevOps and MLOps.<!----></li><li><!---->Exceptional analytical and statistical capabilities, with a proven track record in problem-solving.<!----></li><li><!---->Experience with implementing machine learning trading models in finance.<!----></li><li><!---->Excellent communication skills for effectively conveying complex concepts.<!----></li><li><!---->Passionate about financial markets and systematic trading.<!----></li><li><!---->Ability to work independently and in collaborative settings, with proven leadership skills.<!----></li><li><!---->Experience in agricultural commodities trading is a strong plus.<!----><br><br></li></ul>
<!---->Additional Information<!----><br><br><!---->Additional Information for the job<!----><br><br><strong><!---->Diversity &amp; Inclusion<!----><br><br></strong><!---->LDC is driven by a set of shared values and high ethical standards, with diversity and inclusion being part of our DNA. LDC is an equal opportunity employer committed to providing a working environment that embraces and values diversity, equity and inclusion.<!----><br><br><br><!---->LDC encourages diversity, supports local communities and environmental initiatives. We encourage people of all backgrounds to apply.<!----><br><br><br><strong><!---->Sustainability<!----><br><br></strong><!---->Sustainable value is at the heart of our purpose as a company.<!----><br><br><br><!---->We are passionate about creating fair and sustainable value, both for our business and for other value chain stakeholders: our people, our business partners, the communities we touch and the environment around us<!----><br><br><!---->"What We Offer<!----><br><br><!---->We provide a dynamic and stimulating international environment, which will stretch and develop your abilities and channel your skills and expertise with outstanding career development opportunities in one of the largest and most solid private companies in the world.<!----><br><br><br><!---->We offer<!----><br>      <ul><li><span class="white-space-pre"> </span>Competitive salary<!----></li><li><span class="white-space-pre"> </span>Attractive social and financial benefits<!----></li><li><span class="white-space-pre"> </span>Flexible working environment<!----></li><li><span class="white-space-pre"> </span>Access to training and development "<!----><br></li></ul>

<!---->            </span>"""
content1 = """<div class="mt3 mb2">
              <ul>
                    <li class="job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <li-icon aria-hidden="true" type="job" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;">
      <path d="M17 6V5a3 3 0 00-3-3h-4a3 3 0 00-3 3v1H2v4a3 3 0 003 3h14a3 3 0 003-3V6zM9 5a1 1 0 011-1h4a1 1 0 011 1v1H9zm10 9a4 4 0 003-1.38V17a3 3 0 01-3 3H5a3 3 0 01-3-3v-4.38A4 4 0 005 14z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
<!---->
                            <span>
                              
    <span class="ui-label ui-label--accent-3 text-body-small">
      <span aria-hidden="true"><!---->On-site<!----></span><span class="visually-hidden"><!---->Matches your job preferences, workplace type is On-site.<!----></span>
    </span>
  
                            </span>
<!---->
                            <span class="job-details-jobs-unified-top-card__job-insight-view-model-secondary">
                              
    <span class="ui-label ui-label--accent-3 text-body-small">
      <span aria-hidden="true"><!---->Full-time<!----></span><span class="visually-hidden"><!---->Matches your job preferences, job type is Full-time.<!----></span>
    </span>
  
                            </span>
                            <span class="job-details-jobs-unified-top-card__job-insight-view-model-secondary">
                              <!---->Mid-Senior level<!---->
                            </span>

<!---->                      </span>
                    </li>
                                      <li class="job-details-jobs-unified-top-card__job-insight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <li-icon aria-hidden="true" type="company" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;">
      <path d="M4 2v20h16V2zm14 18h-4v-2h-4v2H6V4h12zm-7-8H8v-2h3zm0 4H8v-2h3zm5-4h-3v-2h3zm-5-4H8V6h3zm5 0h-3V6h3zm0 8h-3v-2h3z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
                        <!---->10,001+ employees · Food and Beverage Manufacturing<!---->
                      </span>
                    </li>
                    <li class="job-details-jobs-unified-top-card__job-insight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <li-icon aria-hidden="true" type="people" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;">
      <path d="M12 16v6H3v-6a3 3 0 013-3h3a3 3 0 013 3zm5.5-3A3.5 3.5 0 1014 9.5a3.5 3.5 0 003.5 3.5zm1 2h-2a2.5 2.5 0 00-2.5 2.5V22h7v-4.5a2.5 2.5 0 00-2.5-2.5zM7.5 2A4.5 4.5 0 1012 6.5 4.49 4.49 0 007.5 2z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
                        <a class="app-aware-link " target="_self" href="https://www.linkedin.com/search/results/people/?origin=JOB_PAGE_CANNED_SEARCH&amp;currentCompany=%5B7177%5D&amp;pastCompany=%5B1586%5D" data-test-app-aware-link=""><!---->12 company alumni work here<!----></a><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span><a class="app-aware-link " target="_self" href="https://www.linkedin.com/search/results/people/?origin=JOB_PAGE_CANNED_SEARCH&amp;currentCompany=%5B7177%5D&amp;schoolFilter=%5B8890%5D" data-test-app-aware-link=""><!---->6 school alumni work here<!----></a>
                      </span>
                    </li>
                        <li class="job-details-jobs-unified-top-card__job-insight">
                          <div class="flex-shrink-zero mr2 t-black--light">
                            
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <svg role="none" aria-hidden="true" class="  rtl-flip" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="checklist-medium">
<!---->    

    <use href="#checklist-medium" width="24" height="24"></use>
</svg>

    </div>
  
          </div>
  
                          </div>
                          <button class="job-details-jobs-unified-top-card__job-insight-text-button" aria-label="View strong skill match modal" tabindex="-1" type="button">
                            <a class="app-aware-link " target="_self" href="#HYM" data-test-app-aware-link=""><!---->Skills: MLOps, Communication, +8 more<!----></a>
                          </button>
                        </li>
                    <li class="job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <svg role="none" aria-hidden="true" class=" " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="verified-medium">
<!---->    

    <use href="#verified-medium" width="24" height="24"></use>
</svg>

    </div>
  
          </div>
  
                      </div>
                      <span>
                        <span aria-hidden="true"><!---->View verifications related to this job post.<!----></span><span class="visually-hidden"><!---->View verifications related to this job post.<!----></span>
                      </span>
                      <button class="job-details-jobs-unified-top-card__job-insight-text-button ml1" aria-label="View verified hiring modal" type="button" fdprocessedid="xrlpab">
                        Show all
                      </button>
                    </li>

                        <li class="job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight">
                          <div class="flex-shrink-zero mr2 t-black--light">
                            
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <svg role="none" aria-hidden="true" class=" " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="lightbulb-medium">
<!---->    

    <use href="#lightbulb-medium" width="24" height="24"></use>
</svg>

    </div>
  
          </div>
  
                          </div>
                          <span>
                            <!---->See how you compare to 7 applicants.<span class="white-space-pre"> </span><a class="app-aware-link " target="_self" href="https://www.linkedin.com/premium/products/?family=JSS&amp;upsellOrderOrigin=premium_job_details_summary_card&amp;utype=job&amp;referenceId=b4%2Fk53MmSICiOo5csq7CDw%3D%3D" data-test-app-aware-link=""><!---->Reactivate Premium<!----></a>
                          </span>
                        </li>
              </ul>
          </div>"""
combined_content = content1 + content2
soup = BeautifulSoup(combined_content, 'html.parser')
text_elements = soup.find_all(string=True)
details = []
for element in text_elements:
	if element.strip():
		details.append(element.strip())
print(details)
