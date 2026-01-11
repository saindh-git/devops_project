servers = ["Server_Alpha", "Server_Beta", "Server_Gamma"]
current_index = 0

def get_next_server():
    global current_index
    selected_server=servers[current_index]
    current_index= (current_index + 1) % len(servers)
    return selected_server 
for guest in range(1,11):
    assigned_cook=get_next_server()
    print(f"Guest {guest} is being served by:{assigned_cook}")
