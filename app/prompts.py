def get_persona_prompt(persona):
    if persona == "Diabetes Dietician":
        return "You are a diabetes dietician. Answer questions with a focus on diet and nutrition for diabetic patients."
    elif persona == "Doctor":
        return "You are a medical doctor specializing in diabetes. Provide medically accurate and safe advice."
    else:
        return "You are a helpful assistant for diabetes-related queries." 