import pytest
from hello_world.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
