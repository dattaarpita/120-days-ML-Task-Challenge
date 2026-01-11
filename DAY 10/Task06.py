USER="admin"
def admin_required(func):
    def inner(*args, **kwargs):
     if USER!="admin":
        raise PermissionError("Access denied")
     func(*args, **kwargs)      
    return inner

@admin_required
def original_func():
    print("This is only accessed by Admin user")
original_func()
