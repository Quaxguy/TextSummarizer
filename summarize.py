import click
import ollama

@click.command()
@click.argument('input_text', required=False)
@click.option('-t', '--text-file', type=click.File('r'), help='A file containing the text to process')
def process_text(input_text, text_file):
    if text_file:
        input_text = text_file.read()
    if not input_text:
        raise click.UsageError("You must provide text either as an argument or via the -t/--text-file option")
    
     # Constructing the message for the ollama chat function
    message = f"summarize the following text: {input_text}"

    response = ollama.chat(model='qwen2', messages=[
        {
            'role': 'user',
            'content': message,
        },
    ])
    print(response['message']['content'])

if __name__ == '__main__':
    process_text()
