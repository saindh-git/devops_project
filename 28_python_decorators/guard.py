def estate_guard(original_worker):
    def wrapper():
        print(f"[LOG]{original_worker.__name__} is starting now..")
        original_worker()
        print(f"[LOG] {original_worker.__name__} has finished successfully.")
    return wrapper
@estate_guard
def restart_server():
    print("REBOOTING: Server system is cycling power...")
@estate_guard
def backup_database():
    print("SAVING: Copying all ledger data to the vault...")
restart_server()
print("-" * 20)
backup_database()
