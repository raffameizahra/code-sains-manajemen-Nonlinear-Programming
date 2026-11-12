from scipy.optimize import minimize

def profit(x):
    x1, x2 = x
    return 6*x1 - 0.1*x1**2 + 8*x2 - 0.2*x2**2

def objective(x):
    return -profit(x)

def constraint(x):
    x1, x2 = x
    return x1 + 2*x2 - 40

initial_guess = [10, 10]

result = minimize(
    objective,
    initial_guess,
    method="SLSQP",
    bounds=[(0, None), (0, None)],
    constraints={"type": "eq", "fun": constraint},
    options={"ftol": 1e-12, "maxiter": 1000}
)

if result.success:
    x1_opt, x2_opt = result.x

    lambda_rupiah = (6 - 0.2*x1_opt) * 1_000_000
    profit_rupiah = profit(result.x) * 1_000_000

    print("HASIL OPTIMASI NOMOR 7")
    print(f"Status optimasi       : {result.message}")
    print(f"Jumlah kursi (x1)     : {x1_opt:.0f} unit")
    print(f"Jumlah meja (x2)      : {x2_opt:.0f} unit")
    print(f"Lambda                : Rp{lambda_rupiah:,.0f}")
    print(f"Profit maksimum       : Rp{profit_rupiah:,.0f}")
    print(f"Penggunaan mesin      : {x1_opt + 2*x2_opt:.0f} jam")

else:
    print("Optimasi gagal:", result.message)
