from bs4 import BeautifulSoup

content = """<!---->MLOps Engineer<!---->

                Harnham
              
content_1 = 
              <ul>
                    <li class="job-details-jobs-unified-top-card__job-insight job-details-jobs-unified-top-card__job-insight--highlight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <li-icon aria-hidden="true" type="job" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
      <path d="M17 6V5a3 3 0 00-3-3h-4a3 3 0 00-3 3v1H2v4a3 3 0 003 3h14a3 3 0 003-3V6zM9 5a1 1 0 011-1h4a1 1 0 011 1v1H9zm10 9a4 4 0 003-1.38V17a3 3 0 01-3 3H5a3 3 0 01-3-3v-4.38A4 4 0 005 14z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
                            <span>
                              <!---->£80,000/yr - £90,000/yr<!---->
                            </span>

<!----><!---->
                            <span class="job-details-jobs-unified-top-card__job-insight-view-model-secondary">
                              
    <span class="ui-label ui-label--accent-3 text-body-small">
      <span aria-hidden="true"><!---->Hybrid<!----></span><span class="visually-hidden"><!---->Matches your job preferences, workplace type is Hybrid.<!----></span>
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
        <li-icon aria-hidden="true" type="company" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
      <path d="M4 2v20h16V2zm14 18h-4v-2h-4v2H6V4h12zm-7-8H8v-2h3zm0 4H8v-2h3zm5-4h-3v-2h3zm-5-4H8V6h3zm5 0h-3V6h3zm0 8h-3v-2h3z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
                        <!---->201-500 employees · Staffing and Recruiting<!---->
                      </span>
                    </li>
                    <li class="job-details-jobs-unified-top-card__job-insight">
                      <div class="flex-shrink-zero mr2 t-black--light">
                        
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        display-flex">
        <li-icon aria-hidden="true" type="people" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
      <path d="M12 16v6H3v-6a3 3 0 013-3h3a3 3 0 013 3zm5.5-3A3.5 3.5 0 1014 9.5a3.5 3.5 0 003.5 3.5zm1 2h-2a2.5 2.5 0 00-2.5 2.5V22h7v-4.5a2.5 2.5 0 00-2.5-2.5zM7.5 2A4.5 4.5 0 1012 6.5 4.49 4.49 0 007.5 2z"></path>
    </svg></li-icon>
    </div>
  
          </div>
  
                      </div>
                      <span>
                        <a class="app-aware-link " target="_self" href="https://www.linkedin.com/search/results/people/?origin=JOB_PAGE_CANNED_SEARCH&amp;network=%22F%22&amp;currentCompany=%5B280603%5D" data-test-app-aware-link=""><!---->1 connection works here<!----></a><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span><a class="app-aware-link " target="_self" href="https://www.linkedin.com/search/results/people/?origin=JOB_PAGE_CANNED_SEARCH&amp;currentCompany=%5B280603%5D&amp;pastCompany=%5B1586%5D" data-test-app-aware-link=""><!---->3 company alumni work here<!----></a><span class="white-space-pre"> </span>·<span class="white-space-pre"> </span><a class="app-aware-link " target="_self" href="https://www.linkedin.com/search/results/people/?origin=JOB_PAGE_CANNED_SEARCH&amp;currentCompany=%5B280603%5D&amp;schoolFilter=%5B8890%5D" data-test-app-aware-link=""><!---->1 school alum works here<!----></a>
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
                            <a class="app-aware-link " target="_self" href="#HYM" data-test-app-aware-link=""><!---->3 of 3 skills match your profile - you may be a good fit<!----></a>
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
                      <button class="job-details-jobs-unified-top-card__job-insight-text-button ml1" aria-label="View verified hiring modal" type="button">
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
                            <!---->See how you compare to 3 applicants.<span class="white-space-pre"> </span><a class="app-aware-link " target="_self" href="https://www.linkedin.com/premium/products/?family=JSS&amp;upsellOrderOrigin=premium_job_details_summary_card&amp;utype=job&amp;referenceId=CgCT20W3RSGrbgXEPBcX2w%3D%3D" data-test-app-aware-link=""><!---->Reactivate Premium<!----></a>
                          </span>
                        </li>
              </ul>
          
content_2
                <p><strong><!---->MLOps Engineer<!----></strong></p><p><strong><!---->up to £90,000<span class="white-space-pre"> </span></strong></p><p><strong><!---->London (1 day a week in the office)<!----></strong></p><p><br></p><p><br></p><p><br></p><p><!---->Join the leader in the Healthcare-tech space!<!----></p><p><br></p><p><br></p><p><br></p><p><br></p><p><strong><!---->Responsibilities:<!----></strong></p>      <ul><li><!---->You will oversee the deployment, maintenance, and monitoring of Machine Learning models for the Healthcare Space<!----></li><li><!---->You will guide Machine Learning tooling and health data infrastructure within the cloud environment GCP &amp; establish best practices.<!----></li><li><!---->You will Contribute to the development of their health data platform, making informed decisions on data modeling and ensuring its resilience to future changes.<!----></li><li><!---->You will work daily with Data Scientists and Data Engineers.<!----></li><li><!---->You will advocate for data quality and observability in ML models and data systems.<!----></li><li><!---->You will assist in the rapid evaluation of new Data Science and AI tools as the field evolves, including assessing LLM-based solutions in the healthcare domain.<!----></li></ul>
<p><br></p><p><br></p><p><br></p><p><strong><!---->Requirements:<!----></strong></p>      <ul><li><!---->You have experience with cloud data infrastructure, GCP, or Azure<!----></li><li><!---->You have experience deploying and maintaining ML models into production (including observability and alerting)<!----></li><li><!---->You have a strong SQL and Python proficiency<!----></li><li><!---->You have a Strong knowledge of data modeling best practices<!----></li><li><!---->Experience deploying LLMs at scale is a plus<!----></li></ul>
<p><br></p><p><br></p><p><br></p><p><br></p><p><strong><!---->Benefits:<!----></strong></p>      <ul><li><!---->Hybrid working (1 day a week in the office)<!----></li><li><!---->Learning Budget<!----></li><li><!---->Competitive Salary<!----></li><li><!---->26 holiday days<!----></li></ul>
<p><br></p><p><br></p><p><br></p><p><strong><!---->HOW TO APPLY:<!----></strong></p><p><!---->Register your interest by sending your CV to Luc Simpson-Kent via the Apply link on this page.<!----></p>
<!---->            
"""

soup = BeautifulSoup(content, 'html.parser')

# Find all span elements within the given div
span_elements = soup.find_all('span')

# Iterate through each span element and print its text content
for span_element in span_elements:
    print(span_element.text.strip())