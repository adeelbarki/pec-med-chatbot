from imports import *

# Function to generate pre-signed URL
def generate_presigned_url(s3_uri):
    # Parse the S3 URI
    parsed_url = urlparse(s3_uri)
    bucket_name = parsed_url.netloc
    object_key = parsed_url.path.lstrip('/')
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Generate a pre-signed URL for the S3 object
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600  # URL expiration time in seconds
    )
    return presigned_url

# Function to retrieve documents, generate URLs, and format the response
def retrieve_and_format_response(query, retriever, llm):
    docs = retriever.get_relevant_documents(query)
    
    formatted_docs = []
    for doc in docs:
        content_data = doc.page_content
        s3_uri = doc.metadata['id']
        s3_gen_url = generate_presigned_url(s3_uri)
        formatted_doc = f"{content_data}\n\n[More Info]({s3_gen_url})"
        formatted_docs.append(formatted_doc)
    
    combined_content = "\n\n".join(formatted_docs)
    # print(combined_content)
    
    # Create a prompt for the LLM to generate an explanation based on the retrieved content
    prompt = f"Instruction: Based on the following information, provide a summarized & concise explanation using a couple of sentences. \
               Only respond with the information relevant to the user query {query}, if there are none, make sure you say 'I don't know, I did not find the relevant data in the knowledge base.' \
               In the event that there's relevant info, make sure to attach the download button at the very end: \n\n[More Info]({s3_gen_url}) \
               Context: {combined_content}"
    
    # Create the messages for the LLM input
    messages = [HumanMessage(content=prompt)]
    
    # Generate the response using the LLM
    response = llm(messages=messages)
    return {"answer": response.content}

# Example usage with memory
def ask_question(query, llm, docsearch, chain, memory):
    # Retrieve and format the response with pre-signed URLs
    response_with_docs = retrieve_and_format_response(query, docsearch.as_retriever(), llm)
    
    # Add the retrieved response to the memory
    memory.save_context({"input": query}, {"output": response_with_docs['answer']})
    
    # Use the conversation chain to get the final response
    response = chain.invoke(query)
    pattern = r"s3(.*?)(?=json)"
    s3_uris = ["s3" + x + "json" for x in re.findall(pattern, response)]
    final_response = ""
    for s3_uri in s3_uris:
        final_response = response.replace(s3_uri, generate_presigned_url(s3_uri))
    return display(Markdown(final_response))