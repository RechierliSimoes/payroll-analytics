from faker import Faker
import pandas as pd
from pathlib import Path
import random

fake = Faker("pt_BR")

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "fake_payrolls"
OUTPUT_DIR.mkdir(exist_ok=True)

data = []

for _ in range(10):
    salario = random.randint(2000, 8000)
    descontos = salario * 0.2

    data.append({
        "Nome": fake.name(),
        "CPF": fake.cpf(),
        "Cargo": fake.job(),
        "Salário Bruto": salario,
        "Descontos": descontos,
        "Salário Líquido": salario - descontos,
    })

df = pd.DataFrame(data)

file_path = OUTPUT_DIR / "folha_pagamento_ficticia.xlsx"
df.to_excel(file_path, index=False)

print(f"Arquivo gerado em: {file_path}")
