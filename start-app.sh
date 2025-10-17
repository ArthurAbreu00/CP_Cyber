#!/usr/bin/env bash
set -e
echo "Iniciando ClickSeguro (demo vulnerável) na porta 8080..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
# rodar em foreground (o workflow executa em background com &)
python3 app.py
