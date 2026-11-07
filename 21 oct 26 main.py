avg1 = (80 + 90 + 85) / 3
print('Aman:', avg1)
avg2 = (35 + 30 + 38) / 3
print('Karan:', avg2)



m1_aman, m2_aman, m3_aman = 80, 90, 85
avg_aman = (m1_aman + m2_aman + m3_aman) / 3
status_aman = 'PASS' if avg_aman >= 40 else 'FAIL'
print(f'Aman: {avg_aman:.1f}% ({status_aman})')

m1_karan, m2_karan, m3_karan = 35, 30, 38
avg_karan = (m1_karan + m2_karan + m3_karan) / 3
status_karan = 'PASS' if avg_karan >= 40 else 'FAIL'
print(f'Karan: {avg_karan:.1f}% ({status_karan})')

m1_priya, m2_priya, m3_priya = 75, 82, 88
avg_priya = (m1_priya + m2_priya + m3_priya) / 3
status_priya = 'PASS' if avg_priya >= 40 else 'FAIL'
print(f'Priya: {avg_priya:.1f}% ({status_priya})')
