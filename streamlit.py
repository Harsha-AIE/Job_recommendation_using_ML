import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF to extract text from PDF
from skill_extraction import extract_skills

# Function to extract text from a PDF using PyMuPDF (fitz)
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()  # Extract text from each page
    return pdf_text

# Load job data
job_data = pd.read_csv('job_listing.csv')  # Update the path to your CSV file

# Display the title of the app
st.title("Job Recommendation System")

# Upload CV file
uploaded_file = st.file_uploader("Upload your CV", type="pdf")
if uploaded_file is not None:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Extract skills from the text
    skills = extract_skills(text)
    st.write("Extracted Skills:", skills)

    # Check if skills were successfully extracted
    if skills:
        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        job_vectors = vectorizer.fit_transform(job_data['Job Description'])

        # User skill vectorization
        user_vector = vectorizer.transform([' '.join(skills)])

        # Compute cosine similarity
        similarities = cosine_similarity(user_vector, job_vectors)

        # Get top 5 recommended jobs
        top_indices = similarities.argsort()[0][-5:][::-1]
        recommended_jobs = job_data.iloc[top_indices]

        # Display recommended jobs
        st.write("Recommended Jobs:")
        for i in range(len(recommended_jobs)):
            st.write(f"**Job Title:** {recommended_jobs.iloc[i]['Job Title']}")
            st.write(f"**Company Name:** {recommended_jobs.iloc[i]['Company Name']}")
            st.write(f"**Salary Estimate:** {recommended_jobs.iloc[i]['Salary Estimate']}")
    else:
        st.write("No skills extracted. Please check the PDF content.")
