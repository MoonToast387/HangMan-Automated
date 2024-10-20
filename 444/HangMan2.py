import csv


def citeste_fisierul_si_identifica_cuvintele(fisier):
    numar_incercari = 0 #Stocam numarul total de incercari
    rezultate = [] #Stocam rezultatele obtinute

    with open(fisier, newline='') as csvfile: #Deschidem fisierul csv
        csvreader = csv.reader(csvfile, delimiter=';') #Determinam delimitatorul
        for row in csvreader:
            cod_joc = row[0] #Codul jocului
            cuvant_partial = row[1] #Cuvintele inca negasite
            cuvant_final = row[2] #Cuvantul final gasit

            numar_incercari += identifica_cuvant(cuvant_partial, cuvant_final) #Apelam functia "identifica_cuvant" care returneaza cate incercari sunt necesare pentru a gasi cuvantul
            rezultate.append((cod_joc, cuvant_partial, cuvant_final)) #Stocam "cod_joc, cuvant_partial, cuvant_final" in rezultate

    return numar_incercari, rezultate


def identifica_cuvant(cuvant_partial, cuvant_final): #Numaram cate caractere din cuvantul partial trebuie sa gichim pentru a gasi rezultatul
    incercari = 0
    # Verificam fiecare caracter si verificam daca este cunoscut sau nu ('*')
    for i in range(len(cuvant_partial)):
        if cuvant_partial[i] == '*':
            # Inlocuim doar caracterele necunoscute!
            incercari += 1
    return incercari


fisier_csv = 'cuvinte_joc.csv'  # Numele fisierului CSV
numar_total_incercari, rezultate = citeste_fisierul_si_identifica_cuvintele(fisier_csv)

print(f'Numărul total de încercări: {numar_total_incercari}')
