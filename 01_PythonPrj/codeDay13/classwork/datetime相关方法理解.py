class Userinfo:
    def user(self):
        return User()

    def info(self):
        return Info()

    def __str__(self):
        return 'userinfo...'


class User:
    def __str__(self):
        return 'user...'


class Info:
    def __str__(self):
        return 'info...'


if __name__ == '__main__':
    userinfo_obj = Userinfo()
    print(userinfo_obj.user())
    print(type(userinfo_obj.user()))

    print(userinfo_obj.info())
    print(type(userinfo_obj.info()))
