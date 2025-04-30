




def generate_id():
    generate_id.counter += 1
    return generate_id.counter
setattr(generate_id, 'counter', 0)