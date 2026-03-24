from packages import login_required, validators


@login_required
def login(name):
    name = 'mohamed'
    print(name)
login('ali')

print(validators.check_e("abdo@gmail.com"))