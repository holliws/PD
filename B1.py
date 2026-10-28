# ----------------------------------------------------------------------
# B1. Python — rindu skaits pa līmeņiem
# ----------------------------------------------------------------------

# Saskaiti, cik žurnālā ir rindu katram līmenim, un izvadi tos no biežākā uz retāko. Aizpildi abas vietas, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms saraksta izvadi tekstu "Limenu kopsavilkums".

skaits = {}
print(" lIMENU kopsavilkums")
y = 0
with open("sistema.log", encoding="utf-8") as file:
    for rinda in file:
        limenis = rinda.split()[2]
        if limenis not in skaits:
          skaits[limenis] = 0
        else:
          skaits[limenis] +=1
    sorted_skaits = dict(sorted(skaits.items(), key=lambda item: item[1], reverse=True))
  print(sorted_skaits)

        # TODO: pieskaiti vienu šim līmeni
# TODO: izvadi sakārtotus no lielākā uz mazāko
