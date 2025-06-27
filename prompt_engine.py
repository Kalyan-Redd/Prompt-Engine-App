import google.generativeai as genai


gemini_api_key = "AIzaSyBIqpJycoSfpx0sSCNJVVoNFoQIPFVPaUM "
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")


def run_prompt(prompt_type,user_input):
    if prompt_type == "Zero-Shot":
        prompt = f"{user_input}"
    elif prompt_type =="Few-Shot":
        prompt = (
            "Q: Who is the president of India\n\n"
            "A: The president of India is Droupadi Murmu"
            "Q:Who is the president of United States\n\n"
            "A: The president of United States is Donald Trump"
            f"Q:{user_input}\n"
            "A: "
        )
    
    elif prompt_type == "Instruction-Based":
        prompt =(
            "Instruction :summarize my article in 3 bullet points"
            f"Text:{user_input}"  
        )  
    
    elif prompt_type =='Chain-of-Thought':
        prompt = (
            "Solve the Neural Network backpropagation equation step by step"
            f"Text: {user_input}"
        )         
        
    elif prompt_type == "Role-based":
        prompt = (
            " you are  REAL STATE Consultant, pls tell me where and why should i purshase in the Hyderabad"
            f"Text: {user_input}"
        )    
        
    else:
        prompt = user_input
        
    response = model.generate_content(prompt)
    
    return response.text.strip()        