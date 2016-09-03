import click
import venusaur.thresholds
import venusaur.motifs
import venusaur.activity
import venusaur.tf_expression
import venusaur.gene_expression


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def cli(name, as_cowboy):
    """
    Driven is a full-fledged bioinformatics suite geared towards easy integration of multiple types of big data to make
    reasonable and interesting biological conclusions.
    """
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
