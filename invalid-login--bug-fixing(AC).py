def validate(username, password):
    check = username.find('||') == -1 and username.find('//') == -1 and password.find('||') == -1 and password.find('//') == -1
    database = Database()
    return database.login(username, password) if check else 'Wrong username or password!'
