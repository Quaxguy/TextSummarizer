import click
import requests
import json

@click.command()
@click.option('--text', prompt='Enter text', help='The text to summarize')
def summarize(text):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "prompt": f"Summarize the following text: {text}",
        "model": "qwen2"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        # Split the response by newlines and take the first valid JSON part
        first_json_part = response.text.splitlines()[0]
        result = json.loads(first_json_part)
        print("Summary:", result['response'])
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode failed: {e}")

if __name__ == '__main__':
    summarize()
