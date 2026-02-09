import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN

# 1. Setup Precision
getcontext().prec = 110
PI_100 = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")

def get_pi(digits, mode):
    if mode == 'round':
        return PI_100.quantize(Decimal(f'1.{"0"*digits}'), rounding=ROUND_HALF_UP)
    return PI_100.quantize(Decimal(f'1.{"0"*digits}'), rounding=ROUND_DOWN)

# 2. Run the Comparison
precisions = [4, 20, 40, 60, 100]
distance = 1_000_000 # Imagine a path of 1 million km

results_r, results_t = [], []

print(f"{'Digits':<8} | {'Rounding Error (km)':<20} | {'Truncation Error (km)'}")
print("-" * 60)

for p in precisions:
    # Calculate error for rounding and truncation
    err_r = abs((PI_100 * distance) - (get_pi(p, 'round') * distance))
    err_t = abs((PI_100 * distance) - (get_pi(p, 'trunc') * distance))
    
    results_r.append(err_r)
    results_t.append(err_t)
    
    print(f"{p:<8} | {err_r:<20.4E} | {err_t:.4E}")

# 3. Plotting
plt.figure(figsize=(8, 5))
plt.plot(precisions, results_r, 'b-o', label='Rounding')
plt.plot(precisions, results_t, 'r--x', label='Truncation')
plt.yscale('log')
plt.title('How Pi Precision Affects a 1 Million km Path')
plt.xlabel('Decimal Places of Pi')
plt.ylabel('Error Distance (km)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()