import numpy as np
from scipy.optimize import minimize

coordinates = np.array([
    [2, 8],  # Toko A
    [6, 2],  # Toko B
    [8, 6],  # Toko C
    [3, 3]   # Toko D
])

weights = np.array([20, 10, 30, 15])

def total_weighted_distance(location):
    x, y = location

    distances = np.sqrt(
        (x - coordinates[:, 0])**2 +
        (y - coordinates[:, 1])**2
    )

    return np.sum(weights * distances)

initial_guess = [5, 5]

result = minimize(
    total_weighted_distance,
    initial_guess,
    method="SLSQP",
    bounds=[(None, None), (None, None)],
    options={
        "ftol": 1e-12,
        "maxiter": 1000
    }
)

if result.success:
    optimal_x, optimal_y = result.x
    minimum_distance = total_weighted_distance(result.x)

    print("HASIL D8A - OPTIMASI LOKASI GUDANG")

    print(f"Status optimasi       : {result.message}")
    print(f"Koordinat gudang X    : {optimal_x:.6f} km")
    print(f"Koordinat gudang Y    : {optimal_y:.6f} km")
    print(f"Total jarak tertimbang: {minimum_distance:.6f} km-pengiriman")

else:
    print("Optimasi D8A gagal:", result.message)


total_weight = np.sum(weights)

center_x = np.sum(weights * coordinates[:, 0]) / total_weight
center_y = np.sum(weights * coordinates[:, 1]) / total_weight

center_distance = total_weighted_distance([center_x, center_y])

print("HASIL D8B - TITIK PUSAT GRAVITASI")

print(f"Total pengiriman      : {total_weight}")
print(f"Koordinat pusat X    : {center_x:.6f} km")
print(f"Koordinat pusat Y    : {center_y:.6f} km")
print(f"Total jarak tertimbang: {center_distance:.6f} km-pengiriman")

print("PERBANDINGAN D8A DAN D8B")

print(f"Jarak optimal (D8A)  : {minimum_distance:.6f}")
print(f"Jarak pusat (D8B)    : {center_distance:.6f}")
print(f"Selisih jarak        : {center_distance - minimum_distance:.6f}")

print("\nKesimpulan:")
print("Hasilnya berbeda karena metode pusat gravitasi menghitung rata-rata koordinat berdasarkan bobot pengiriman")
print("sedangkan optimasi D8a secara langsung mencari lokasi yang meminimalkan total jarak tertimbang.")
print("Oleh karena itu, lokasi optimal menghasilkan total jarak yang lebih kecil")
print("sebesar 2,8712 km-pengiriman/bulan dibandingkan titik pusat gravitasi.")

