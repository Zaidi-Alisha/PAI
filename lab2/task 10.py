def build_message(**info):
    message_parts = []
    
    for key, value in info.items():
        message_parts.append(f"{key.capitalize()}: {value}")
    
    formatted_message = "\n".join(message_parts)
    
    return formatted_message

print(build_message(name="Alisha Zaidi", age=19, city="Karachi", profession="CS Major"))
