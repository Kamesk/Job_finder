from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the passages
passage1 = """You will oversee the deployment, maintenance, and monitoring of Machine Learning models for the Healthcare Space
You will guide Machine Learning tooling and health data infrastructure within our the cloud environment GCP & establish best practices.
You will Contribute to the development of their health data platform, making informed decisions on data modeling and ensuring its resilience to future changes.
You will work daily with Data Scientists and Data Engineers.
You will advocate for data quality and observability in ML models and data systems.
You will assist in the rapid evaluation of new Data Science and AI tools as the field evolves, including assessing LLM-based solutions in the healthcare domain."""
passage2 = """Demonstrated experience building data structures to support analytics/research/actuarial functions in an insurance company setting
Experience with cloud technologies like Snowflake and Databricks
Familiarity with the MLOps framework
Ability to operate independently – managing tasks and engaging people across the team
Exceptional collaboration and relationship building skills
Comfortable handling ambiguous concepts and breaking down complex problems into manageable pieces
Strong data manipulation skills for analytics
Resilient problem solving and critical thinking skills
Thorough understanding of data warehousing concepts and design
Ability to communicate effectively to different target audiences
Flexibility – able to meet changing requirements and priorities"""

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the passages
tfidf_matrix = tfidf_vectorizer.fit_transform([passage1, passage2])

# Compute the cosine similarity
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Similarity between the passages:", similarity[0][0])
