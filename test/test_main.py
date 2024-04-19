# première version basique pour un hello world histoire de commencer quelque part
# main affiche simplemain un hello world dans la console


import main

def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World !\n"

