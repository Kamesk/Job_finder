import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the passages
passage1 = """• Facilitating seamless communication and collaboration with stakeholders worldwide to address project integration, enhance pipeline efficiency, and refine Business Requirements Documents (BRD).
• Establishing meaningful connections with data scientists, business analysts, and data engineers to foster synergy, share insights, and drive impactful data-driven initiatives.
• Research and implement innovative Deep Learning approaches to enhance Amazon's spoken language applications, leveraging expertise in AWS SageMaker, TensorFlow, Keras, and other frameworks, and deploying them within Flask environments.
• Mentor junior engineers and scientists, fostering a collaborative and learning-oriented environment to drive continuous improvement and innovation in spoken language applications.
• Participate in the design, development, evaluation, deployment, and updating of data-driven models and analytical solutions for spoken language applications, ensuring alignment with business objectives and user needs. 
• End to end deployment of feature extractions from product images and developing a GAN based model to enhance the cost prediction accuracy and optimizing inventory management.
• Utilized Data Version Control (DVC) for efficient versioning of large datasets, enabling seamless integration with the machine learning model lifecycle.
• Incorporated docker and Kubernetes for all pipeline model containerization and orchestration, ensuring consistent and scalable deployment across diverse environments.
• DVC and Git versioning into the CI/CD pipelines, facilitating automated testing and deployment while maintaining the integrity of model artifacts.
• Conducted data preprocessing and feature engineering on large-scale datasets, ensuring data quality and preparing it for modeling.
"""

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

# Load GPT2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Tokenize the passages
passage1_tokens = tokenizer.encode(passage1, return_tensors="pt", max_length=1024, truncation=True)
passage2_tokens = tokenizer.encode(passage2, return_tensors="pt", max_length=1024, truncation=True)


input_ids = tokenizer.encode(passage1, return_tensors="pt", max_length=1024, truncation=True)

# Generate text similar to Passage 2 based on Passage 1
output_ids = model.generate(input_ids, max_length=450, num_return_sequences=1, temperature=0.7, pad_token_id=tokenizer.eos_token_id)


# Decode the generated text
generated_passage = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the generated passage
print("Generated Passage Similar to Passage 2:\n", generated_passage)

tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the passages
tfidf_matrix = tfidf_vectorizer.fit_transform([generated_passage, passage2])

# Compute the cosine similarity
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

print("Similarity", similarity[0][0])

