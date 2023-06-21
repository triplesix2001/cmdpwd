import typer
import keyring
import pyperclip

app = typer.Typer()

# Test kommando
@app.command()
def repeat(word: str):
    typer.echo(word)

# 
@app.command()
def new(link: str, name: str, pwd: str):
    keyring.set_password(link, name, pwd)
    typer.echo("Password stored")

@app.command()
def get(link: str, name: str):
    pwd = keyring.get_password(link, name)
    if pwd:
        pyperclip.copy(pwd)
        typer.echo("Password is copied to clipboard")
    else:
        typer.echo("Password not found.")

if __name__ == "__main__":
    app()
