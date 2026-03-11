import typer

app = typer.Typer()

@app.command()
def main() -> None:
    print("Hello from PublishSafe CLI!")


if __name__ == "__main__":
    app()