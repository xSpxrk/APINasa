from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

greeting_template = env.get_template('greeting.txt')


def load_greeting_template(name, bot_name):
    return greeting_template.render(name=name, bot_name=bot_name)
