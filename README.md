# Patient Education Chatbot - Project Document RAG Powered Chatbot
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pec-med-chatbot-yb29cngag6itjnmcr3vlhp.streamlit.app/)

## Background
The Patient Education System is designed to leverage a Retrieval-Augmented Generation
(RAG) powered chatbot to provide users with accurate and relevant healthcare information.
The system integrates various tools and services to preprocess, store, and retrieve data
efficiently, enhancing the user experience by delivering precise responses to their queries in
real-time.

## Goals
1. Enhance Patient Education: Provide users with accurate, relevant, and timely
healthcare information through an interactive, AI-powered chatbot to empower patients.
This will help patients to manage their care at home, helping to achieve better clinical
outcomes.
2. Ensure Data Security and Privacy: Implement robust security measures and
compliance protocols like de-identification and anonymization to protect patient data,
ensuring privacy and confidentiality while adhering to healthcare regulations such as
HIPAA and GDPR.
3. Improve User Experience: Develop a user-friendly web application interface that offers
seamless navigation, real-time query responses.

## Non-Goals
1. <strong>Full Multilingual Support:</strong> Initially, the system may not support multiple languages and
will primarily operate in English, with potential multilingual support considered for future
enhancements.
2. <strong>Audio Support:</strong> Initially the system may not support audio conversion to text. But it
might be included in future work.
3. <strong>Authentication and Authorization Management:</strong> The project will not focus on
developing user authentication and authorization mechanisms.
4. <strong>Encryption:</strong> This solution will not encrypt data for data security.
5. <strong>Scalability Solutions:</strong> It will not focus on scalability solutions for handling concurrent
users.
6. <strong>Logging and Monitoring:</strong> The project will not include logging and monitoring
capabilities.

## Estimated Milestones & Timeline
<strong>Phase 1: Planning and Initial Setup (Week 1)</strong>
- Finalise project requirements and scope.
- Set up project management tools
- Define architecture and data flow diagrams.
- Select and set up initial development environments and tools (AWS services, Pinecone Vector DB, etc.).

<strong>Phase 2: Backend Development (Week 2)</strong>
- Set up AWS S3 buckets for storing structured and unstructured data.
- Integrate the Pinecone Vector Database with backend services.
- Implement data preprocessing, de-identification and anonymization workflows.

<strong>Phase 3: Data Integration and Embedding (Week 3-4)</strong>
- Ingest general and patient-specific data into the system.
- Implement chunking, tokenization, and embedding processes.
- Populate the Pinecone Vector Database with embedded data.
- Ensure data integrity and proper indexing for efficient retrieval.

<strong>Phase 4: Large Language Model (LLM) Integration (Week 5-6)</strong>
- Develop Lambda functions for query embedding and data preprocessing.
- Integrate LLM with the backend to process and generate responses.
- Conduct initial testing of query processing and response generation.
- Optimise LLM performance and response accuracy.
- Implement feedback loops for continuous model improvement.

<strong>Phase 5: Frontend Development (Week 7)</strong>
- Develop the web application interface using Streamlit or other frontendtechnologies.
- Integrate the frontend with backend services for data query and responsehandling.
- Conduct initial frontend testing and user interface improvements.

<strong>Phase 6: Testing & Launch (Week 8)</strong>
- Conduct user acceptance testing with select group of users
- Finalise system deployment plans and conduct final testing
- Deploy system to a production environment

<strong>Phase 7: Presentation (Week 9)</strong>
- Present solution with presentation and final design document

## Technical Details

### Data Flow Diagram
![alt Data Flow Diagram](https://github.com/adeelbarki/pec-med-chatbot/blob/main/images/flow-diagram.png)

#### Real time Data Flow
1. User Interaction (Step 1 & 6): The user interacts with the web application interface,
which is developed using Streamlit or other frontend technologies. The user's query is
sent to the backend for processing.
2. Query Embedding (Step 2): The query is forwarded to a Lambda function that
generates query embeddings.
3. Pinecone Vector DB (Step 3): The generated embeddings are used to query the
Pinecone Vector Database to retrieve relevant information.
4. Large Language Model (LLM) (Step 4): The retrieved information is sent to an LLM,
which processes the data to generate a coherent and contextually appropriate response.
5. Response Delivery (Step 5): The response is sent back through the web application to
the user.
#### Data Ingestion
1. Unstructured Data (Step A): Unstructured data is collected and stored in a designated
S3 bucket.
2. Data Preprocessing (Step B): A Lambda function preprocesses this data and process
de-identification and anonymization. Then convert it to chunks.
3. Structured Data (Step B): Structured data is similarly stored in another S3 bucket and
processed.
4. Embedding (Step C): After tokenization, the data is embedded and injected into the
Pinecone Vector Database using another Lambda function.
5. Database Population (Step D): The Pinecone Vector Database is populated with these
embeddings, making the data ready for retrieval during user queries.
#### Tools & Technologies
- Frontend: Streamlit or similar frameworks for developing the web application interface.
- Lambda Functions: AWS Lambda for serverless computing to handle query
embedding, data preprocessing, and data injection.
- Pinecone Vector Database: For storing and retrieving vector embeddings efficiently.
- Large Language Model (LLM): For generating contextually relevant responses based
on the retrieved data. Chatgpt and langchain are used for interacting with human-like
text and response for our patient queries.
- AWS S3 Buckets: For storing structured and unstructured data.
- Voyage API: For embedding, enhancing semantic search and RAG for AI applications
#### Cost Management
- AWS Lambda: $0.20 per 1 million requests
- S3 storage: $0.023 per GB for standard storage
- Amazon API Gateway: $3.5 per million requests
- Pinecone: 0.07 per index hour for storage
- Total Estimated Cost: < $20
#### Limitation
1. Scalability: Handling a high volume of concurrent users may require efficient scaling of
Lambda functions and database operations.
2. Latency: Real-time data retrieval and processing may introduce latency, affecting user
experience.
3. Data Privacy: Ensuring privacy and security of user data, especially in healthcare, is
paramount and must comply with relevant regulations (e.g.,HIPAA, PIPEDA, GDPR).
4. Model Accuracy: The accuracy of responses depends on the quality of the LLM and
the embedded data. Continuous training and data updates are necessary to maintain
high accuracy.
5. Handling Real time data Processing - Handling real-time data flow efficiently to
provide quick responses
6. Bias: The chatbot may inherit biases present in the training data, potentially leading to
biassed responses. Regular audits and updates to the training data are essential to
mitigate this.
7. Misinterpretation: The LLM might misinterpret user queries or provide incorrect
information. Clear user prompts and regular model updates can help reduce these
occurrences.
8. Scope: The system is designed for patient education and should not be used as a
replacement for professional medical advice. Its scope should be clearly defined to
users to avoid misuse.
9. Cost Management: Balancing performance and cost, especially with usage-based
pricing models, requires careful monitoring and optimization.
#### Conclusion
The Patient Education System - RAG Powered Chatbot is a sophisticated integration of
modern technologies aimed at providing users with reliable healthcare information. By
leveraging serverless architecture and advanced machine learning models, the system
ensures efficient and accurate responses. However, considerations around scalability,
latency, data privacy, model accuracy, bias, misinterpretation, project scope, and cost
management are crucial for its successful deployment and operation.

## Future Work
![alt future work Diagram](https://github.com/adeelbarki/pec-med-chatbot/blob/main/images/future-work.png)
1. Integration with Electronic Health Records (EHR):
- Develop APIs to seamlessly integrate with various EHR systems.
- Ensure secure and efficient data exchange protocols between the hospital
network and the chatbot system.
2. Enhanced Data Security and Privacy:
- Implement advanced encryption methods for data at rest and in transit.
- Regularly update anonymization and de-identification techniques to comply
with evolving data privacy regulations.
3. User Authentication and Authorization Improvements:
- Incorporate multi-factor authentication (MFA) for enhanced security.
4. Scalability and Performance Optimization:
- Use serverless architecture and auto-scaling features to handle increased
user load efficiently.
5. Advanced Natural Language Processing (NLP) Techniques:
- Integrate more sophisticated NLP models to better understand and interpret
user queries.
6. Personalization and Customization:
- Develop mechanisms to personalise responses based on user history and
preferences.
- Allow users to customise their interface and the type of information they
receive.
7. Comprehensive Logging and Monitoring:
- Implement detailed logging of user interactions for better troubleshooting and
system improvement.
- Set up monitoring tools to detect and respond to system anomalies in
real-time.
8. User Feedback and Continuous Improvement:
- Create a feedback loop where users can rate responses and provide
suggestions.
- Use feedback to iteratively improve the chatbot's performance and accuracy.
9. Expansion of Data Sources:
- Incorporate additional data sources such as medical journals, clinical trials,
and patient forums.
- Ensure the data is regularly updated and validated for accuracy.
10. Multi-language Support:
- Implement support for multiple languages to cater to a diverse user base.
- Ensure translations maintain the accuracy and context of medical information.
11. Compliance and Certification:
- Regularly audit the system for compliance with healthcare regulations (e.g.,
HIPAA, GDPR, PIPEDA).
- Seek certifications from relevant health information authorities to build trust
with users.
12. User Interface Enhancements:
- Improve the user interface for better accessibility and ease of use.
- Include features like voice recognition and response for hands-free
interaction.
13. AI and Machine Learning Integration:
- Continuously train the models with new data to improve their predictive
accuracy.
14. Interoperability with Other Health Applications:
- Ensure the system can interoperate with other health and wellness
applications.
- Develop plugins or modules that can be integrated into other platforms

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
