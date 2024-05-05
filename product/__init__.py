from faker import Faker
import random


def product_generator():
    fake = Faker()

    categoria = random.choice(['Alimentos', 'Bebidas', 'Produtos de Limpeza', 'Higiene Pessoal', 'Produtos para Casa', 'Utensílios Domésticos'])
    if categoria == 'Alimentos':
        produto =  fake.word(ext_word_list=["Salame", "Salsicha", "Bacon", "Queiro","Mortadela","Farinha", "Arroz"]) + " " +  fake.company()
    elif categoria == 'Bebidas':
        produto = fake.word(ext_word_list=["Vodka", "Cerveja", "Refrigerante", "Yogurt", "Agua"]) + " " +  fake.company()
    elif categoria == 'Produtos de Limpeza':
        produto = fake.word(ext_word_list=["Detergente", "Desinfetante", "Lustra Móveis", "Água Sanitária"]) + " " +  fake.company()
    elif categoria == 'Higiene Pessoal':
        produto = fake.word(ext_word_list=["Sabonete", "Shampoo", "Condicionador", "Creme Dental"]) + " " + fake.word(ext_word_list=["Fresh", "Natural", "Revitalizante", "Refrescante"])
    elif categoria == 'Produtos para Casa':
        produto = fake.word(ext_word_list=["Vassoura", "Pano de Limpeza", "Esponja", "Balde"]) + " " +  fake.company()
    elif categoria == 'Utensílios Domésticos':
        produto = fake.word(ext_word_list=["Panela", "Talher", "Prato", "Copo"]) + " " + fake.word(ext_word_list=["Inox", "de Vidro", "Plástico", "Descartável"]) + " " +  fake.company()
    return (produto)

# Imprimir os produtos