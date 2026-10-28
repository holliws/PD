# ----------------------------------------------------------------------
# C1. Python — rīks ar servisa nosaukumu
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram servisa nosaukumu padod kā argumentu komandrindā. Skripts izvada, cik šim servisam žurnālā ir ERROR rindu, un parāda pirmās divas no tām. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ---------------------------------------------------------------------- 
with open("sistema.log", encoding="utf-8") as file:
    x = input("ievadi servisu")
    y = 2
    count = 0
    if x == '':
      print("dont do that")
      sys.exit()
    for rinda in file:
      if x and "ERROR" in rinda:
        count +=1
        if y != 0 :
          print(rinda)
          y = y-1
