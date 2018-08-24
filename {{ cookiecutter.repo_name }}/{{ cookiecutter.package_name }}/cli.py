import click


@click.command()
@click.option('--as-robot', '-r', is_flag=True, help='Greet as a robot.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    """{{ cookiecutter.project_short_description }}"""
    greet = 'Beep boop, hello' if as_robot else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
