import json
import os
 
ARQ = "produtos.json"
 
 
def _carregar():
    if not os.path.exists(ARQ):
        return []
    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)
 
 
def _salvar(produtos):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=2)
 
 
def cadastrar_produto():
    produtos = _carregar()
    codigo = f"P{len(produtos) + 1:04d}"
    print(f"Codigo: {codigo}")
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()
    preco = float(input("Preco: "))
    estoque = int(input("Estoque: "))
 
    produtos.append({
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque,
    })
    _salvar(produtos)
    print("Cadastrado!")
 
 
def editar_produto():
    produtos = _carregar()
    if not produtos:
        print("Vazio.")
        return
 
    cod = input("Codigo: ").strip()
    for p in produtos:
        if p["codigo"] == cod:
            p["nome"] = input(f"Nome [{p['nome']}]: ").strip() or p["nome"]
            p["categoria"] = input(f"Categoria [{p['categoria']}]: ").strip() or p["categoria"]
            preco_input = input(f"Preco [{p['preco']:.2f}]: ").strip()
            if preco_input:
                p["preco"] = float(preco_input)
            estoque_input = input(f"Estoque [{p['estoque']}]: ").strip()
            if estoque_input:
                p["estoque"] = int(estoque_input)
            _salvar(produtos)
            print("Atualizado!")
            return
 
    print("Nao encontrado.")
 
 
def listar_produtos():
    produtos = _carregar()
    if not produtos:
        print("Vazio.")
        return
    for p in produtos:
        print(f"[{p['codigo']}] {p['nome']} | {p['categoria']} | R${p['preco']:.2f} | Estoque: {p['estoque']}")
 
 
def buscar_produto():
    produtos = _carregar()
    if not produtos:
        print("Vazio.")
        return
    termo = input("Nome ou codigo: ").strip()
    for p in produtos:
        if termo.lower() in p["nome"].lower() or termo == p["codigo"]:
            print(f"[{p['codigo']}] {p['nome']} | R${p['preco']:.2f} | Estoque: {p['estoque']}")
 
 
def ver_estoque():
    produtos = _carregar()
    if not produtos:
        print("Vazio.")
        return
    for p in produtos:
        if p["estoque"] == 0:
            status = "SEM ESTOQUE"
        elif p["estoque"] <= 5:
            status = "BAIXO"
        else:
            status = "OK"
        print(f"[{p['codigo']}] {p['nome']} | {p['estoque']} un | {status}")
 
 
def registrar_venda():
    produtos = _carregar()
    if not produtos:
        print("Vazio.")
        return
 
    cod = input("Codigo: ").strip()
    for p in produtos:
        if p["codigo"] == cod:
            if p["estoque"] == 0:
                print("Sem estoque!")
                return
            print(f"Produto: {p['nome']} | Estoque: {p['estoque']}")
            qtd = int(input("Quantidade: "))
            if qtd > p["estoque"]:
                print("Quantidade insuficiente!")
                return
            p["estoque"] -= qtd
            _salvar(produtos)
            total = qtd * p["preco"]
            print(f"Venda: {qtd} x R${p['preco']:.2f} = R${total:.2f} | Restante: {p['estoque']}")
            return
 
    print("Nao encontrado.")
 
 
def menu_produto():
    opcoes = {
        "1": ("Cadastrar", cadastrar_produto),
        "2": ("Editar", editar_produto),
        "3": ("Listar", listar_produtos),
        "4": ("Buscar", buscar_produto),
        "5": ("Estoque", ver_estoque),
        "6": ("Venda", registrar_venda),
    }
 
    while True:
        print("\n1-Cadastrar  2-Editar  3-Listar  4-Buscar  5-Estoque  6-Venda  0-Sair")
        op = input("Opcao: ").strip()
        if op == "0":
            break
        elif op in opcoes:
            opcoes[op][1]()
        else:
            print("Invalido!")
