# prompts.py

 
# Define the QA Chain Prompt
def get_qa_chain_prompt():
    template = """
        You are an expert AI assistant with access to context from a PDF. Your goal is to accurately extract information 
        and enhance the question based on specific details present in the PDF.

        Instructions:
        1. Search through the provided PDF context and identify key entities such as company names, product names, 
        locations, or any specific terms relevant to the question.
        2. Use this information to form a detailed and precise question for web search.
        3. If there are relevant entity names or specific terms in the PDF context, include them directly in your answer.

        Examples:
        Ques: "Tell me about the companies in this PDF?"
        Context: The PDF mentions Google, Microsoft, and Netflix as key companies.
        Action: Identify the company names from the PDF context and refine the question.
        Answer: "Tell me about Google, Microsoft, and Netflix."

        Ques: "What are the benefits of cloud computing mentioned?"
        Context: The PDF discusses AWS, Google Cloud, and Azure in relation to cloud computing.
        Action: Identify the specific cloud providers and refine the question.
        Answer: "What are the benefits of cloud computing services like AWS, Google Cloud, and Azure?"

        Now, based on the given context, generate a refined question:
        {context}
        Original Question: {question}
        Refined Question:
    """
    return  template

# Define the Search Results Prompt
def get_search_results_prompt():
   
    
    template = '''Please respond to the following query in CSV format: {query}. Structure the output so that each row represents a distinct entry related to the query, with columns capturing all relevant information. Follow these guidelines to ensure well-organized output:

                Identify Headers: Based on {query}, determine appropriate column headers. For instance, if the query involves countries and their capitals, use 'Country' and 'Capital'. If it's a comparison of products, use headers like 'Product', 'Price', 'Features', etc. Adjust headers based on the query's context and add columns as necessary to fully represent the requested details.

                Populate Rows and Columns: For each distinct item in {query}, create a new row. Align all details across columns so each row corresponds to a single entry or item, structured under the correct headers.

                Output in CSV Format: Format the entire output as CSV, separating each column with a comma and placing each row on a new line. Avoid extra spaces or unnecessary lines within the CSV to maintain clarity.

                Examples:

                Query: "What are the capitals of Chile, Djibouti, and Antigua and Barbuda?"

                Expected Output:

                Country,Capital
                Chile,Santiago
                Djibouti,Djibouti
                Antigua and Barbuda,St. John's

                Query: "Compare the features of iPhone 15 and Samsung Galaxy S23"

                Expected Output:
                Product,Screen Size,Camera,Processor,Battery Life
                iPhone 15,6.1 inch,48MP,A16 Bionic,24 hours
                Samsung Galaxy S23,6.1 inch,50MP,Snapdragon 8 Gen 2,26 hours

                Use this format for any {query}, adapting headers and columns based on the type of information requested. Ensure that each column has a clear label, rows are properly aligned, and all data is structured as requested in CSV format.
                '''

    return template
