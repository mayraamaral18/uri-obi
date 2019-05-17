renda = float(input())

if 0 < renda <= 2000.00:
    print("Isento")

elif 2000.01 <= renda <= 3000.00:
    # subtrai a parte isenta:
    imposto = (renda-2000)*0.08
    print("R$ %.2f" %imposto)

elif 3000.01 <= renda <= 4500.00:
    # subtrai a parte isenta e a parte tarifada em 8%, para adicionar logo em seguida apenas a taxação
    imposto = ((renda-3000)*0.18) + (1000.00*0.08)
    print("R$ %.2f" %imposto)

elif renda > 4500.00:
    # subtrai a parte isenta e a parte tarifada em 8% e em 18%, para adicionar logo em seguida apenas a taxação
    imposto = ((renda-4500)*0.28) + (1000.00*0.08) + (1500.00*0.18)
    print("R$ %.2f" %imposto)
