def chat(query):
    # operation
    response = f"You wanted to know about {query}"
    response = {
        "status_code":200,
        "data":response
    }
    return response